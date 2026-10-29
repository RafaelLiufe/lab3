import socket
import threading

HOST = '127.0.0.1'
PORT = 55555

clientes = []

def broadcast(msg, r):
    for c in clientes[:]:
        if c != r:
            try:
                c.send(msg)
            except:
                clientes.remove(c)

def g(c, addr):
    print(f"[+] {addr} entrou no chat.")
    while True:
        try:
            msg = c.recv(1024)
            if not msg:
                break
            broadcast(msg, c)
        except:
            break

    if c in clientes:
        clientes.remove(c)
    c.close()
    print(f"[-] {addr} saiu do chat.")

def init():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[*] Servidor escutando em {HOST}:{PORT}")

    while True:
        c, endereco = server.accept()
        clientes.append(c)
        thread = threading.Thread(target=g, args=(c, endereco), daemon=True)
        thread.start()

if __name__ == "__main__":
    init()