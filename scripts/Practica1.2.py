#Practica1.2 Crear un programa que sugiera una contraseña segura 
import random
import string

def generar_contrasena():
    # Definir los caracteres que se pueden usar
    mayusculas = string.ascii_uppercase
    minusculas = string.ascii_lowercase
    numeros = string.digits
    caracteres_especiales = "!@#$%^&*()-_=+[]{}|;:'\",.<>/?~`"
    
    # Asegurar que la contraseña cumpla con los requisitos mínimos
    while True:
        contrasena = []
        contrasena.append(random.choice(mayusculas))
        contrasena.append(random.choice(minusculas))
        contrasena.append(random.choice(numeros))
        contrasena.append(random.choice(caracteres_especiales))
        
        # Rellenar el resto de la contraseña con caracteres aleatorios
        todos_caracteres = mayusculas + minusculas + numeros + caracteres_especiales
        contrasena += [random.choice(todos_caracteres) for _ in range(4, random.randint(8, 12))]
        
        # Verificar que la contraseña no contenga más de 2 caracteres iguales consecutivos
        if any(contrasena[i] == contrasena[i+1] == contrasena[i+2] for i in range(len(contrasena)-2)):
            continue
        
        # Verificar que no haya espacios en blanco
        contrasena_final = ''.join(contrasena)
        if " " in contrasena_final:
            continue

        # Suficiente longitud y cumple los criterios
        if len(contrasena_final) >= 8:
            return contrasena_final

# Ejemplo de uso
contrasena_segura = generar_contrasena()
print("Contraseña segura generada:", contrasena_segura)
