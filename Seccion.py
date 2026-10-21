class Seccion:
    def __init__(self, codigo: str, codigo_curso: str, codigo_periodo: str, vacantes: int):
        self._codigo = codigo
        self._codigo_curso = codigo_curso
        self._codigo_periodo = codigo_periodo
        self._matriculados = 0
        self.vacantes = vacantes

    @property
    def vacantes(self) -> int:
        return self._vacantes

    @vacantes.setter
    def vacantes(self, valor: int):
        if valor <= 0:
            raise ValueError("El número de vacantes debe ser mayor a 0.")
        if valor < self._matriculados:
            raise ValueError("No se pueden reducir vacantes por debajo de los matriculados.")
        self._vacantes = valor

    @property
    def matriculados(self) -> int:
        return self._matriculados

    @property
    def vacantes_disponibles(self) -> int:
        return self._vacantes - self._matriculados

    def matricular_estudiante(self):
        if self.vacantes_disponibles <= 0:
            raise ValueError("Matrícula rechazada: la sección está llena.")
        self._matriculados += 1

    def retirar_estudiante(self):
        if self._matriculados <= 0:
            raise ValueError("No hay estudiantes matriculados para retirar.")
        self._matriculados -= 1