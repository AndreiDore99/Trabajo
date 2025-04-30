import mysql.connector
from mysql.connector import Error
import Propiedades as propiedades
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
                print("Conexión exitosa a la base de datos.")
        except Error as e:
            print(f"Error al conectar a MySQL: {e}")
            self.connection = None

    def disconnect(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Conexión cerrada.")
    
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
           
            print(f"Base de datos '{propiedades.DB_NAME}' creada con éxito.")
        except Error as e:
            print(f"Error al crear la base de datos: {e}")
        finally:
            cursor.close()