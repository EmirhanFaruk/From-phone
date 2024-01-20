import pygame

pygame.init()

class Obje:
    def __init__(self, x, y, genislik, yukseklik, can):
        #Parametrelerden gelen değerleri objeye almak/işlemek
        self.x, self.y, self.genislik, self.yukseklik, self.can = x, y, genislik, yukseklik, can

        #Hareket için gerekli olan değişkenleri oluşturmak(sağa bak = sagb, sağa git = sagg gibi)
        self.sagb = True
        self.solb, self.asab, self.yukb = False, False, False
        self.sagg, self.solg, self.asag, self.yukg = False, False, False, False

        self.yerden_yukseklik = 0#self.yukseklik#yer birimleri kendi yükseklik yüksekliğinde olacak

    


    def golge_ciz(self, pencere, sag_resim, sol_resim, asagi_resim, yukari_resim, abbuyukluk):#gölge çizme fonksiyonu
        if self.sagb:#eğer obje sağa bakıyorsa sağa bakarkenki halini çiz
            sag_resim.set_alpha(220-self.yerden_yukseklik)
            sag_resim = pygame.transform.scale(sag_resim, (int(self.genislik + self.yerden_yukseklik/2), int(abbuyukluk + self.yerden_yukseklik/2)))
            pencere.blit(sag_resim, (self.x - self.genislik/2, self.y - self.yukseklik/2 - self.yerden_yukseklik))
        elif self.solb:
            sol_resim.set_alpha(220-self.yerden_yukseklik)
            sol_resim = pygame.transform.scale(sol_resim, (int(self.genislik + self.yerden_yukseklik/2), int(abbuyukluk + self.yerden_yukseklik/2)))
            pencere.blit(sol_resim, (self.x - self.genislik/2, self.y - self.yukseklik/2 - self.yerden_yukseklik))
        elif self.asab:
            asagi_resim.set_alpha(220-self.yerden_yukseklik)
            asagi_resim = pygame.transform.scale(asagi_resim, (int(self.genislik + self.yerden_yukseklik/2), int(abbuyukluk + self.yerden_yukseklik/2)))
            pencere.blit(asagi_resim, (self.x - self.genislik/2, self.y - self.yukseklik/2 - self.yerden_yukseklik))
        elif self.yukb:
            yukari_resim.set_alpha(220-self.yerden_yukseklik)
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
