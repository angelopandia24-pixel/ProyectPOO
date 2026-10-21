from abc import ABC, abstractmethod

class EntidadNombrada(ABC):
    def __init__(self, nombre: str, max_longitud: int):
        self._max_longitud = max_longitud
        self.nombre = nombre  # Invoca al setter con validación

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str):
        if not valor or not valor.strip():
            raise ValueError("El nombre no puede estar vacío.")
        if len(valor.strip()) > self._max_longitud:
            raise ValueError(f"El nombre no puede exceder los {self._max_longitud} caracteres.")
        self._nombre = valor.strip()

    @abstractmethod
    def obtener_resumen(self) -> str:
        """Devuelve un resumen identificativo de la entidad."""
        pass