class Usuario:
    def __init__(self, id,nick,nombre,correo,departamento):
        self.id = id
        self.nick = nick
        self.nombre = nombre
        self.correo = correo
        self.departamento = departamento

    def get_id(self):
        return self.id
    
    def get_nick(self):
        return self.nick
    
    def get_nombre(self):
        return self.nombre
    
    def get_correo(self):
        return self.correo
    
    def get_departamento(self): 
        return self.departamento
    
    def set_id(self, id):
        self.id = id
    
    def set_nick(self, nick):
        self.nick = nick
    
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def set_correo(self, correo):
        self.correo = correo
    
    def set_departamento(self, departamento):
        self.departamento = departamento
    
    
    def __str__(self):
        return f"Usuario(id={self.id}, nick={self.nick}, nombre={self.nombre}, correo={self.correo}, departamento={self.departamento})"
