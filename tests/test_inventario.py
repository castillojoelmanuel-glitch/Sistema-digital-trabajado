"""Pruebas del componente de control de existencias (patrón Observer).

CP-01 Registrar venta       | CP-02 Registrar compras | CP-03 Gestionar productos
CP-04 Consultar inventario  | CP-05 Consultar reportes
"""
from types import SimpleNamespace

import pytest

from producto import Producto
from observador import ObservadorStock
from observadores import AlertaStockMinimo, RegistroMovimientos


class ObservadorEspia(ObservadorStock):
    """Observador de prueba: guarda las notificaciones que recibe."""

    def __init__(self):
        self.avisos = []

    def actualizar(self, producto, motivo):
        self.avisos.append((producto.nombre, motivo, producto.stock))


class ObservadorDefectuoso(ObservadorStock):
    """Observador de prueba: siempre falla al ser notificado."""

    def actualizar(self, producto, motivo):
        raise RuntimeError("fallo del observador")


@pytest.fixture
def arroz():
    return Producto(1, "Arroz 5 lb", 45.0, 12, 5)


# ---------------- CP-01: Registrar venta (CA1, CA3, CA4) ----------------

@pytest.mark.unit
def test_cp01_venta_correcta_descuenta_stock(arroz):
    arroz.actualizarStock(-4, "Venta")
    assert arroz.stock == 8


@pytest.mark.unit
def test_cp01_venta_mayor_al_stock_se_rechaza(arroz):
    with pytest.raises(ValueError):
        arroz.actualizarStock(-13, "Venta")
    assert arroz.stock == 12


@pytest.mark.unit
def test_cp01_venta_total_deja_stock_en_cero(arroz):
    arroz.actualizarStock(-12, "Venta")
    assert arroz.stock == 0


@pytest.mark.unit
def test_cp01_venta_con_cantidad_no_numerica_lanza_valueerror(arroz):
    with pytest.raises(ValueError):
        arroz.actualizarStock("abc", "Venta")
    assert arroz.stock == 12


@pytest.mark.unit
@pytest.mark.parametrize("stock, debe_alertar", [(6, False), (5, True), (4, True), (0, True)])
def test_cp01_alerta_segun_stock_minimo(capsys, stock, debe_alertar):
    producto = SimpleNamespace(nombre="Arroz 5 lb", stock=stock, stockMinimo=5)
    AlertaStockMinimo().actualizar(producto, "Venta")
    assert ("ALERTA" in capsys.readouterr().out) == debe_alertar


@pytest.mark.integration
def test_cp01_venta_hasta_el_minimo_dispara_alerta(arroz, capsys):
    arroz.agregarObservador(AlertaStockMinimo())
    arroz.actualizarStock(-6, "Venta")       # stock 6: sin alerta
    assert "ALERTA" not in capsys.readouterr().out
    arroz.actualizarStock(-1, "Venta")       # stock 5 = mínimo
    assert "ALERTA" in capsys.readouterr().out


# ---------------- CP-02: Registrar compras (CA2, CA3, CA4) ----------------

@pytest.mark.unit
def test_cp02_compra_correcta_incrementa_stock(arroz):
    arroz.actualizarStock(20, "Compra")
    assert arroz.stock == 32


@pytest.mark.unit
def test_cp02_compra_con_cantidad_cero_se_rechaza(arroz):
    with pytest.raises(ValueError):
        arroz.actualizarStock(0, "Compra")
    assert arroz.stock == 12


@pytest.mark.integration
def test_cp02_movimiento_vacio_no_se_notifica(arroz):
    espia = ObservadorEspia()
    arroz.agregarObservador(espia)
    try:
        arroz.actualizarStock(0, "Compra")
    except ValueError:
        pass
    assert espia.avisos == []


@pytest.mark.integration
def test_cp02_compra_que_supera_el_minimo_no_alerta(capsys):
    aceite = Producto(2, "Aceite 1 L", 120.0, 3, 5)
    aceite.agregarObservador(AlertaStockMinimo())
    aceite.actualizarStock(10, "Compra")     # stock 13
    assert "ALERTA" not in capsys.readouterr().out


@pytest.mark.integration
def test_cp02_compra_que_deja_el_stock_en_el_minimo_mantiene_alerta(capsys):
    aceite = Producto(2, "Aceite 1 L", 120.0, 0, 5)
    aceite.agregarObservador(AlertaStockMinimo())
    aceite.actualizarStock(5, "Compra")      # stock 5 = mínimo
    assert "ALERTA" in capsys.readouterr().out


