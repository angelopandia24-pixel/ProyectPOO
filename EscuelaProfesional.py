class EscuelaProfesional:
    """Representa una Escuela Profesional dentro de una facultad."""

    def __init__(self, id_escuela_profesional: int, id_facultad_academica: int, perfil_egresado: str, id_docente: int, id_director: int, id_secretario: str) -> None:
        self.id_escuela_profesional: int = id_escuela_profesional
        self.id_facultad_academica: int = id_facultad_academica
        self.perfil_egresado: str = perfil_egresado
        self.id_docente: int = id_docente
        self.id_director: int = id_director

    def informacion_general(self) -> str:
        """Genera un resumen de la escuela profesional."""
        return f"Escuela Profesional ID: {self.id_escuela_profesional} (Facultad ID: {self.id_facultad_academica})"
