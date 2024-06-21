class Profesor:
    def __init__(self, nombre, apellido, asignaturas):
        self.nombre = nombre
        self.apellido = apellido
        self.asignaturas = asignaturas

    def mostrar_info(self):
        info = f"Profesor: {self.nombre} {self.apellido}\nAsignaturas: {', '.join(self.asignaturas)}"
        return info
