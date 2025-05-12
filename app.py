import tkinter as tk
import login as login

class App:
    def __init__(self):
        AppLogin = tk.Tk()
    
    def start(self):
        AppLogin = login.LoginApp()
        AppLogin.mainloop()

