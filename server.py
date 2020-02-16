import socket
import argparse

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '192.168.1.36'
port = 1235
print(host, port)
s.bind((host, port))

s.listen(5)
H = 10

def send(s, msg):
    header = str(len(msg)).ljust(H)
    body = header + msg
    print(body)
    b = bytes(body)
    s.send(b)


parser = argparse.ArgumentParser()
parser.add_argument('--file')
args = parser.parse_args()


while True:
    client, addr = s.accept()
    print(client,addr)
    send(client, open(args.file).read())
    client.close()
