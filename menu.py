import tkinter as tk
import src.Propiedades as Propiedades
from tkinter import messagebox, Label, PhotoImage
from src.Conector import Conector
from src.Administrador import Administrador

class MenuApp:
    def __init__(self):
        Menu = tk.Tk()
        Menu.title(Propiedades.VENTANA_LOGIN_TITULO)
        Menu.configure(bg=Propiedades.COLOR_VENTANA_FONDO)
        tk.Button(Menu, text="Crear Usuario", command=self.crear_usuario).pack(pady=10)
        tk.Button(Menu, text="Eliminar Usuario", command=self.eliminar_usuario).pack(pady=10)
        tk.Button(Menu, text="Modificar Usuario", command=self.modificar_usuario).pack(pady=10)
        Menu.mainloop()

    def crear_usuario(self):
        # Lógica para crear un nuevo usuario
        messagebox.showinfo("CREANDO USUARIO")
    def eliminar_usuario(self):
        # Lógica para eliminar un usuario existente
        messagebox.showinfo("ELIMINANDO USUARIO")
    def modificar_usuario(self):
        # Lógica para modificar un usuario existente
        messagebox.showinfo("MODIFICANDO USUARIO")
