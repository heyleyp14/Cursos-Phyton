import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
from Asignatura import Asignatura
from Curso import Curso
from Estudiante import Estudiante
from Evaluacion import Evaluacion
from Horario import Horario
from Profesor import Profesor

class InformacionGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Cursos")
        self.master.configure(bg="#C5CAE9")

        self.label = tk.Label(master, text="Sistema de gestión de cursos", font=("Arial", 18),bg="#C5CAE9")
        self.label.pack(pady=10)
        
        self.imagen = Image.open("imagen.png")
        self.imagen = self.imagen.resize((200, 200))
        self.imagen = ImageTk.PhotoImage(self.imagen)
        self.label_imagen = tk.Label(master, image=self.imagen, bg="#C5CAE9")
        self.label_imagen.pack(pady=10)

        self.horario = Horario("Viernes", "9:00", "12:00")
        self.profesor = Profesor("Miguel", "Posada", ["Programacion orientada a objetos", "Gestion de proyectos"])
        self.asignatura = Asignatura("Programacion Orientada a Objetos", self.profesor)
        self.curso = Curso("Programacion orientada a objetos", self.profesor, self.horario)
        self.estudiante = Estudiante("Heyley", "Parada", "1093887319")
        self.evaluacion = Evaluacion(self.curso, self.estudiante, 4)
        self.curso.agregar_estudiante(self.estudiante)
        self.estudiante.cursos.append(self.curso)

        self.seleccion_label = tk.Label(master, text="¿Qué información deseas ver?",bg="#E0E0E0")
        self.seleccion_label.pack()

        self.tipos_info = ["Curso", "Profesor", "Estudiante", "Asignatura", "Evaluación"]
        self.combobox = ttk.Combobox(master, values=self.tipos_info,)
        self.combobox.pack()
        self.combobox.bind("<<ComboboxSelected>>", self.actualizar_info)

        self.info_text = tk.Text(master, height=10, width=50,bg="#E0E0E0")
        self.info_text.pack(pady=10)

        self.actualizar_info() 

    def actualizar_info(self, event=None):
        seleccion = self.combobox.get()
        if seleccion == "Curso":
            info = self.curso.mostrar_info()
        elif seleccion == "Profesor":
            info = self.profesor.mostrar_info()
        elif seleccion == "Estudiante":
            info = self.estudiante.mostrar_info()
        elif seleccion == "Asignatura":
            info = self.asignatura.mostrar_info()
        elif seleccion == "Evaluación":
            info = self.evaluacion.mostrar_info()
        else:
            info = "Selecciona un tipo de información"
        self.info_text.delete("1.0", tk.END)
        self.info_text.insert(tk.END, info)

root = tk.Tk()
app = InformacionGUI(root)
root.mainloop()


