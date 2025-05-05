import tkinter as tk
from tkinter import ttk
from tkinter import messagebox,Label
from src.Conector import Conector

import tkinter as tk
from tkinter import messagebox

def loging():
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()
    print("Variable usuario: ", usuario)
    print("Variable admin: ", administradores[i])
    #AQUI TENGO QUE HACER LA COMPROBACION DE QUE EL USUARIO EXISTE EN LA BASE DE DATOS Y QUE LA CONTRASEÑA SEA CORRECTA
    con = Conector()
    administradores = con.select_all_admin()

    for i in administradores:
        if administradores[i] == usuario:
            print("Variable usuario: ", usuario,color='green')
            print("Variable admin: ", i[0])
            print("Variable contraseña: ", contrasena,color='green')
            print("Variable contraseña admin: ", i[1])
            messagebox.showinfo("Inicio de Sesión", "Inicio de sesión exitoso")
            return
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")
            return
# Crear ventana
ventana = tk.Tk()
ventana.title("Inicio de Sesión")
ventana.geometry("300x180")

# Etiqueta y campo de texto para usuario
tk.Label(ventana, text="Usuario:").pack(pady=5)
entry_usuario = tk.Entry(ventana)
entry_usuario.pack()

# Etiqueta y campo de texto para contraseña
tk.Label(ventana, text="Contraseña:").pack(pady=5)
entry_contrasena = tk.Entry(ventana, show="*")
entry_contrasena.pack()

# Botón para guardar
btn_guardar = tk.Button(ventana, text="Guardar", command=loging)
btn_guardar.pack(pady=10)

ventana.mainloop()
