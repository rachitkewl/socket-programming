import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.1.36'
port = 1235
s.connect((host, port))
H = 10

def recv(s):
    full_msg = b''
    header = s.recv(H)
    msg_len = int(header)
    full_msg = header
    while len(full_msg) != msg_len+H:
        full_msg += s.recv(16)
    res = full_msg[H:].decode('UTF-8')
    print(res)
    return res

print(recv(s))
