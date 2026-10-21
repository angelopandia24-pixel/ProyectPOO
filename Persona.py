from datetime import date
from abc import ABC, abstractmethod
# 1. PERSONAS Y USUARIOS (Docente, Estudiante, Director Escuela)


class Persona(ABC):
    def __init__(self, dni: int, nombres_personas: str, apellido_paterno: str, apellido_materno: str) -> None:
        self.dni: int = dni
        self.nombres_personas: str = self.nombres_personas
        self.apellido_paterno: str = apellido_paterno
        self.apellido_materno: str = apellido_materno

    def rol_persona(self) -> str:
        return "Persona"
class Docente(Persona):
    def __init__(self, id_persona: int, nombres: str, apellido_paterno: str, apellido_materno: str, id_docente: int) -> None:
        super().__init__(id_persona, nombres, apellido_paterno, apellido_materno)
        self.id_docente: int = id_docente

    def rol_docente(self) -> str:
        return f"Docente (ID: {self.id_docente})"

class Estudiante(Persona):
    def __init__(self, id_persona: int, nombres: str, apellido_paterno: str, apellido_materno: str, codigo_estudiante: int, id_escuela_profesional: str) -> None:
        super().__init__(id_persona, nombres, apellido_paterno, apellido_materno)
        self.codigo_estudiante: int = codigo_estudiante
        self.id_escuela_profesional: str = id_escuela_profesional
    def rol_persona(self) -> str:
        """Sobrescribe el rol base indicando que es un estudiante."""
        return f"Estudiante - Escuela: {self.id_escuela_profesional}"
class DirectorEscuela(Persona):
    """Representa al director de una escuela profesional."""
    def __init__(self, id_director: int, id_persona, nombres, apellido_paterno, apellido_materno) -> None:
        super().__init__(id_persona, nombres, apellido_paterno, apellido_materno)
        self.id_director: int = id_director

    def rol_director(self) -> str:
        """Retorna el rol del director."""
        return f"Director de Escuela ID: {self.id_director}"

class Secretaria(Persona):
    def __init__(self, id_secretario, id_persona, nombres, apellido_paterno, apellido_materno):
        super().__init__(id_persona, nombres, apellido_paterno, apellido_materno)
        self.id_secretaria = id_secretario    
# 2. ESTRUCTURA ACADÉMICA Y DEPARTAMENTOS
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


class DepartamentoAcademico:
    """Representa un departamento académico dentro de la institución."""

    def __init__(self, id_departamento_academico: int, id_escuela_profesional: str) -> None:
        self.id_departamento_academico: int = id_departamento_academico
        self.id_escuela_profesional: str = id_escuela_profesional

    def procesar(self) -> str:
        """Procesa las operaciones administrativas del departamento."""
        return f"Procesando departamento {self.id_departamento_academico}"


class FacultadAcademica:
    """Representa la Facultad Académica."""

    def __init__(self, id_facultad_academica: int, id_escuela_profesional: str, id_director_escuela: str) -> None:
        self.id_facultad_academica: int = id_facultad_academica
        self.id_escuela_profesional: str = id_escuela_profesional
        self.id_director_escuela: str = id_director_escuela


# 3. PLAN DE ESTUDIOS Y CURSOS

class PlanEstudio:
    """Gestiona el plan de estudios de la carrera."""

    def __init__(self, id_plan_estudio: int, id_escuela_profesional: str, creditos_obligatorios: int, creditos_electivos: int, creditos_extracurriculares: int) -> None:
        self.id_plan_estudio: int = id_plan_estudio
        self.id_escuela_profesional: str = id_escuela_profesional
        self.creditos_obligatorios: int = creditos_obligatorios
        self.creditos_electivos: int = creditos_electivos
        self.creditos_extracurriculares: int = creditos_extracurriculares

    def operaciones_plan_estudio(self) -> int:
        """Calcula la suma total de créditos requeridos en el plan de estudios."""
        return self.creditos_obligatorios + self.creditos_electivos + self.creditos_extracurriculares


class Curso:
    """Representa una asignatura del plan académico."""

    def __init__(self, id_curso: int, codigo_curso: str, nombre_curso: str,
                 creditos_teoricos: int, creditos_practicos: int, creditos_curso: int) -> None:
        self.id_curso: int = id_curso
        self.codigo_curso: str = codigo_curso
        self.nombre_curso: str = nombre_curso
        self.creditos_teoricos: int = creditos_teoricos
        self.creditos_practicos: int = creditos_practicos
        self.creditos_curso: int = creditos_curso

    def cantidad_horas_teoricas(self) -> int:
        """Calcula las horas semanales teóricas (1 crédito teórico = 1 hora)."""
        return self.creditos_teoricos

    def cantidad_horas_practicas(self) -> int:
        """Calcula las horas semanales prácticas (1 crédito práctico = 2 horas)."""
        return self.creditos_practicos * 2



# 4. GESTIÓN PERÍODO ACADÉMICO Y SECCIONES

