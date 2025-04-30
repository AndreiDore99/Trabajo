class Usuario:
    def __init__(self, id,nick,nombre,correo,departamento):
        self.id = id
        self.nick = nick
        self.nombre = nombre
        self.correo = correo
        self.departamento = departamento


    def __str__(self):
        return f"Usuario(id={self.id}, nick={self.nick}, nombre={self.nombre}, correo={self.correo}, departamento={self.departamento})"
