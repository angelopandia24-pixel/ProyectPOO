from datetime import date
from enum import Enum
from EntidadNombrada import EntidadNombrada

class EstadoPeriodo(Enum):
    PLANIFICADO = 1
    EN_CURSO = 2
    MATRICULA_CERRADA = 3
    FINALIZADO = 4

class PeriodoAcademico(EntidadNombrada):
    def __init__(self, nombre: str, numero: str, anio: int, 
                 f_inicio: date, f_fin: date, f_mat_inicio: date, f_mat_fin: date, 
                 es_verano: int, nota_minima: float, estado: EstadoPeriodo):
        super().__init__(nombre, max_longitud=45)
        self._numero = numero
        self._anio = anio
        self.cambiar_fechas_periodo(f_inicio, f_fin)
        self.cambiar_fechas_matricula(f_mat_inicio, f_mat_fin)
        self.es_verano = es_verano
        self.nota_minima = nota_minima
        self.estado = estado

    def cambiar_fechas_periodo(self, inicio: date, fin: date):
        if fin < inicio:
            raise ValueError("La fecha de fin no puede ser anterior a la de inicio.")
        self._fecha_inicio = inicio
        self._fecha_fin = fin

    def cambiar_fechas_matricula(self, inicio: date, fin: date):
        if fin < inicio:
            raise ValueError("La fecha fin de matrícula no puede ser anterior a la de inicio.")
        self._fecha_mat_inicio = inicio
        self._fecha_mat_fin = fin

    @property
    def es_verano(self) -> bool:
        return self._es_verano_int == 1

    @es_verano.setter
    def es_verano(self, valor: int):
        if valor not in (0, 1):
            raise ValueError("El valor de es_verano debe ser 0 o 1.")
        self._es_verano_int = valor

    @property
    def nota_minima(self) -> float:
        return self._nota_minima

    @nota_minima.setter
    def nota_minima(self, valor: float):
        if not (0 <= valor <= 20):
            raise ValueError("La nota mínima aprobatoria debe estar entre 0 y 20.")
        self._nota_minima = valor

    def obtener_resumen(self) -> str:
        return f"Período: {self.nombre} ({self._anio}-{self._numero}) - Estado: {self.estado.name}"