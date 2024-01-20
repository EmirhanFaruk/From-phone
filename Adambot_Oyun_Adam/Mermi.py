from random import randint
import pygame

pygame.init()

pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize

mermi_sesi = pygame.mixer.Sound("mermi_ateşi_sesi_gerçek.mp3")#"pshot.wav")
mermi_sesi.set_volume(0.1)



def Mermi(pencere, bx, by, hx, hy, hasar, muhtemel_hedefler):
    pygame.mixer.find_channel().play(mermi_sesi)
    if randint(1, 3) == 2:
        pygame.draw.line(pencere, (200, 200, 100), (bx, by), (hx, hy))
    pygame.draw.circle(pencere, (200, 200, 100), (hx, hy), 2)
    for hedef in muhtemel_hedefler:
        if hx > hedef.x - hedef.genislik/2 and hx < hedef.x + hedef.genislik/2:
            if hy > hedef.y - hedef.yukseklik/2 and hy < hedef.y + hedef.yukseklik/2:
                hedef.can -= hasar
