class Administrador:
    def __init__(self,nombre_usuario,contrasena):
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
  
    def get_nombre_usuario(self):
        return str(self.nombre_usuario)
    
    def get_contrasena(self):
        return str(self.contrasena)
    
    def set_nombre_usuario(self, nombre_usuario):
        self.nombre_usuario = nombre_usuario
    
    def set_contrasena(self, contrasena):
        self.contrasena = contrasena
    
    
        
    def __str__(self):
        return f"Administrador(nombre_usuario={self.nombre_usuario}, contrasena={self.contrasena})"
    
