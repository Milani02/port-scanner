import socket
import sys
from datetime import datetime


target = input("Digite o IP alvo para escanear: ")

print("-" * 50)
print(f"Escaneando alvo: {target}")
print(f"Iniciado em: {str(datetime.now())}")
print("-" * 50)

try:
    for port in range(1, 100): 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1) 
        result = s.connect_ex((target, port)) 
        if result == 0:
            print(f"Porta {port}: ABERTA")
        s.close()

except KeyboardInterrupt:
    print("\nSaindo do programa.")
    sys.exit()
except socket.gaierror:
    print("Hostname não pôde ser resolvido.")
    sys.exit()
except socket.error:
    print("Não foi possível conectar ao servidor.")
    sys.exit()