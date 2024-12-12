import mysql.connector

# Configuración de la base de datos
db_config = {
    'host': 'localhost',
    'user': 'root',  # Cambia por tu usuario de MySQL
    'password': 'BY24asod_',  # Cambia por tu contraseña
    'database': 'secure_db'
}

# Conexión a la base de datos
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

# Entrada simulada del usuario
username = input("Introduce tu usuario: ")
password = input("Introduce tu contraseña: ")

# Consulta vulnerable
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}';"
print(f"Ejecutando consulta: {query}")

cursor.execute(query)
results = cursor.fetchall()

# Mostrar los resultados
if results:
    print("Usuario encontrado:")
    for row in results:
        print(row)
else:
    print("No se encontraron resultados.")

cursor.close()
connection.close()