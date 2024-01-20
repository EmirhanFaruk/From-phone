from Hareketli_Obje import *
from Yazi import *
from Patlama import *
from Mermi import *
from Bomba import *
import pygame

pygame.init()

pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize

muzik = pygame.mixer.Sound("müzik.mp3")
muzik.set_volume(0.3)
bzz = pygame.mixer.Sound("bzzz.mp3")
bzz.set_volume(0.1)
mermi_sesi = pygame.mixer.Sound("mermi_ateşi_sesi_gerçek.mp3")#"pshot.wav")
mermi_sesi.set_volume(0.1)
#Team Fortress 2 Resupply Cabinet sound effect.mp3
cephane_yenileme_sesi = pygame.mixer.Sound("Team Fortress 2 Resupply Cabinet sound effect.mp3")
cephane_yenileme_sesi.set_volume(0.1)
pygame.mixer.set_num_channels(999)





class Adambot(Hareketli_Obje):
    def __init__(self, x, y, genislik, yukseklik, can, hiz, hiz_siniri, hasar, kamikaze_saldiri_gucu, monitor_buyuklugu):
        #Parametrelerden gelen değerleri objeye almak/işlemek
        super().__init__(x, y, genislik, yukseklik, can, hiz)#Hareketli_Obje class'ının init fonksiyonundan gerekli değişkenleri almak
        self.kamikaze_saldiri_gucu = kamikaze_saldiri_gucu
        self.hasar = hasar
        #Yükseklik değişkeni ve kamikaze dolum süresi değişkenleri
        self.kamikaze_dolum_suresi = 30 #1 saniyede bir
        self.kamikaze_saldirisi_yuksekligi = 0
        self.kamikaze_saldirisinda = False
        
        self.ates_suresi = 2
        
        #akışkan hareket sistemi için değişkenler
        self.hiz_siniri = hiz_siniri
        self.hiz_asimi_surtunmesi = 0.9
        self.surtunme = 0.5
        self.ivme = [0, 0]

        self.bomba_suresi = 0
        self.bomba_sayisi_max = 30
        self.bomba_sayisi = 30
        self.bomba_yazisi = Yazi(monitor_buyuklugu[0]//2, monitor_buyuklugu[1]-60, 30, "Bomba sayisi: " + str(self.bomba_sayisi))

        self.cephane_yenileme_suresi = 60


    def cephane_doldur(self):
        if self.cephane_yenileme_suresi >= 60:
            self.bomba_sayisi = self.bomba_sayisi_max
            self.bomba_yazisi.yazi = "Bomba sayisi: " + str(self.bomba_sayisi)
            pygame.mixer.find_channel().play(cephane_yenileme_sesi)
            self.cephane_yenileme_suresi = 0

    
    def cephane_goster(self, pencere):
        self.bomba_yazisi.ekrana_ciz(pencere)

    
    def sayac_arttir(self):
        self.cephane_yenileme_suresi += 1
        self.kamikaze_dolum_suresi += 1
        self.bomba_suresi += 1

    
    def bomba_birak(self, bombalar):
        if self.bomba_suresi >= 5 and self.bomba_sayisi > 0:
            bombalar.append(Bomba(self.x, self.y, 16, 16, 0, 1.5, self.yerden_yukseklik, 40, self.ivme, self.sagb, self.solb, self.yukb, self.asab))
            self.bomba_suresi = 0
            self.bomba_sayisi -= 1
            self.bomba_yazisi.yazi = "Bomba sayisi: " + str(self.bomba_sayisi)
        return bombalar

    def akiskan_hareket_sistemi(self):
        if self.sagg:
            if self.ivme[0] == 0:
                self.ivme[0] = self.surtunme
            self.ivme[0] += self.hiz
        if self.solg:
            if self.ivme[0] == 0:
                self.ivme[0] = -self.surtunme
            self.ivme[0] = self.ivme[0] - self.hiz
            
        if self.ivme[0] > 0:
            self.ivme[0] -= self.surtunme
        elif self.ivme[0] < 0:
            self.ivme[0] += self.surtunme
        if abs(self.ivme[0]) <= self.surtunme:
            self.ivme[0] = 0

        if abs(self.ivme[0]) > self.hiz_siniri:
            self.ivme[0] *= self.hiz_asimi_surtunmesi
        

        if self.asag:
            if self.ivme[1] == 0:
                self.ivme[1] = self.surtunme
            self.ivme[1] += self.hiz
        if self.yukg:
            if self.ivme[1] == 0:
                self.ivme[1] = -self.surtunme
            self.ivme[1] = self.ivme[1] - self.hiz
        
        if self.ivme[1] > 0:
            self.ivme[1] -= self.surtunme
        elif self.ivme[1] < 0:
            self.ivme[1] += self.surtunme
        if abs(self.ivme[1]) <= self.surtunme:
            self.ivme[1] = 0

        if abs(self.ivme[1]) > self.hiz_siniri:
            self.ivme[1] *= self.hiz_asimi_surtunmesi

        return

    def hareket_et_ivmeli(self):
        self.x += self.ivme[0]
        self.y += self.ivme[1]

    
    def kamikaze_saldirisi(self, patlamalar, p1, p2, p3):
        if not(self.kamikaze_saldirisinda) and self.kamikaze_dolum_suresi >= 30:
            if self.yerden_yukseklik > 10:
                self.hiz = 0.3 * (100//self.yerden_yukseklik + 1)
                self.kamikaze_saldirisinda = True
                self.kamikaze_saldirisi_yuksekligi = self.yerden_yukseklik * self.kamikaze_saldiri_gucu
        if self.kamikaze_saldirisinda:
            if self.yerden_yukseklik <= 5:
                self.yerden_yukseklik = 0
                patlamalar.append(Patlama(self.x, self.y, int(self.kamikaze_saldirisi_yuksekligi), int(self.kamikaze_saldirisi_yuksekligi), 0, 0, 0, self.kamikaze_saldirisi_yuksekligi, p1, p2, p3))
                self.kamikaze_saldirisinda = False
                self.hiz = 1.5
                self.kamikaze_dolum_suresi = 0
            else:
                self.yerden_yukseklik *= 0.5

    def ates_et(self, pencere, muhtemel_hedefler):
        if self.ates_suresi < 1:
            self.ates_suresi += 1
        else:
            if self.sagb:#eğer obje sağa bakıyorsa sağa bakarkenki halini çiz
                Mermi(pencere, self.x + self.genislik*0.5, self.y - self.yerden_yukseklik, uniform(self.x + self.yerden_yukseklik + 100, self.x + self.yerden_yukseklik * 2 + 100), uniform(self.y - 10, self.y + 10), self.hasar, muhtemel_hedefler)
            elif self.solb:
                Mermi(pencere, self.x , self.y - self.yerden_yukseklik, uniform(self.x - self.yerden_yukseklik * 2 - 100, self.x - self.yerden_yukseklik - 100), uniform(self.y, self.y + 10), self.hasar, muhtemel_hedefler)
            elif self.asab:
                Mermi(pencere, self.x , self.y - self.yerden_yukseklik, uniform(self.x - 10, self.x + 10), uniform(self.y + self.yerden_yukseklik + 100, self.y + self.yerden_yukseklik * 2 + 100), self.hasar, muhtemel_hedefler)
            elif self.yukb:
                Mermi(pencere, self.x , self.y - self.yerden_yukseklik - self.yukseklik*0.5, uniform(self.x - 10, self.x + 10), uniform(self.y - self.yerden_yukseklik * 2 - 100, self.y - self.yerden_yukseklik - 100), self.hasar, muhtemel_hedefler)
            self.ates_suresi = 0
