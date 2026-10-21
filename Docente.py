from Persona import Persona
class Docente(Persona):
    def __init__(self, dni: str, nombres: str, apellidos: str, codigo_docente: str):
        super().__init__(dni, nombres, apellidos)
        self._codigo_docente = codigo_docente

    def rol_persona(self) -> str:
        return f"Docente (Código: {self._codigo_docente})"