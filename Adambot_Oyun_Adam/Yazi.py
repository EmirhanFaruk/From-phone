import pygame
pygame.init()


class Yazi:
    def __init__(self, x, y, boyut, yazi):
        self.x, self.y, self.boyut, self.yazi = x, y, boyut, yazi
    def ekrana_ciz(self, pencere):
        self.fon = pygame.font.Font("PKMN_RBYGSC.ttf", self.boyut)
        self.yazi_yuzeyi = self.fon.render(self.yazi, False, (0, 0, 0))
        self.yazi_genisligi = self.yazi_yuzeyi.get_width()
        pencere.blit(self.yazi_yuzeyi, (int(self.x - self.yazi_genisligi/2), int(self.y)))
