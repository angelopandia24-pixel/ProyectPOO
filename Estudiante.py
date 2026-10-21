from Persona import Persona,  abstractmethod
class Estudiante(Persona):
    def __init__(self, dni: str, nombres: str, apellidos: str, codigo_estudiante: str, codigo_escuela: str):
        super().__init__(dni, nombres, apellidos)
        self._codigo_estudiante = codigo_estudiante
        self._codigo_escuela = codigo_escuela

    def rol_persona(self) -> str:
        return f"Estudiante (Código: {self._codigo_estudiante}, Escuela: {self._codigo_escuela})"