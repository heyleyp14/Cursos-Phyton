class Asignatura:
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor

    def mostrar_info(self):
        info = f"Asignatura: {self.nombre}\nProfesor: {self.profesor.nombre}"
        return info


  