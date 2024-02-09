import socket

host = ''
port = 12000
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.settimeout(1)
    print("Starting Chat Server")
    s.listen(2)
    addies = set()
    while True:
        try:
            connection, address = s.accept()
            print(f"{address} Connected.")
            addies.add(connection)
            message = connection.recv(2048)
            message = message.decode()
            print(f"{message} from {address}")
        except socket.timeout:
               continue
        except KeyboardInterrupt:
             break
        

