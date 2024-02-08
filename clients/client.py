import socket
import time

address = 'localhost'
port = 12000

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as cs:
    try:
        cs.connect((address, port))
        cs.settimeout(1)
        message = str(input("You: "))
        cs.send(message.encode())
    except:
        pass