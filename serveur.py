#!/usr/bin/env python

import socket

IP_SERV = "192.168.0.224"
PORT = 28564

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((IP_SERV, PORT))

while True:
    data, address = sock.recvfrom(1024)
    print "Donnees recues", data


