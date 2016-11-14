#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys

# Cliente UDP simple.

# Dirección IP del servidor.
SERVER = 'localhost'
METHOD= sys.argv[1]
DIR = sys.argv[2]
LOGIN = DIR.split('@')[0]
IP = DIR.split(':')[0].split('@')[1]
PORT = int(DIR.split(':')[1])
# Contenido que vamos a enviar



if (not '@' or ':' in LOGIN) or (len(sys.argv) != 3):
    sys.exit('Usage: python client.py method receiver@IP:SIPport')


LINE = '¡Hola mundo!'

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((SERVER, PORT))

print("Enviando: " + LINE)
my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
data = my_socket.recv(1024)

instruction = data.decode('utf-8')
print('Recibido --', instruction)

## if METHOD = "INVITE" :
    
    
    
    
    

print("Terminando socket...")

# Cerramos todo
my_socket.close()
print("Fin.")
