import pygame
from pygame import Color
from math import sqrt
from random import choice, randint, uniform


pygame.init()

class Hareketli_Obje:
    def __init__(self, x, y, genislik, yukseklik, can, hiz, hiz_siniri = 0):
        #Parametrelerden gelen değerleri objeye almak/işlemek
        self.x, self.y, self.genislik, self.yukseklik, self.can, self.hiz = x, y, genislik, yukseklik, can, hiz

        #Hareket için gerekli olan değişkenleri oluşturmak(sağa bak = sagb, sağa git = sagg gibi)
        self.sagb = True
        self.solb, self.asab, self.yukb = False, False, False
        self.sagg, self.solg, self.asag, self.yukg = False, False, False, False

        self.yerden_yukseklik = self.yukseklik#yer birimleri kendi yükseklik yüksekliğinde olacak

        #akışkan hareket sistemi için değişkenler
        self.hiz_siniri = hiz_siniri
        self.hiz_asimi_surtunmesi = 0.9
        self.surtunme = 0.1
        self.ivme = [0, 0]
        return
    

    def akiskan_hareket_sistemi(self):
        if self.sagg:
            if self.ivme[0] == 0:
                self.ivme[0] = 0.1
            self.ivme[0] += self.hiz
        if self.solg:
            if self.ivme[0] == 0:
                self.ivme[0] = -0.1
            self.ivme[0] = self.ivme[0] - self.hiz
            
        if self.ivme[0] > 0:
            self.ivme[0] -= self.surtunme
        elif self.ivme[0] < 0:
            self.ivme[0] += self.surtunme
        if abs(self.ivme[0]) <= 0.1:
            self.ivme[0] = 0

        if abs(self.ivme[0]) > self.hiz_siniri:
            self.ivme[0] *= self.hiz_asimi_surtunmesi
        

        if self.asag:
            if self.ivme[1] == 0:
                self.ivme[1] = 0.1
            self.ivme[1] += self.hiz
        if self.yukg:
            if self.ivme[1] == 0:
                self.ivme[1] = -0.1
            self.ivme[1] = self.ivme[1] - self.hiz
            
        if self.ivme[1] > 0:
            self.ivme[1] -= self.surtunme
        elif self.ivme[1] < 0:
            self.ivme[1] += self.surtunme
        if abs(self.ivme[1]) <= 0.1:
            self.ivme[1] = 0

        if abs(self.ivme[1]) > self.hiz_siniri:
            self.ivme[1] *= self.hiz_asimi_surtunmesi

        return

    def hareket_et_ivmeli(self):
        self.x += self.ivme[0]
        self.y += self.ivme[1]

    
    def hareket_et(self):#objeyi gereken değişkenlere göre hareket ettirecek olan fonksiyon
        if self.sagg:#eğer sağa gidiyorsa x koordinatını hız ile arttır
            self.x += self.hiz
        elif self.solg:
            self.x -= self.hiz
        if self.yukg:
            self.y -= self.hiz
        elif self.asag:
            self.y += self.hiz
        return

    def golge_ciz(self, pencere, sag_resim, sol_resim, asagi_resim, yukari_resim, abbuyukluk):#gölge çizme fonksiyonu
        if self.sagb:#eğer obje sağa bakıyorsa sağa bakarkenki halini çiz
            sag_resim.set_alpha(100-self.yerden_yukseklik)
            sag_resim = pygame.transform.scale(sag_resim, (int(self.genislik + self.yerden_yukseklik/2), int(abbuyukluk + self.yerden_yukseklik/2)))
            pencere.blit(sag_resim, (self.x - self.genislik/2, self.y - self.yukseklik/2 - self.yerden_yukseklik))
        elif self.solb:
            sol_resim.set_alpha(100-self.yerden_yukseklik)
            sol_resim = pygame.transform.scale(sol_resim, (int(self.genislik + self.yerden_yukseklik/2), int(abbuyukluk + self.yerden_yukseklik/2)))
            pencere.blit(sol_resim, (self.x - self.genislik/2, self.y - self.yukseklik/2 - self.yerden_yukseklik))
        elif self.asab:
            asagi_resim.set_alpha(100-self.yerden_yukseklik)
            asagi_resim = pygame.transform.scale(asagi_resim, (int(self.genislik + self.yerden_yukseklik/2), int(abbuyukluk + self.yerden_yukseklik/2)))
            pencere.blit(asagi_resim, (self.x - self.genislik/2, self.y - self.yukseklik/2 - self.yerden_yukseklik))
        elif self.yukb:
            yukari_resim.set_alpha(100-self.yerden_yukseklik)
            yukari_resim = pygame.transform.scale(yukari_resim, (int(self.genislik + self.yerden_yukseklik/2), int(abbuyukluk + self.yerden_yukseklik/2)))
            pencere.blit(yukari_resim, (self.x - self.genislik/2, self.y - self.yukseklik/2 - self.yerden_yukseklik))
        #pygame.draw.circle(pencere, ((52/255)*self.yerden_yukseklik, (140/255)*self.yerden_yukseklik, (49/255)*self.yerden_yukseklik), ((self.x), (self.y)), self.genislik/3 + self.yerden_yukseklik/10)#gölgeyi yuvarlak olarak çizmek/(52, 140, 49)
        return


    def ana_ekrana_ciz(self, pencere, sag_resim, sol_resim, asagi_resim, yukari_resim):#obje resmini gerekli şekilde çizdiren fonksiyon
        if self.sagb:#eğer obje sağa bakıyorsa sağa bakarkenki halini çiz
            pencere.blit(sag_resim, (self.x - self.genislik/2, self.y - self.yukseklik/2 - self.yerden_yukseklik))
        elif self.solb:
            pencere.blit(sol_resim, (self.x - self.genislik/2, self.y - self.yukseklik/2 - self.yerden_yukseklik))
        elif self.asab:
            pencere.blit(asagi_resim, (self.x - self.genislik/2, self.y - self.yukseklik/2 - self.yerden_yukseklik))
        elif self.yukb:
            pencere.blit(yukari_resim, (self.x - self.genislik/2, self.y - self.yukseklik/2 - self.yerden_yukseklik))
        return
