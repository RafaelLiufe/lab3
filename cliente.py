import socket
import threading

HOST = '127.0.0.1'
PORT = 55555

def rec(c):
    while True:
        try:
            msg = c.recv(1024).decode('utf-8')
            if not msg:
                break
            print(f"\r{msg}\nVocê: ", end="", flush=True)
        except:
            print("\n[!] Desconectado do servidor.")
            break

def init():
    apelido = input("Escolha seu apelido: ")
    
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect((HOST, PORT))

    esc = threading.Thread(target=rec, args=(c,), daemon=True)
    esc.start()

    print("Conectado! Digite suas mensagens (ou 'sair' para encerrar).")
    while True:
        try:
            tex = input("Você: ")
            if tex.lower() == 'sair':
                break
            if tex.strip():
                msg = f"[{apelido}]: {tex}"
                c.send(msg.encode('utf-8'))
        except (KeyboardInterrupt, EOFError):
            break

    c.close()

if __name__ == "__main__":
    init()