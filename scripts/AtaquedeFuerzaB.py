import sys
import time
import itertools
import string

def brute_force(user, target_password, limit):
    start = time.time()
    attempts = 0

    # Define el conjunto de caracteres para las contraseñas
    charset = string.ascii_letters + string.digits

    for length in range(1, len(target_password) + 1):
        for attempt in itertools.product(charset, repeat=length):
            attempts += 1
            guessed_password = ''.join(attempt)

            if guessed_password == target_password:
                end = time.time()
                print(f'Inició sesión como {user} con la contraseña {guessed_password}')
                print(f'Intentos fallidos: {attempts - 1}')
                print(f'Tiempo transcurrido: {end - start:.2f} segundos')
                print(f'Combinaciones intentadas: {attempts}')
                return

            if attempts >= limit:
                break

        if attempts >= limit:
            break

    end = time.time()
    print('No se pudo iniciar sesión')
    print(f'Intentos fallidos: {attempts}')
    print(f'Tiempo transcurrido: {end - start:.2f} segundos')
    print(f'Combinaciones intentadas: {attempts}')

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Uso: python brute_force.py <usuario> <contraseña> <intentos>')
        sys.exit(1)

    user = sys.argv[1]
    password = sys.argv[2]
    limit = int(sys.argv[3])

    brute_force(user, password, limit)
import sys
import time
import itertools
import string

def brute_force(user, target_password, limit):
    start = time.time()
    attempts = 0

    # Define el conjunto de caracteres para las contraseñas
    charset = string.ascii_letters + string.digits

    for length in range(1, len(target_password) + 1):
        for attempt in itertools.product(charset, repeat=length):
            attempts += 1
            guessed_password = ''.join(attempt)

            if guessed_password == target_password:
                end = time.time()
                print(f'Inició sesión como {user} con la contraseña {guessed_password}')
                print(f'Intentos fallidos: {attempts - 1}')
                print(f'Tiempo transcurrido: {end - start:.2f} segundos')
                print(f'Combinaciones intentadas: {attempts}')
                return

            if attempts >= limit:
                break

        if attempts >= limit:
            break

    end = time.time()
    print('No se pudo iniciar sesión')
    print(f'Intentos fallidos: {attempts}')
    print(f'Tiempo transcurrido: {end - start:.2f} segundos')
    print(f'Combinaciones intentadas: {attempts}')

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Uso: python brute_force.py <usuario> <contraseña> <intentos>')
        sys.exit(1)

    user = sys.argv[1]
    password = sys.argv[2]
    limit = int(sys.argv[3])

    brute_force(user, password, limit)
