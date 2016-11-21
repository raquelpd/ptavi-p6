#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys

# Cliente UDP simple.

# Dirección IP del servidor.
if len(sys.argv) != 3:
    sys.exit('Usage: Python clientpy method receiver@IP:SIPport')

METHOD = sys.argv[1]
USER = sys.argv[2]
LOGIN = USER.split('@')[0] + '@'
IP = USER.split(':')[0].split('@')[1]
PORT = int(USER.split(':')[1])

if METHOD not in ['INVITE', 'BYE']:
    sys.exit('Usage: python client.py method (INVITE/BYE) receiver@IP:SIPport')
else:
    # Contenido que vamos a enviar
    Line_SIP = ' sip:' + LOGIN + IP + ' SIP/2.0\r\n'
    LINE = METHOD + Line_SIP

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((IP, PORT))

print("Enviando: " + LINE)
my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')

try:
    data = my_socket.recv(1024)
except ConnectionRefusedError:
    sys.exit('Conection Refused')

print('Recibido -- ', data.decode('utf-8'))
if METHOD == 'INVITE':
    I1 = data.decode('utf-8').split()[5]
    I2 = data.decode('utf-8').split()[8]
    I3 = data.decode('utf8').split()[11]
    if I1 == '100' and I2 == '180' and I3 == '200':
        Line = 'ACK ' + 'sip:' + LOGIN + 'SIT/2.0'
        print('Sending: ' + Line)
        my_socket.send(bytes(Line, 'utf-8') + b'\r\n')
        data = my_socket.recv(1024)


print("Terminando socket...")


# Cerramos todo
my_socket.close()
print("Fin.")