class PeriodoAcademico:
    """Maneja los rangos de fechas y configuración del semestre o período actual."""

    def __init__(self, id_periodo_academico: int, nombre_periodo: str, numero_periodo: str,
                 fecha_inicio: date, fecha_final: date, estado_academico: str,
                 nota_minima_ap: int, nota_maxima_ap: int) -> None:
        self.id_periodo_academico: int = id_periodo_academico
        self.nombre_periodo: str = nombre_periodo
        self.numero_periodo: str = numero_periodo
        self.fecha_inicio: date = fecha_inicio
        self.fecha_final: date = fecha_final
        self.estado_academico: str = estado_academico
        self.nota_minima_ap: int = nota_minima_ap
        self.nota_maxima_ap: int = nota_maxima_ap

    def evaluar_fecha(self) -> bool:
        """Verifica si la fecha actual está dentro del rango del período."""
        hoy = date.today()
        return self.fecha_inicio <= hoy <= self.fecha_final

    def evaluacion_fecha_inicial(self) -> bool:
        """Verifica si el período ya dio inicio."""
        return date.today() >= self.fecha_inicio

    def evaluacion_fecha_final(self) -> bool:
        """Verifica si el período ya ha finalizado."""
        return date.today() > self.fecha_final

    def fecha_matricula(self) -> bool:
        """Valida si el estado actual del período está activo para matrículas."""
        return self.estado_academico.upper() == "ACTIVO"


class Seccion:
    """Gestiona el grupo de clase, sus cupos y estudiantes matriculados."""

    def __init__(self, id_seccion: int, id_curso:int, id_docente: int, id_periodo_academico: int, vacantes_disponibles: int) -> None:
        self.id_seccion: int = id_seccion
        self.id_curso: int = id_curso
        self.id_docente: int = id_docente
        self.id_periodo_academico: int = id_periodo_academico
        self.vacantes_disponibles: int = vacantes_disponibles
        self.cantidad_matriculados: int = 0

    def vacantes_disponibles_seccion(self) -> int:
        """Retorna las vacantes que aún quedan libres."""
        return self.vacantes_disponibles - self.cantidad_matriculados

    def matriculados_totales(self) -> int:
        """Devuelve el total acumulado de matriculados."""
        return self.cantidad_matriculados

    def retirados_totales(self) -> int:
        """Calcula el total de vacantes liberadas por retirados (métrica demostrativa)."""
        return max(0, self.vacantes_disponibles - self.cantidad_matriculados)


# 5. REGISTRO Y MATRÍCULA


class RegistroMatricula:
    """Entidad encarga de la recepción del registro de matrícula."""

    def __init__(self, id_registro: int, nombre_registro: str) -> None:
        self.id_registro: int = id_registro
        self.nombre_registro: str = nombre_registro

    def procesamiento(self) -> str:
        """Procesa y valida la constancia del registro."""
        return f"Registro '{self.nombre_registro}' (ID: {self.id_registro}) procesado exitosamente."



if __name__ == "__main__":
    # Instanciación de Período Académico
    periodo = PeriodoAcademico(
        id_periodo_academico=1,
        nombre_periodo="2026-I",
        numero_periodo="01",
        fecha_inicio=date(2026, 3, 1),
        fecha_final=date(2026, 7, 31),
        estado_academico="ACTIVO",
        nota_minima_ap=11,
        nota_maxima_ap=20
    )

    # Instanciación de Curso y Plan de Estudios
    curso_poo = Curso(
        id_curso=101,
        codigo_curso="IS-282",
        nombre_curso="Programación Orientada a Objetos",
        creditos_teoricos=2,
        creditos_practicos=2,
        creditos_curso=4
    )

    plan = PlanEstudio(
        id_plan_estudio=2026,
        id_escuela_profesional="EPIS",
        creditos_obligatorios=160,
        creditos_electivos=20,
        creditos_extracurriculares=10
    )

    # Instanciación de Personas y Roles
    estudiante = Estudiante(
        id_persona=1,
        nombres="Angelo",
        apellido_paterno="Pandia",
        apellido_materno="Caceres",
        id_estudiante=2026001,
        id_escuela_profesional="Ingeniería de Sistemas"
    )

    seccion = Seccion(id_seccion=10, id_docente=5, id_periodo_academico=1, vacantes_disponibles=30)
    seccion.cantidad_matriculados += 1

    registro = RegistroMatricula(id_registro=5001, nombre_registro="Matrícula Regular 2026")

    # Muestra de Salida de Control
    print("=== SISTEMA ACADÉMICO UML DEPURADO ===")
    print(f"Estudiante: {estudiante.nombres} {estudiante.apellido_paterno} | Rol: {estudiante.rol_persona()}")
    print(f"Curso: {curso_poo.codigo_curso} - {curso_poo.nombre_curso} | Horas Prácticas: {curso_poo.cantidad_horas_practicas()}h")
    print(f"Créditos Totales del Plan: {plan.operaciones_plan_estudio()} créditos")
    print(f"Vacantes Libres Sección: {seccion.vacantes_disponibles_seccion()}")
    print(f"Estado Matrícula Período: {'Habilitado' if periodo.fecha_matricula() else 'Cerrado'}")
    print(f"Estado Registro: {registro.procesamiento()}")