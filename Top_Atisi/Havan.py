import pygame
from math import pi, cos, sin
from Havan_Topu import *


pygame.init()


class Havan:
	def __init__(self, x, y, guc, yon):
		self.x, self.y, self.guc, self.yon = x, y, guc, yon
		self.vektor = [0, 0]
	def vektor_hesapla(self):
		radyan = self.yon * (pi / 180)
		self.vektor[0] = cos(radyan) * self.guc
		self.vektor[1] = sin(radyan) * self.guc
	def ates_et(self, havan_toplari):
		havan_toplari.append(Havan_Topu(self.x, self.y, self.vektor))
	def ekrana_ciz(self, ekran):
		pygame.draw.rect(ekran, (150, 60, 10), pygame.Rect(self.x - 5, self.y - 5, 10, 10))