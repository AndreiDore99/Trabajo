from Conector import Conector

con = Conector()
con.connect()
con.create_database()
con.create_table_usuarios()
con.create_table_administradores()

con.disconnect()