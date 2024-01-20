from Hareketli_Obje import *
import pygame
from random import choice

pygame.init()

class Tank(Hareketli_Obje):
    def __init__(self, x, y, genislik, yukseklik, can, hiz):
        #Parametrelerden gelen değerleri objeye almak/işlemek
        Hareketli_Obje.__init__(self, x, y, genislik, yukseklik, can, hiz)#Hareketli_Obje class'ının init fonksiyonundan gerekli değişkenleri almak
        self.dusurdu = False
        self.goruntu_sayaci = 0;
        self.yerden_yukseklik = 0

    def sayi_dusur(self, sayac):
        if not(self.dusurdu) and self.can <= 0:
            sayac -= 1
            self.dusurdu = True
            return sayac
        return sayac

    def ana_ekrana_ciz(self, pencere, r0, r1, r2, r3):
        if self.can > 0:
            pencere.blit(r0, (self.x - self.genislik/2, self.y))
        else:
            self.goruntu_sayaci += 0.1
            pencere.blit([r1, r2, r3][int(self.goruntu_sayaci//3)], (self.x - self.genislik/2, self.y))
            if self.goruntu_sayaci >= 8:
                self.goruntu_sayaci = 0
        return
