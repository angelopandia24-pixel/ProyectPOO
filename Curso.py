from EntidadNombrada import EntidadNombrada
class Curso(EntidadNombrada):
    def __init__(self, id_curso: str, codigo: str, nombre: str, creditos: float, 
                 horas_teoricas: int, horas_practicas: int, horas_seminario: int, horas_virtuales: int):
        super().__init__(nombre, max_longitud=200)
        self._id_curso = id_curso  # Identificador inmutable
        self._codigo = codigo
        self.creditos = creditos
        self.horas_teoricas = horas_teoricas
        self.horas_practicas = horas_practicas
        self.horas_seminario = horas_seminario
        self.horas_virtuales = horas_virtuales

    @property
    def id_curso(self) -> str:
        return self._id_curso

    @property
    def creditos(self) -> float:
        return self._creditos

    @creditos.setter
    def creditos(self, valor: float):
        if valor <= 0:
            raise ValueError("Los créditos deben ser mayores a 0.")
        self._creditos = round(valor, 2)

    def _validar_hora(self, valor: int) -> int:
        if not (0 <= valor <= 255):
            raise ValueError("Las horas deben estar entre 0 y 255.")
        return valor

    @property
    def horas_teoricas(self) -> int: 
        return self._horas_teoricas
    @horas_teoricas.setter
    def horas_teoricas(self, v: int): 
        self._horas_teoricas = self._validar_hora(v)

    @property
    def horas_practicas(self) -> int: return self._horas_practicas
    @horas_practicas.setter
    def horas_practicas(self, v: int): 
        self._horas_practicas = self._validar_hora(v)

    @property
    def horas_seminario(self) -> int: return self._horas_seminario
    @horas_seminario.setter
    def horas_seminario(self, v: int): self._horas_seminario = self._validar_hora(v)

    @property
    def horas_virtuales(self) -> int: return self._horas_virtuales
    @horas_virtuales.setter
    def horas_virtuales(self, v: int): self._horas_virtuales = self._validar_hora(v)

    @property
    def horas_totales(self) -> int:
        # Calculado en tiempo de ejecución para evitar inconsistencias
        return self._horas_teoricas + self._horas_practicas + self._horas_seminario + self._horas_virtuales
    def obtener_resumen(self) -> str:
        return f"Curso: {self.nombre} ({self._codigo}) - {self.creditos} Créditos"