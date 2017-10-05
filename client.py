#!/usr/bin/env python

import socket

IP_SERV = "192.168.0.224"
PORT = 28564

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print 'connexion reussi avec le serveur'

sock.sendto("Salut",(IP_SERV,PORT))

print 'Message envoyer'

