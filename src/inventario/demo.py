from producto import Producto
from observadores import AlertaStockMinimo, RegistroMovimientos

arroz = Producto(1, "Arroz 5 lb", 45.0, 12, 5)
arroz.agregarObservador(AlertaStockMinimo())
arroz.agregarObservador(RegistroMovimientos())

arroz.actualizarStock(-4, "Venta")    # sin alerta
arroz.actualizarStock(-4, "Venta")    # dispara alerta (4 <= 5)
arroz.actualizarStock(20, "Compra")   # entrada de proveedor