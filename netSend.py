import socket

host, port = "127.0.0.1", 25001
data = "si test"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect((host, port))
    sock.sendall(data.encode("utf-8"))
    data = sock.recv(1024).decode("utf-8")
    print(data)

finally:
    sock.close()
