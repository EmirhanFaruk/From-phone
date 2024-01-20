import pygame
from math import sqrt, cos, sin, pi
from random import randint

pygame.init()

win = pygame.display.set_mode((800, 400), pygame.FULLSCREEN)

pygame.display.set_caption("bruh")

infoObject = pygame.display.Info()

monitor_width, monitor_height = infoObject.current_w, infoObject.current_h

def distance(x1, y1, x2, y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)

class Player:
    def __init__(self, x, y, w, h, velocity):
        self.x, self.y, self.w, self.h, self.velocity = x, y, w, h, velocity
        self.vel = [0, 0]
        self.vel_lim = 15
    
    def draw(self):
        pygame.draw.rect(win, (200, 50, 50), pygame.Rect(self.x - self.w/2, self.y -self.h/2, self.w, self.h))
    
    def move(self):
        self.x += self.vel[0]
        self.y += self.vel[1]
        
    def change_direction(self, lrd, udd):
        self.vel[0] *= lrd
        self.vel[1] *= udd
    
    def get_velocity(self, lr, ud):
        if lr:
            if self.vel[0] == 0:
                self.vel[0] = 0.1
            self.vel[0] *= self.velocity
        else:
            if self.vel[0] != 0:
                if abs(self.vel[0])  <= 0.1:
                    self.vel[0] = 0
                else:
                    if self.vel[0] > 0:
                        self.vel[0] -= 0.1
                    else:
                        self.vel[0] += 0.1
        if ud:
            if self.vel[1] == 0:
                self.vel[1] = 0.1
            self.vel[1] *= self.velocity
        else:
            if self.vel[1] != 0:
                if abs(self.vel[1])  <= 0.1:
                    self.vel[1] = 0
                else:
                    if self.vel[1] > 0:
                        self.vel[1] -= 0.1
                    else:
                        self.vel[1] += 0.1
        while distance(0, 0, self.vel[0], self.vel[1]) > self.vel_lim:
            self.vel[0] *= 0.9
            self.vel[1] *= 0.9

p = Player(200, 200, 10, 10, 1.4)

counter = 0
da_lr = [True, 1]
da_ud = [False, 1]


clock = pygame.time.Clock()
running = True
while running:
    counter += 1
    
    
    if counter %30 == 0:
        if da_lr[0]:
            da_lr[1] *= -1
            p.change_direction(da_lr[1], 1)
            da_lr[0] = False
            da_ud[0] = True
        elif da_ud[0]:
            da_ud[1] *= -1
            p.change_direction(1, da_ud[1])
            da_ud[0] = False
            da_lr[0] = True
            
    
    win.fill((100, 200, 100))#(100, 0, 100))
    pygame.draw.rect(win, (0, 0, 0), pygame.Rect(0, 0, 800, 400), 2)
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    p.get_velocity(da_lr[0], da_ud[0])
    p.move()
    p.draw()
    
    
    
    
    pygame.display.flip()