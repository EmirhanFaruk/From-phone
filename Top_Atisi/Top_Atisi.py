import pygame
from Havan import *


pygame.init()

genislik, yukseklik = 2000, 1000
bayraklar = pygame.SCALED | pygame.FULLSCREEN | pygame.NOFRAME
pencere = pygame.display.set_mode((genislik, yukseklik), bayraklar)

yon = 0
ana_havan = Havan(1000, 500, 25, yon)
havan_toplari = []
ana_havan.vektor_hesapla()
ana_havan.ates_et(havan_toplari)

calis = True
kare_hizi = 60
sayac = pygame.time.Clock()
while calis:
	pencere.fill((10, 10, 10))
	sayac.tick(kare_hizi)
	for olay in pygame.event.get():
		if olay == pygame.QUIT:
			calis = False
	ana_havan = Havan(1000, 500, 25, yon)
	yon += 31
	ana_havan.vektor_hesapla()
	ana_havan.ates_et(havan_toplari)
	ana_havan.ekrana_ciz(pencere)
	for havan_topu in havan_toplari:
		if havan_topu.vektor[0] > 0.01:
			surtunme = -0.01
		elif havan_topu.vektor[0] < -0.01:
			surtunme = 0.01
		else:
			surtunme = -havan_topu.vektor[0]
		havan_topu.hareket_et([0, 0.9])
		havan_topu.ekrana_ciz(pencere)
	pygame.display.flip()
	
pygame.quit()