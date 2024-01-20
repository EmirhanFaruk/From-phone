import pygame
from network import Network
import threading


class Player():
	width = height = 50

	def __init__(self, id, startx, starty, color=(255,0,0)):
		self.x = startx
		self.y = starty
		self.velocity = 2
		self.color = color
		self.yon_data = "0000"
		self.id = id

	def draw(self, g, canvas):
		print(f"Çizmeye çalışıyorum, benim id no {self.id}")
		pygame.draw.rect(g, self.color ,(self.x - self.width/2, self.y - self.height/2, self.width, self.height), 0)
		canvas.draw_text(str(self.id), 30, self.x, self.y)
		pygame.display.update()


class Game:
	
	
	def __init__(self, w, h):
		self.net = Network()
		print("self net elde edildi")
		self.width = w
		self.height = h
		self.oyuncular = [Player(self.net.id, 50, 50, (20, 200, 20))]
		self.canvas = Canvas(self.width, self.height, "Testing...")
	
	def id_listesi(self, veriler):
		liste = []
		for veri in veriler:
			liste.append(veri.split(":")[0])
		return liste
		
	def veri_işle(self, oyuncu, veri):
		veri = veri.split(":")[1].split(",")
		oyuncu.x = int(veri[0])
		oyuncu.y = int(veri[1])
		return oyuncu
	
	def veri_oyuncu_eşitliği(self, veriler, oyuncular):
		if len(oyuncular) < len(veriler):
			for veri in veriler:
				listede = False
				for oyuncu in oyuncular:
					if veri.split(":")[0] == oyuncu.id:
						listede = True
						break
				if not(listede):
					x, y = veri.split(":")[1].split(",")[0], veri.split(":")[1].split(",")[1]
					oyuncular.append(Player(veri.split(":")[0], x, y))
		if len(oyuncular) > len(veriler):
			for oyuncu in oyuncular:
				listede = False
				for veri in veriler:
					if veri.split(":")[0] == oyuncu.id:
						listede = True
						break
				if not(listede):
					oyuncular.remove(oyuncu)
					continue
		return veriler, oyuncular
	
	def oyuncuları_çiz(self, veriler, oyuncular):
		# Update Canvas
		self.canvas.draw_background()
		for index in range(len(veriler)):
			for oyuncu_index in range(len(oyuncular)):
				print(f"{oyuncular[oyuncu_index].id} == {index}")
				if int(oyuncular[oyuncu_index].id) == int(index):
					print(f"ifin içindeyim, veri: {veriler[index]}")
					oyuncular[oyuncu_index] = self.veri_işle(oyuncular[oyuncu_index], veriler[index])
					oyuncular[oyuncu_index].draw(self.canvas.get_canvas(), self.canvas)
					break
		if "[WinError 10054]" in veriler[0]:
			self.canvas.draw_text("Bağlantı sorunu", 30, 20, 20)
			try:
				self.net = Network()
			except Exception as e:
				print(e)
		self.canvas.update()
		pygame.display.update()
		return veriler, oyuncular
	
	def oyuncu_hareket_verisi(self, tuşlar, oyuncular):
		for index in range(len(oyuncular)):
			if oyuncular[index].id == self.net.id:
				oyuncular[index].yon_data = list(oyuncular[index].yon_data)
				if tuşlar[pygame.K_RIGHT]:
					oyuncular[index].yon_data[0] = "1"
				else:
					oyuncular[index].yon_data[0] = "0"

				if tuşlar[pygame.K_LEFT]:
					oyuncular[index].yon_data[1] = "1"
				else:
					oyuncular[index].yon_data[1] = "0"
				
				if tuşlar[pygame.K_DOWN]:
					oyuncular[index].yon_data[2] = "1"
				else:
					oyuncular[index].yon_data[2] = "0"
					
				if tuşlar[pygame.K_UP]:
					oyuncular[index].yon_data[3] = "1"
				else:
					oyuncular[index].yon_data[3] = "0"
				#tuş girişlerini göndermek için string haline getir
				oyuncular[index].yon_data = "".join(oyuncular[index].yon_data)
				#tuş girişlerini gönder ve sunucudan verileri al
				veriler = self.parse_data(self.send_data(oyuncular[index]))#gönderilen: 1:100,100,0,0,0,0 | alınan: 1:100,100
				print(f"Alınan veri: {veriler}")
				break
			
		return veriler, oyuncular
	
	def run(self):
		print("run metodu çalıştırılıyor.")
		clock = pygame.time.Clock()
		run = True
		while run:
			print("Döngünün başı.")
			clock.tick(60)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False

				if event.type == pygame.K_ESCAPE:
					run = False
			
			print("Üçlü fonksiyonun başı.")
			#tuş girişlerini al ve gönder
			veriler, self.oyuncular = self.oyuncu_hareket_verisi(pygame.key.get_pressed(), self.oyuncular)
			print(f"İlk fonksiyon oyuncu_hareket_verisi başarıyla çalıştırıldı. Elde edilenler: \n{veriler}")#, \n{self.oyuncular}")
			veriler, self.oyuncular = self.veri_oyuncu_eşitliği(veriler, self.oyuncular)
			print(f"İkinci fonksiyon veri_oyuncu_eşitliği başarıyla çalıştırıldı. Elde edilenler: \n{veriler}")#, \n{self.oyuncular}")
			veriler, self.oyuncular = self.oyuncuları_çiz(veriler, self.oyuncular)
			print(f"Üçüncü fonksiyon oyuncuları_çiz başarıyla çalıştırıldı. Elde edilenler: \n{veriler}")#, \n{self.oyuncular}")
			

		pygame.quit()

	def send_data(self, oyuncu):
		"""
		Send position to server
		:return: None
		"""
		data = str(self.net.id) + ":" + str(oyuncu.x) + "," + str(oyuncu.y) + "," + oyuncu.yon_data
		print(f"Gönderilen: {data}")
		reply = self.net.send(data)
		return reply

	@staticmethod
	def parse_data(data):
		try:
			return data
		except Exception as e:
			return e#[]


class Canvas:

	def __init__(self, w, h, name="None"):
		self.width = w
		self.height = h
		self.screen = pygame.display.set_mode((w,h))
		pygame.display.set_caption(name)

	@staticmethod
	def update():
		pygame.display.update()

	def draw_text(self, text, size, x, y):
		pygame.font.init()
		font = pygame.font.SysFont("comicsans", size)
		render = font.render(text, 1, (0,0,0))

		self.screen.blit(render, (x,y))

	def get_canvas(self):
		return self.screen

	def draw_background(self):
		self.screen.fill((30,70,255))


game = Game(500, 500)
game.run()