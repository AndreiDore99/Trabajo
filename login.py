import tkinter as tk
import src.Propiedades as Propiedades
from tkinter import messagebox, Label, PhotoImage
from src.Conector import Conector
from src.Administrador import Administrador
import menu as menu

AppLogin = tk.Tk()
class LoginApp:
    
    def __init__(self):
       
        AppLogin.title(Propiedades.VENTANA_LOGIN_TITULO)
        AppLogin.configure(bg=Propiedades.COLOR_VENTANA_FONDO)
        imagen = PhotoImage(file=Propiedades.IMAGEN_LOGO)
        logo = tk.Label(AppLogin, image=imagen)
        logo.pack()

        #Etiqueta y campo de texto para usuario
        tk.Label(AppLogin, text="Usuario:").pack(pady=5)
        self.entry_usuario = tk.Entry(AppLogin)
        self.entry_usuario.pack()

        # Etiqueta y campo de texto para contraseña
        tk.Label(AppLogin, text="Contraseña:").pack(pady=5)
        self.entry_contrasena = tk.Entry(AppLogin, show="*")
        self.entry_contrasena.pack()

        # Botón para guardar
        btn_guardar = tk.Button(AppLogin, text="Iniciar Sesión", command=self.loging)
        btn_guardar.pack(pady=10)
        
        AppLogin.mainloop()
        

    def loging(self):
        Adm = Administrador(self.entry_usuario.get(), self.entry_contrasena.get())
        print("Usuario: ", Adm.get_nombre_usuario())
        print("Contraseña: ", Adm.get_contrasena())
        if len(Adm.get_nombre_usuario().strip())==0 or len(Adm.get_contrasena().strip())==0:
            messagebox.showinfo("Error","Error: No se puede tener campos vacíos.")
            raise TypeError("Error: No se puede tener campos vacíos.")
        con = Conector()
        administradores = con.select_all_admin()
        for i in administradores:
            print("Variable usuario: ", Adm.get_nombre_usuario())
            print("Variable admin: ", administradores[0][1])

            if Adm.get_nombre_usuario() == administradores[0][1] and Adm.get_contrasena() == administradores[0][2]:
                messagebox.showinfo("Inicio de Sesión", "Inicio de sesión exitoso")
                # Aqui tedria que abrir la ventana de administrador
                AppLogin.destroy()
                accesomenu = menu.MenuApp()          
                return accesomenu
            else:
                messagebox.showerror("Error", "Usuario o contraseña incorrectos")
                return
            
    def salir(self):
        # Lógica para salir de la aplicación
        messagebox.showinfo("SALIENDO")
        self.loging.destroy()