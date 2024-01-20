import pygame
from math import pi, cos, sin


pygame.init()


class Havan_Topu:
	def __init__(self, x, y, ivme):
		self.x, self.y = x, y
		self.vektor = ivme
	def hareket_et(self, etki):
		self.vektor[0] += etki[0]
		self.vektor[1] += etki[1]
		self.x += self.vektor[0]
		self.y += self.vektor[1]
	def ekrana_ciz(self, ekran):
		pygame.draw.line(ekran, (10, 160, 10), (self.x, self.y), (self.x - self.vektor[0], self.y - self.vektor[1]))
		pygame.draw.rect(ekran, (10, 160, 10), pygame.Rect(self.x - 2, self.y - 2, 4, 4))
