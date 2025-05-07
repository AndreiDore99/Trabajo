import mysql.connector
import src.Propiedades as propiedades
from mysql.connector import Error
from src.Administrador import Administrador
from print_color import print



# Configuración de la conexión
class Conector:
    def __init__(self):
        self.host = propiedades.DB_HOST
        self.user = propiedades.DB_USER
        self.password = propiedades.DB_PASSWORD
        self.database = propiedades.DB_NAME

# Establecer la conexión
    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            check_connection = self.connection.cursor()

            if self.connection.is_connected():
                print("Conexión exitosa a la base de datos.",tag='success', tag_color='green', color='white')
        except Error as e:
            print(f"Error al conectar a MySQL: {e}",tag='failure', tag_color='red', color='magenta')
            self.connection = None

    def disconnect(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Conexión cerrada.",tag='success', tag_color='green', color='white')
    
    def create_database(self):
        try:
            temp_connection = mysql.connector.connect(host=self.host,user=self.user,password=self.password)
            cursor = temp_connection.cursor()
            cursor.execute(propiedades.CREACION_BBDD)
            cursor.close()
            temp_connection.close()
           
            print(f"Base de datos '{propiedades.DB_NAME}' creada con éxito.",tag='success', tag_color='green', color='white')
        except Error as e:
            print(f"Error al crear la base de datos: {e}",tag='failure', tag_color='red', color='magenta')
        finally:
            cursor.close()

    def create_table_usuarios(self):
        try:
            temp_connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password
            )
            cursor = temp_connection.cursor()
            cursor.execute(propiedades.CREACION_TABLA_USUARIOS)
            cursor.close()
            temp_connection.close()
            print(f"Tabla 'usuarios' creada con éxito en la base de datos '{propiedades.DB_NAME}'.",tag='success', tag_color='green', color='white')
        except Error as e:
            print(f"Error al crear la tabla: {e}",tag='failure', tag_color='red', color='magenta')
            
    def create_table_administradores(self):
        try:
            temp_connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password
            )
            cursor = temp_connection.cursor()
            cursor.execute(propiedades.CREACION_TABLA_ADMINISTRADORES)
            cursor.close()
            temp_connection.close()
            print(f"Tabla 'administradores' creada con éxito en la base de datos '{propiedades.DB_NAME}'.",tag='success', tag_color='green', color='white')
        except Error as e:
            print(f"Error al crear la tabla: {e}",tag='failure', tag_color='red', color='magenta')

    def create_admin_user(self, Administrador):
        try:
            cursor = self.connection.cursor()            
            sql = propiedades.CREACION_ADMIN
            val = (Administrador.get_nombre_usuario(), Administrador.get_contrasena())
            cursor.execute(sql, val)
            self.connection.commit()
            print(f"Administrador creado con éxito.",tag='success', tag_color='green', color='white')
        except Error as e:
            print(f"Error al crear el administrador: {e}",tag='Warning', tag_color='yellow', color='magenta')
            cursor.close()
   
    def select_all_admin(self):
        try:
            temp_connection = mysql.connector.connect(host=propiedades.DB_HOST,user=propiedades.DB_USER,password=propiedades.DB_PASSWORD,database=propiedades.DB_NAME)
            cursor = temp_connection.cursor()
            cursor.execute(propiedades.CONSULTA_TODOS_ADMINISTRADORES)
            resultados = cursor.fetchall()
            print("Resultados de la consulta:")
            print(f"ID: {resultados[0][0]}, Nombre de usuario: {resultados[0][1]}, Contraseña: {resultados[0][2]}",tag='success', tag_color='green', color='white')
            cursor.close()
            temp_connection.close()
            return resultados
        except mysql.connector.Error as e:
            print(f"Error de base de datos: {e}")
        
    def check_connection(self):
        if self.connection:
            cursor = self.connection.cursor()
            print("Conectando.....",tag='success', tag_color='green', color='white')
            cursor.close()
        else:
            print("La conexión a la base de datos falló.",tag='failure', tag_color='red', color='magenta')

    def start(self):
        self.connect()
        self.create_database()
        self.create_table_usuarios()
        self.create_table_administradores()  # Import the Administrador class
        admin = Administrador("admin", "admin")
        self.create_admin_user(admin)
        
    
    