from abc import ABC, abstractmethod


class ObservadorStock(ABC):
    """Interfaz que deben implementar quienes reaccionan a cambios de stock."""

    @abstractmethod
    def actualizar(self, producto, motivo):
        pass