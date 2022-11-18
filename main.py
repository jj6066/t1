import socket
import threading


def open_server(bind_ip, bind_port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((bind_ip, bind_port))
    server.listen(5)

    print(f"[*] Listening on {bind_ip}:{bind_port}")

    while True:
        conn, addr = server.accept()
        print(f"Connected by {addr}")

        while True:
            data = conn.recv(1024).decode("utf-8").strip()
            print(f"Client send data: {data}")

            if data == "bye":
                conn.close()
                break
            reply = "hello, " + data
            conn.send(reply.encode())

        break

    server.close()

def open_math_server(bind_ip, bind_port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((bind_ip, bind_port))
    server.listen(5)

    print(f"[*] Listening on {bind_ip}:{bind_port}")

    while True:
        conn, addr = server.accept()
        print(f"Connected by {addr}")

        while True:
            data = conn.recv(1024).decode("utf-8").strip()
            print(f"Client send data: {data}")

            if data == "bye":
                conn.close()
                break
            reply = "hello, " + data
            conn.send(reply.encode())

        break

    server.close()


if __name__ =='__main__':
    ip = "127.0.0.1"
    port = 8133
    math_port = 8233
    threading.Thread(openserver, )
    open_server(ip, port)
