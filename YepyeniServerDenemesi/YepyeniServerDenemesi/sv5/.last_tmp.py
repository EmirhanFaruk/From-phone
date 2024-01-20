import socket
import threading
import sys


class Server:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connections = []
    def __init__(self):
        self.sock.bind(('', 10422))#('0.0.0.0', 10422))
        self.sock.listen()
        print("Bağlantı bekleniyor...")
        
    def handler(self, c, a):
        while True:
            data = c.recv(1024)
            for connection in self.connections:
                connection.send(bytes(data))
            if not data:
                print(str(a[0]) + ':' + str(a[1]) + " bağlantısını kesti.")
                connections.remove(c)
                c.close()
                break

    def run(self):
        while True:
            c, a = self.sock.accept()
            cThread = threading.Thread(target=self.handler, args=(c, a))
            cThread.daemon = True
            cThread.start()
            self.connections.append(c)
            print(str(a[0]) + ':' + str(a[1]) + " bağlandı.")

class Client:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def sendMsg(self):
		while True:
			self.sock.send(bytes(str(self.isim + ": " + input("\r")), 'utf-8'))
			#print("\r")
	def __init__(self, adress):
		self.isim = input("İsminizi giriniz: ")
		host = socket.gethostbyname("localhost")
		print(f"{host}'a bağlanılıyor...")
		self.sock.connect((host, 10422))
		print("Bağlantı kuruldu.")
        #self.sock.connect((adress, 10422))

		iThread = threading.Thread(target=self.sendMsg)
		iThread.daemon = True
		iThread.start()
        
		while True:
			data = self.sock.recv(1024)
			if not data:
				break
			data = str(data, 'utf-8')
			#if data.startswith(self.isim + ": "):
			print(data)


if True:#len(sys.argv) > 1:
    client = Client("192.0.0.4")#sys.argv[1])
else:
    server = Server()
    server.run()