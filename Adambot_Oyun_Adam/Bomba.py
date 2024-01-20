from Hareketli_Obje import *
from Patlama import *
import pygame

pygame.init()

class Bomba(Hareketli_Obje):
    def __init__(self, x, y, genislik, yukseklik, can, hiz, yerden_yukseklik, hasar, ivme, sagb, solb, yukb, asab):
        #Parametrelerden gelen değerleri objeye almak/işlemek
        super().__init__(x, y, genislik, yukseklik, can, hiz)#Hareketli_Obje class'ının init fonksiyonundan gerekli değişkenleri almak
        self.yerden_yukseklik = yerden_yukseklik
        self.ivme = ivme
        self.inis_hizi = 0.0
        self.hasar = hasar

        self.sagb, self.solb, self.yukb, self.asab = sagb, solb, yukb, asab
        self.x, self.y, self.genislik, self.yukseklik, self.can, self.hiz = x, y, genislik, yukseklik, can, hiz

        self.hiz_siniri = 999
        self.surtunme = 0.1
        self.ivme = [ivme[0], ivme[1]]
            

    def dus(self, patlamalar, p1, p2, p3):
        self.yerden_yukseklik -= self.inis_hizi
        self.inis_hizi += 0.2
        if self.yerden_yukseklik <= 0:
            self.yerden_yukseklik = 0
            patlamalar.append(Patlama(self.x, self.y, 32, 32, 0, 0, 0, self.hasar, p1, p2, p3))
            return True
        return False
