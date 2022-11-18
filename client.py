import socket

HOST = "127.0.0.1"
PORT = 8133

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

attempt = 2
while True:
    cmd = input("Please input msg: ")
    if cmd == 'bye':
        s.send("bye".encode("utf-8"))
        s.close()
        break
    s.send(cmd.encode("utf-8"))        
    data = s.recv(1024).decode()
    print(f"server reply: {data}")

