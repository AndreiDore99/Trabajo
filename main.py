from src.Conector import Conector

con = Conector()
con.connect()
con.create_database()
con.create_table_usuarios()
con.create_table_administradores()
con.create_admin_user("admin", "admin")
lista = con.select_all_admin()
print("Lista de administradores: ", lista)
for i in lista:
    print("Usuario: ", i[0])
    print("Contraseña: ", i[1])
    if i[0] == "admin":
        print("Usuario admin encontrado")
    else:
        print("Usuario admin no encontrado")
       

con.disconnect()