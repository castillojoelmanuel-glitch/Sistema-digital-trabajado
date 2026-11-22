class Producto:
    """Sujeto observado: notifica cuando cambia su stock (RF02)."""

    def __init__(self, id, nombre, precio, stock, stockMinimo):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.stockMinimo = stockMinimo
        self._observadores = []

    def agregarObservador(self, observador):
        self._observadores.append(observador)

    def quitarObservador(self, observador):
        self._observadores.remove(observador)

    def _notificar(self, motivo):
        for observador in self._observadores:
            observador.actualizar(self, motivo)

    def actualizarStock(self, cantidad, motivo):
        """cantidad negativa = venta (RF04); positiva = compra (RF06)."""
        if self.stock + cantidad < 0:
            raise ValueError("Stock insuficiente")
        self.stock += cantidad
        self._notificar(motivo)
