from Hareketli_Obje import *
from Patlama import *
import pygame

pygame.init()

class Anti_Hava_Mermisi(Hareketli_Obje):
	def __init__(self, x, y, genislik, yukseklik, can, hiz, yerden_yukseklik, hasar, ivme, yukseklik_siniri, sure):
		super().__init__(x, y, genislik, yukseklik, can, hiz)#Hareketli_Obje class'ının init fonksiyonundan gerekli değişkenleri almak
		self.yerden_yukseklik = yerden_yukseklik
		self.ivme = ivme
		self.hasar = hasar
		self.yerden_yukseklik = yerden_yukseklik
		self.yukseklik_siniri = yukseklik_siniri
#buradan yukarısına tab koy boşluk yerine
		self.sagb, self.solb, self.yukb, self.asab = True, False, False, False
		self.x, self.y, self.genislik, self.yukseklik, self.can, self.hiz = x, y, genislik, yukseklik, can, hiz

		self.ivme = ivme
		self.sure = 0
		self.sure_siniri = sure
            

	def hareket(self, patlamalar, p1, p2, p3):
		self.sure += 1
		#hareket sistemi ekle
		self.x += self.ivme[0]
		self.y += self.ivme[1]
		self.yerden_yukseklik += self.ivme[2]
		if self.sure >= self.sure_siniri:
			patlamalar.append(Patlama(self.x, self.y - self.yerden_yukseklik/2, 32, 32, self.yerden_yukseklik, 0, 0, self.hasar, p1, p2, p3))
			return True
		return False
        
	def ekrana_ciz(self, ekran):
		pygame.draw.circle(ekran, (100, 100, 100), (self.x, self.y - self.yerden_yukseklik/2), 5)