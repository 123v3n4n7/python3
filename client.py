#!/usr/bin/env python3

import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('localhost', 8007))
hello = bytes('hello', 'utf-8')
s.send(hello)
data = s.recv(100000)
print('redieved', data, len(data), 'bytes')
s.close()