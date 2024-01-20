import pygame
from Yazi import *

pygame.init()

class Dugme:
    def __init__(self, x, y, genislik, yukseklik, renk, yazi):
        self.x, self.y, self.genislik, self.yukseklik, self.renk, self.yazi = x, y, genislik, yukseklik, renk, Yazi(x + genislik/2, y + yukseklik/4, yukseklik//2, yazi)
        
        self.acik_renk = (int((self.renk[0]*1.1)), int((self.renk[1]*1.1)), int((self.renk[2]*1.1)))
        self.koyu_renk = (int((self.renk[0]*0.9)), int((self.renk[1]*0.9)), int((self.renk[2]*0.9)))
        for i in range(3):
        	if self.acik_renk[i] > 255:
        		self.acik_renk[i] = 255
        
        
    def ekrana_ciz(self, pencere):
        pygame.draw.rect(pencere, self.renk, pygame.Rect(self.x, self.y, self.genislik, self.yukseklik))
        pygame.draw.rect(pencere, self.koyu_renk, pygame.Rect(self.x, self.y + self.yukseklik*0.95, self.genislik, self.yukseklik*0.05))
        pygame.draw.rect(pencere, self.koyu_renk, pygame.Rect(self.x, self.y, self.genislik*0.05, self.yukseklik))
        pygame.draw.rect(pencere, self.acik_renk, pygame.Rect(self.x + self.genislik*0.95, self.y, self.genislik*0.05, self.yukseklik))
        pygame.draw.rect(pencere, self.acik_renk, pygame.Rect(self.x, self.y, self.genislik, self.yukseklik*0.05))
        
        self.yazi.ekrana_ciz(pencere)
        
    def tiklama_kontrolu(self, tiklamalar):
        if tiklamalar:
            for tiklama_pozisyonu in tiklamalar:
                if tiklamalar[tiklama_pozisyonu][0] > self.x and tiklamalar[tiklama_pozisyonu][0] < self.x + self.genislik:
                    if tiklamalar[tiklama_pozisyonu][1] > self.y and tiklamalar[tiklama_pozisyonu][1] < self.y + self.yukseklik:
                        return True
        return False
