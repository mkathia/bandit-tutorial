# Web server binds to all interfaces
import socket

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 9090))  # Listens on all interfaces
    server.listen(5)
    print("Server listening on port 9090...")
    conn, addr = server.accept()
    print(f"Connection from {addr}")
    conn.send(b"Hello!\n")
    conn.close()

start_server()

