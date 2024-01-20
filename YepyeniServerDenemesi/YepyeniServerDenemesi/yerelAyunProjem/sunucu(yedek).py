import socket
import threading
import sys


class Server:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connections = []
	oyuncular = []
	veri_listesi = []
	anlık_id = "0"
	
	def __init__(self):
		try:
			self.sock.bind(('0.0.0.0', 5555))
			self.sock.listen()
		except socket.error as e:
			print(str(e))
			
		
	
	def id_listesi(self, veriler):
		liste = []
		for veri in veriler:
			liste.append(veri.split(":")[0])
		return liste
	
	
	def oyuncuyu_hareket_ettir(self, veri, vel):
		"""
		ham olarak veriyi ve ivmeyi alır, işler, ve işlenmiş olarak geri döndürür(sadece id:x,y)
		"""

		veri_poz = veri.split(":")[1].split(",")#0 x, 1 y, 2 sag, 3 sol, 4 asagı, 5 yukarı
		x, y = int(veri_poz[0]), int(veri_poz[1])
		veri_id = veri.split(":")[0]
		print("--------------------------")
		print("--------------------------")
		print(veri_poz)
		print(veri_id)
		print(str(veri_poz[2][0]) + str(veri_poz[2][1]) + str(veri_poz[2][2]) + str(veri_poz[2][3]))
		print(x, y)
		print("--------------------------")
		
		if str(veri_poz[2][0]) == "1":
			x += vel
		if str(veri_poz[2][1]) == "1":
			x -= vel
		if str(veri_poz[2][2]) == "1":
			y += vel
		if str(veri_poz[2][3]) == "1":
			y -= vel
		veri_id = veri_id + ":" + str(x) + "," + str(y)
		print(veri_id)
		print("--------------------------")
		print("--------------------------")
		return veri_id
				
	def handler(self, c, a):
		print("Gelen mesaj deneme değil, ama motoru başlatmak için elle zorlamak gerekecek.")
		for connection in self.connections:
			connection.send(str.encode(self.anlık_id))
		self.anlık_id = str(int(self.anlık_id) + 1)
		while True:
			print("\n\n\n========================================HERŞEYİN BAŞI========================================\n\n\n")
			data = c.recv(2048)#alınan: 1:100,100,0,0,0,0 | gönderilen: 1:100,100
			print(f"data alındı: {data}")
			if data:
				print("Oyuncular listesi:")
				for oyuncu in self.oyuncular:
					print(oyuncu)
				idler = self.id_listesi(self.oyuncular)
				print(data, type(data))
				data = data.decode('utf-8')
				print(data, type(data))
				data_list = data.split("|")
				temp = data
				del data
				print("döngüye giriliyor")
				for data in data_list:
					print(data)
					if not(data.split(":")[0] in idler):
						print("Görünüşe bakılırsa yeni data listede yok, ekleniyor...")
						geçici = []
						geçici.append(data.split(":")[0])
						geçici.append(":")
						geçici.append(data.split(":")[1].split(",")[0])
						geçici.append(data.split(":")[1].split(",")[1])
						self.oyuncular.append(geçici)
					print("Oyuncu hareket ettirilecek:")
					güncel_oyuncu = self.oyuncuyu_hareket_ettir(data, 3)
					print(f"Güncel oyuncu: {güncel_oyuncu}")
					o_idsi = güncel_oyuncu.split(":")[0]
					for i in range(len(self.oyuncular)):
						print(self.oyuncular[i])
						if self.oyuncular[i] == o_idsi:
							print("Oyuncu güncelleniyor:")
							print(self.oyuncular[i], güncel_oyuncu)
							self.oyuncular[i] = güncel_oyuncu
							print(self.oyuncular[i])
							break
							
							
				print("Gönderilecek veri oluşturuluyor...")
				gönderilecek_veri = ""
				for oyuncu_index in range(len(self.oyuncular)):
					gönderilecek_veri = gönderilecek_veri + self.oyuncular[oyuncu_index][0] + ":" + self.oyuncular[oyuncu_index][2] + "," + self.oyuncular[oyuncu_index][3] + "|"
					self.oyuncular[oyuncu_index] = "".join(self.oyuncular[oyuncu_index])
				gönderilecek_veri = gönderilecek_veri[:-1]
				print(f"Gönderilen veri: {gönderilecek_veri}")
				for connection in self.connections:
					connection.send(str.encode(gönderilecek_veri))
					
			else:
				print(str(a[0]) + ':' + str(a[1]) + " disconnected")
				self.connections.remove(c)
				c.close()
				break
				
				
	def run(self):
		while True:
			c, a = self.sock.accept()
			cThread = threading.Thread(target=self.handler, args=(c, a))
			cThread.daemon = True
			cThread.start()
			self.connections.append(c)
			print(str(a[0]) + ':' + str(a[1]) + " connected")


"""
if len(sys.argv) > 1:
	oyun = Game(500, 500, sys.argv[1])
	oyun.run()
else:
	adress = input("Bağlanılacak olan ip adresini giriniz(eğer sunucu olacaksanız boş bırakıp enter'a basın):")
	if adress != "":
		oyun = Game(500, 500, adress)
		oyun.run()
	else:
"""
server = Server()
server.run()
	
