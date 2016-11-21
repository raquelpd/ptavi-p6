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
        self.wfile.write(b"Hemos recibido tu peticion")
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read()
            print("El cliente nos manda " + line.decode('utf-8'))

            # Si no hay más líneas salimos del bucle infinito
            if not line:
                break

if __name__ == "__main__":

    if len(sys.argv) !=4:
        sys.exit('Usage: python server.py IP Port audio_file')

    IP = sys.argv[1]
    PORT = sys.argv[2]
    FICH = sys.argv[3]

    if not os.path.exists(FICH):
        sys.exit('Usage: audio file does nt exist')

    print('listening...')

    # Creamos servidor de eco y escuchamos
    serv = SocketServer.UDPServer(('', 6001), EchoHandler)
    print("Lanzando servidor UDP de eco...")
    serv.serve_forever()
