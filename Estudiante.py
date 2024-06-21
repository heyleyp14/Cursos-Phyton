class Estudiante:
    def __init__(self, nombre, apellido, id_estudiante):
        self.nombre = nombre
        self.apellido = apellido
        self.id_estudiante = id_estudiante
        self.cursos = []

    def mostrar_info(self):
        info = f"Estudiante: {self.nombre} {self.apellido}\nID: {self.id_estudiante}\nCursos: {[curso.nombre for curso in self.cursos]}"
        return info
