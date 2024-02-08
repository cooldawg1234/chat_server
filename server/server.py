import socket

host = ''
port = 12000
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
	try:
		s.bind((host, port))
		s.listen(2)
		addies = set()
		print("Serving up ")
		while 1:
			a = s.accept()
			if a:
				addies.add(a[0])

				
	except Exception as e:
		pass
