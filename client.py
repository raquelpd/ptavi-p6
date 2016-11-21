#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys

# Cliente UDP simple.

# Dirección IP del servidor.
if len(sys.argv) !=3:
    sys.exit('Usage: Python clientpy method receiver@IP:SIPport')

METHOD = sys.argv[1]
USER = sys.argv[2]
LOGIN = USER.split('@')[0]
IP = USER.split(':')[0].split('@')[1]
PORT = int(USER.split(':')[1])

# Contenido que vamos a enviar
Line_SIP = 'SIP:' + LOGIN + IP + 'SIP/2.0\r\n'
LINE = METHOD + Line_SIP

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((IP, PORT))

print("Enviando: " + LINE)
my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
data = my_socket.recv(1024)

print('Recibido -- ', data.decode('utf-8'))
print("Terminando socket...")

#if METHOD == 'INVITE' :
    

# Cerramos todo
my_socket.close()
print("Fin.")
