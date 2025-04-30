import mysql.connector
from mysql.connector import Error
import Propiedades as propiedades
from print_color import print
# Configuración de la conexión
class Conector:
    def __init__(self):
        self.host = propiedades.DB_HOST
        self.user = propiedades.DB_USER
        self.password = propiedades.DB_PASSWORD
        self.database = propiedades.DB_NAME
        self.connection = None

# Establecer la conexión
    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
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
            temp_connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password
            )
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
