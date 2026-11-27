class Producto:
    """Sujeto observado: notifica cuando cambia su stock (RF02)."""

    def __init__(self, id, nombre, precio, stock, stockMinimo):
        if not self._es_entero(stock) or stock < 0:
            raise ValueError("El stock inicial debe ser un entero mayor o igual a 0")
        if not self._es_entero(stockMinimo) or stockMinimo < 0:
            raise ValueError("El stock mínimo debe ser un entero mayor o igual a 0")
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.stockMinimo = stockMinimo
        self._observadores = []

    @staticmethod
    def _es_entero(valor):
        return isinstance(valor, int) and not isinstance(valor, bool)

    def agregarObservador(self, observador):
        if observador not in self._observadores:
            self._observadores.append(observador)

    def quitarObservador(self, observador):
        self._observadores.remove(observador)

    def _notificar(self, motivo):
        for observador in list(self._observadores):
            try:
                observador.actualizar(self, motivo)
            except Exception as error:
                print(f"AVISO: el observador {type(observador).__name__} "
                      f"falló: {error}")

    def actualizarStock(self, cantidad, motivo):
        """cantidad negativa = venta (RF04); positiva = compra (RF06)."""
        if not self._es_entero(cantidad) or cantidad == 0:
            raise ValueError("La cantidad debe ser un entero distinto de 0")
        if self.stock + cantidad < 0:
            raise ValueError("Stock insuficiente")
        self.stock += cantidad
        self._notificar(motivo)