import pandas as pd
import mysql.connector
from mysql.connector import Error

# Configuración de conexión a la base de datos
db_config = {
    'host': 'localhost',
    'user': 'root',       # Reemplaza con tu usuario de MySQL
    'password': 'BY24asod_',  # Reemplaza con tu contraseña de MySQL
    'database': 'secure_db'
}

# Leer archivo CSV
csv_file = 'customers-2000000.csv'  # Cambia esta ruta si el archivo está en otro lugar

try:
    # Leer el archivo CSV con pandas
    data = pd.read_csv(csv_file)
    
    # Verificar las primeras filas para asegurarse de que se lee correctamente
    print(data.head())

    # Conectar a la base de datos
    connection = mysql.connector.connect(**db_config)

    if connection.is_connected():
        cursor = connection.cursor()
        print("Conexión exitosa a la base de datos.")

        # SQL para insertar registros
        insert_query = """
        INSERT INTO customers (customer_id, first_name, last_name, subscription_date, website)
        VALUES (%s, %s, %s, %s, %s)
        """

        # Insertar cada fila en la tabla
        for index, row in data.iterrows():
            cursor.execute(insert_query, (
                row['customer_id'],
                row['first_name'],
                row['last_name'],
                row['subscription_date'],
                row['website']
            ))

            # Confirmar cada 1000 filas para mayor eficiencia
            if index % 1000 == 0:
                connection.commit()
                print(f"{index} registros insertados.")

        # Confirmar los registros restantes
        connection.commit()
        print("Inserción de datos completada.")
    
except FileNotFoundError:
    print(f"Error: No se encontró el archivo {csv_file}.")
except Error as e:
    print(f"Error al conectar con la base de datos: {e}")
except Exception as e:
    print(f"Se produjo un error: {e}")
finally:
    # Cerrar conexión
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexión cerrada.")