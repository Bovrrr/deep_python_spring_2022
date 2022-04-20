import multiprocessing
import socket
import time


def server():
    sock = socket.socket()
    sock.bind(("", 15000))
    sock.listen(5)

    while True:
        client, addr = sock.accept()
        print("server: conn from", addr)

        data = client.recv(4096)
        print("server:", data)
        client.send(data.upper())
        break


def client():
    sock = socket.socket()
    sock.connect(("", 15000))
    sock.sendall(b"qwerty")
    data = sock.recv(1024)
    print("client:", data)


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=server)
    p2 = multiprocessing.Process(target=client)

    p1.start()
    time.sleep(1)
    p2.start()

    p1.join()
    p2.join()
