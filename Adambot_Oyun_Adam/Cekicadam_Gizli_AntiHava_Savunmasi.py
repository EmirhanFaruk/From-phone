import pygame
from math import cos, sin, atan
from random import choice, randint, uniform
from mesafe import *
from Obje import *
from Anti_Hava_Mermisi import *


pygame.init()

pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize

mermi_sesi = pygame.mixer.Sound("mermi_ateşi_sesi_gerçek.mp3")#"pshot.wav")
mermi_sesi.set_volume(0.1)

class Cekicadam_Gizli_AntiHava_Savunmasi(Obje):
	def __init__(self, x, y, genislik, yukseklik, can, hasar, mermi_hizi, menzil):
        #Parametrelerden gelen değerleri objeye almak/işlemek
		super().__init__(x, y, genislik, yukseklik, can)#Obje class'ının init fonksiyonundan gerekli değişkenleri almak
		self.hasar = hasar
		self.mermi_hizi = mermi_hizi
		self.menzil = menzil
		self.ates_suresi_siniri = 15
		self.ates_suresi = self.ates_suresi_siniri
        #bir şarjör ve cehpane doldurma süresi olsun
        
        
		return
	
	def ates_et(self, hedefx, hedefy, hedefyukseklik, anti_hava_mermileri):
		if self.ates_suresi >= self.ates_suresi_siniri and hedefyukseklik > 1:
			hmes = mesafe((self.x + self.genislik/2, self.y + self.yukseklik/2), (hedefx, hedefy))#mesafeyi ilk aşamadan sonra bir değişkene koy ayrı bir yerde
			if hmes <= self.menzil:
				self.solb = True
				self.sagb = False
				self.ates_suresi = 0
				y_farki = hedefy - self.y
				x_farki = hedefx - self.x
				if x_farki == 0:
					mermi_x_orani = 0
					if y_farki > 0:
						mermi_y_orani = 1
					elif y_farki < 0:
						mermi_y_orani = -1
					else:
						mermi_y_orani = 0
						
				if y_farki == 0:
					mermi_y_orani = 0
					if x_farki > 0:
						mermi_x_orani = 1
					elif x_farki < 0:
						mermi_x_orani = -1
					else:
						mermi_x_orani = 0
						
				if not(x_farki == 0 or y_farki == 0):
					tanjant = atan(y_farki/x_farki)
					mermi_x_orani = sin(tanjant)
					mermi_y_orani = cos(tanjant)
					if hedefx < self.x:
						mermi_x_orani = -mermi_x_orani
						mermi_y_orani = -mermi_y_orani
				
				tanjant = atan(hedefyukseklik/hmes)
				mermi_z_orani = sin(tanjant)*2
				
				xhiz = mermi_x_orani * self.mermi_hizi
				yhiz = mermi_y_orani * self.mermi_hizi
				zhiz = mermi_z_orani * self.mermi_hizi
				sure = hmes/self.mermi_hizi
				anti_hava_mermileri.append(Anti_Hava_Mermisi(self.x, self.y, 10, 10, 0, 10, -1, 10, (yhiz, xhiz, zhiz), hedefyukseklik, sure))
				pygame.mixer.find_channel().play(mermi_sesi)
				return anti_hava_mermileri
			else:
				return anti_hava_mermileri
		else:
			self.ates_suresi += 1
			return anti_hava_mermileri
	def ana_ekrana_ciz(self, pencere, sag_resim, sol_resim, asagi_resim, yukari_resim):#obje resmini gerekli şekilde çizdiren fonksiyon
		if self.sagb:#eğer obje sağa bakıyorsa sağa bakarkenki halini çiz
			pencere.blit(sag_resim, (self.x - self.genislik/2, self.y - self.yukseklik/2))
		elif self.solb:
		      pencere.blit(sol_resim, (self.x - self.genislik/2, self.y - self.yukseklik/2))
		      self.solb = False
		      self.sagb = True
		elif self.asab:
		      pencere.blit(asagi_resim, (self.x - self.genislik/2, self.y - self.yukseklik/2))
		elif self.yukb:
		      pencere.blit(yukari_resim, (self.x - self.genislik/2, self.y - self.yukseklik/2))