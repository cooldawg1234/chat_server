import socket
import time

address = 'localhost'
port = 12000

name = "Oumar"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cs:
    try:
        cs.connect((address, port))
        cs.send(f"{name}".encode())
        print("Connected to the server. CTRL + C to exit.")
        while True:
            try:
                message = str(input(f"{name}: "))
                cs.send(message.encode())
            except KeyboardInterrupt:
                break
    except:
        print("Connection Failed")
