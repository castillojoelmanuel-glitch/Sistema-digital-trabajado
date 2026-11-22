from observador import ObservadorStock


class AlertaStockMinimo(ObservadorStock):  # RF03
    def actualizar(self, producto, motivo):
        if producto.stock <= producto.stockMinimo:
            print(f"ALERTA: {producto.nombre} está en stock mínimo "
                  f"({producto.stock} unidades)")


class RegistroMovimientos(ObservadorStock):
    def __init__(self):
        self.historial = []

    def actualizar(self, producto, motivo):
        self.historial.append((producto.nombre, motivo, producto.stock))
        print(f"Movimiento: {motivo} | {producto.nombre} | "
              f"stock actual: {producto.stock}")
