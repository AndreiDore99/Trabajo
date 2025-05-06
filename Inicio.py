import tkinter as tk
from tkinter import ttk
from tkinter import messagebox,Label,PhotoImage
from src.Conector import Conector

import tkinter as tk
from tkinter import messagebox
from src.Administrador import Administrador


def init_app():
        con = Conector()
        con.start()

if __name__ == "__main__":
    init_app()


def loging():
    
    administrador = Administrador(entry_usuario.get(), entry_contrasena.get())
    #AQUI TENGO QUE HACER LA COMPROBACION DE QUE EL USUARIO EXISTE EN LA BASE DE DATOS Y QUE LA CONTRASEÑA SEA CORRECTA
    con = Conector()
    administradores = con.select_all_admin()

    for i in administradores:
        print("Variable usuario: ", administrador.get_nombre_usuario())
        print("Variable admin: ", administradores[0][1])

        if administrador.get_nombre_usuario() == administradores[0][1] and administrador.get_contrasena() == administradores[0][2]:
            messagebox.showinfo("Inicio de Sesión", "Inicio de sesión exitoso")
            return
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")
            return
# Crear ventana
ventana = tk.Tk()
ventana.title("Inicio de Sesión")
ventana.geometry("300x200")
ventana.configure(bg="#F9F7F7")
imagen = PhotoImage(file="src/img/logo_sek.png")
label = tk.Label(ventana, image=imagen)
label.pack()


# Etiqueta y campo de texto para usuario
tk.Label(ventana, text="Usuario:").pack(pady=5)
entry_usuario = tk.Entry(ventana)
entry_usuario.pack()

# Etiqueta y campo de texto para contraseña
tk.Label(ventana, text="Contraseña:").pack(pady=5)
entry_contrasena = tk.Entry(ventana, show="*")
entry_contrasena.pack()

# Botón para guardar
btn_guardar = tk.Button(ventana, text="Entrar", command=loging)
btn_guardar.pack(pady=10)

ventana.mainloop()

