#!/usr/bin/env python3
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 8007
s.bind((host, port))
s.listen(1)
conn, addr = s.accept()
data = conn.recv(100000)
conn.send(data)
print('client is an', addr, data)
conn.close()