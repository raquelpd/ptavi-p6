#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import SocketServer
import sys
import os.path
import os


class EchoHandler(SocketServer.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        # Escribe dirección y puerto del cliente (de tupla client_address)
        self.wfile.write(b"Hemos recibido tu peticion" + b'\r\n\r\n')
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read()
            # Si no hay más líneas salimos del bucle infinito
            if not line:
                break

            print("El cliente nos manda " + line.decode('utf-8'))
            METHOD = line.decode('utf-8').split(' ')[0]
            if METHOD == 'INVITE':
                self.wfile.write(b"SIP/2.0 100 Trying" + b"\r\n")
                self.wfile.write(b"SIP/2.0 180 Ring" + b"\r\n")
                self.wfile.write(b"SIP/2.0 200 OK" + b"\r\n")
            elif METHOD == 'BYE':
                self.wfile.write(b"SIP/2.0 200 OK" + b"\r\n")
            elif METHOD not in ['INVITE', 'ACK', 'BYE']:
                self.wfile.write(b"SIP/2.0 405 METHOD Not Allowed" + b"\r\n")
            elif METHOD == 'ACK':
                # aEjecutar es un string con lo que se ha de ejecutar en la shell
                aEjecutar = './mp32rtp -i 127.0.0.1 -p 23032 < ' + FICH
                print("Vamos a ejecutar" + aEjecutar)
                os.system(aEjecutar)
            else:
                self.wfile.write(b"SIP/2.0 400 Bad Request" + b"\r\n\r\n")

if __name__ == "__main__":

    if len(sys.argv) != 4:
        sys.exit('Usage: python server.py IP Port audio_file')

    IP = sys.argv[1]
    PORT = int(sys.argv[2])
    FICH = sys.argv[3]

    if not os.path.exists(FICH):
        sys.exit('Usage: audio file does not exist')

    # Creamos servidor de eco y escuchamos
    serv = SocketServer.UDPServer(('', PORT), EchoHandler)

    print('listening...')
    serv.serve_forever()
