class Evaluacion:
    def __init__(self, curso, estudiante, nota):
        self.curso = curso
        self.estudiante = estudiante
        self.nota = nota

    def mostrar_info(self):
        info = f"Evaluación de {self.estudiante.nombre} en el curso {self.curso.nombre}\nNota: {self.nota}"
        return info
