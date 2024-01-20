import socket
import threading
import sys


class Kullanıcı:
    def __init__(self, a, cevaplar = []):
        self.a, self.cevaplar = a, cevaplar
    

class Server:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connections = []
    kullanıcılar = []
    port_listesi = []
    def __init__(self):
        self.sock.bind(('', 10422))#('0.0.0.0', 10422))
        self.sock.listen()
        print("Bağlantı bekleniyor...")
        
    def handler(self, c, a):
        while True:
            data = c.recv(1024)
            #print(c, a)
            kullanıcı_adı = str(data, 'utf-8').split(": ")[0]
            mesaj = str(data, 'utf-8').split(": ")[1]
            if not(a[1] in self.port_listesi):
                self.kullanıcılar.append([kullanıcı_adı, c, a])
                self.port_listesi.append(a[1])
            print(self.kullanıcılar)
            print(self.port_listesi)
            for connection in self.connections:
                connection.send(bytes(data))
            if not data:
                
                print(str(a[0]) + ':' + str(a[1]) + " bağlantısını kesti.")
                for i in range(len(port_listesi)):
                	if a[1] == port_listesi[i]:
                		port_listesi.pop(i)
                		kullanıcılar.pop(i)
                		break
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
			self.sock.send(bytes(input(""), 'utf-8'))
	def __init__(self, adress):
		host = socket.gethostbyname("localhost")
		print(f"{host}'a bağlanılıyor...")
		self.sock.connect((host, 10422))
        #self.sock.connect((adress, 10422))

		iThread = threading.Thread(target=self.sendMsg)
		iThread.daemon = True
		iThread.start()
        
		while True:
			data = self.sock.recv(1024)
			if not data:
				break
			print(str(data, 'utf-8'))


if False:#len(sys.argv) > 1:
    client = Client("192.0.0.4")#sys.argv[1])
else:
    server = Server()
    server.run()
