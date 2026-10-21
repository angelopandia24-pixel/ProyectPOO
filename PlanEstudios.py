from EntidadNombrada import EntidadNombrada

class PlanEstudios(EntidadNombrada):  # Inyosmo ti 's' iti ingana ti PlanEstudios
    def __init__(self, nombre: str, anio_aprobacion: int, obligatorios: int, electivos: int, extracurriculares: int, vigente: int):
        super().__init__(nombre, max_longitud=36)
        self._anio_aprobacion = anio_aprobacion
        self._creditos_obligatorios = max(0, obligatorios)
        self._creditos_electivos = max(0, electivos)
        self._creditos_extracurriculares = max(0, extracurriculares)
        self.vigente = vigente

    @property
    def vigente(self) -> bool:
        return self._vigente_int == 1

    @vigente.setter
    def vigente(self, valor_int: int):
        if valor_int not in (0, 1):
            raise ValueError("El estado de vigencia internamente debe ser 0 o 1.")
        self._vigente_int = valor_int

    @property
    def total_creditos(self) -> int:
        return self._creditos_obligatorios + self._creditos_electivos + self._creditos_extracurriculares

    def obtener_resumen(self) -> str:
        estado = "Vigente" if self.vigente else "No Vigente"
        return f"Plan: {self.nombre} ({self._anio_aprobacion}) - Total Créditos: {self.total_creditos} - {estado}"