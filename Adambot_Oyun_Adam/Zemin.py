import pygame

pygame.init()

class Zemin:
    def __init__(self, x, y, genislik, yukseklik, resim, resmi_fulle):
        self.x, self.y, self.genislik, self.yukseklik = x, y, genislik, yukseklik
        self.yinele_x = 0
        self.yinele_y = 0
        self.resim = resim
        self.resim_genisligi = self.resim.get_width()
        self.resim_yuksekligi = self.resim.get_height()
        if resmi_fulle:
            self.resim = pygame.transform.scale(resim, (genislik, yukseklik))
            self.resim.convert()
        else:
            self.yinele_x = self.genislik // self.resim.get_width()
            self.yinele_y = self.yukseklik // self.resim.get_height()
        self.resmi_fulle = resmi_fulle
    def ana_ekrana_ciz(self, pencere):
        if self.resmi_fulle:
            pencere.blit(self.resim, (self.x, self.y))
        else:
            for x in range(self.yinele_x):
                for y in range(self.yinele_y):
                    pencere.blit(self.resim, (self.x + self.resim_genisligi * x, self.y + self.resim_yuksekligi * y))