# ---------------- CP-03: Gestionar productos (creación, stock mínimo y observadores) ----------------

@pytest.mark.unit
def test_cp03_producto_valido_conserva_sus_datos():
    p = Producto(7, "Habichuelas 1 lb", 60.0, 0, 5)
    assert (p.id, p.nombre, p.precio, p.stock, p.stockMinimo) == (7, "Habichuelas 1 lb", 60.0, 0, 5)


@pytest.mark.unit
def test_cp03_stock_inicial_negativo_se_rechaza():
    with pytest.raises(ValueError):
        Producto(8, "Sal 1 lb", 20.0, -1, 5)


@pytest.mark.unit
def test_cp03_stock_minimo_negativo_se_rechaza():
    with pytest.raises(ValueError):
        Producto(9, "Azúcar 5 lb", 55.0, 10, -2)


@pytest.mark.integration
def test_cp03_editar_stock_minimo_cambia_el_umbral_de_alerta(arroz, capsys):
    arroz.agregarObservador(AlertaStockMinimo())
    arroz.stockMinimo = 10
    arroz.actualizarStock(-2, "Venta")       # stock 10 = nuevo mínimo
    assert "ALERTA" in capsys.readouterr().out


@pytest.mark.integration
def test_cp03_observador_repetido_se_notifica_una_sola_vez(arroz):
    espia = ObservadorEspia()
    arroz.agregarObservador(espia)
    arroz.agregarObservador(espia)
    arroz.actualizarStock(-1, "Venta")
    assert len(espia.avisos) == 1


@pytest.mark.integration
def test_cp03_observador_retirado_deja_de_recibir_avisos(arroz):
    espia = ObservadorEspia()
    arroz.agregarObservador(espia)
    arroz.quitarObservador(espia)
    arroz.actualizarStock(-1, "Venta")
    assert espia.avisos == []


@pytest.mark.integration
def test_cp03_observador_defectuoso_no_interrumpe_a_los_demas(arroz):
    espia = ObservadorEspia()
    arroz.agregarObservador(ObservadorDefectuoso())
    arroz.agregarObservador(espia)
    arroz.actualizarStock(-1, "Venta")
    assert arroz.stock == 11
    assert len(espia.avisos) == 1


# ---------------- CP-04: Consultar inventario (CA1, CA4) ----------------

@pytest.mark.unit
def test_cp04_stock_actual_tras_varios_movimientos(arroz):
    arroz.actualizarStock(-4, "Venta")
    arroz.actualizarStock(-4, "Venta")
    arroz.actualizarStock(20, "Compra")
    assert arroz.stock == 24


@pytest.mark.integration
def test_cp04_consultar_el_stock_no_genera_notificaciones(arroz):
    espia = ObservadorEspia()
    arroz.agregarObservador(espia)
    _ = arroz.stock
    assert espia.avisos == []


@pytest.mark.integration
def test_cp04_productos_distintos_no_se_afectan_entre_si(arroz):
    aceite = Producto(2, "Aceite 1 L", 120.0, 8, 3)
    espia = ObservadorEspia()
    arroz.agregarObservador(espia)
    aceite.actualizarStock(-2, "Venta")
    assert espia.avisos == []
    assert (arroz.stock, aceite.stock) == (12, 6)


# ---------------- CP-05: Consultar reportes (CA5) ----------------

@pytest.mark.unit
def test_cp05_historial_inicia_vacio():
    assert RegistroMovimientos().historial == []


@pytest.mark.integration
def test_cp05_historial_registra_cada_movimiento_en_orden(arroz):
    registro = RegistroMovimientos()
    arroz.agregarObservador(registro)
    arroz.actualizarStock(-4, "Venta")
    arroz.actualizarStock(20, "Compra")
    assert registro.historial == [("Arroz 5 lb", "Venta", 8), ("Arroz 5 lb", "Compra", 28)]


@pytest.mark.integration
def test_cp05_movimiento_rechazado_no_se_registra(arroz):
    registro = RegistroMovimientos()
    arroz.agregarObservador(registro)
    with pytest.raises(ValueError):
        arroz.actualizarStock(-50, "Venta")
    assert registro.historial == []