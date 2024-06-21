class Curso:
    def __init__(self, nombre, profesor, horario):
        self.nombre = nombre
        self.profesor = profesor
        self.estudiantes = []
        self.horario = horario

    def mostrar_info(self):
        info = f"Curso: {self.nombre}\nProfesor: {self.profesor.nombre}\nHorario: {self.horario.dia} {self.horario.hora_inicio} - {self.horario.hora_fin}\nEstudiantes: {[estudiante.nombre for estudiante in self.estudiantes]}"
        return info

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
