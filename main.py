from Curso import Curso
from PlanEstudios import PlanEstudios
from PeriodoAcademico import PeriodoAcademico, EstadoPeriodo
from datetime import date

# Lista mixta de entidades
registros = [
    Curso("C1", "IS-282", "Ingeniería de Software", 4.0, 3, 2, 0, 0),
    PlanEstudios("Plan 2026 Sistemas", 2026, 120, 30, 10, 1),
    PeriodoAcademico("Semestre 2026-I", "I", 2026, date(2026, 3, 1), date(2026, 7, 15), 
                     date(2026, 2, 1), date(2026, 2, 28), 0, 10.5, EstadoPeriodo.EN_CURSO)
]

# Polimorfismo sin necesidad de evaluar el tipo (isinstance)
for registro in registros:
    print(registro.obtener_resumen())