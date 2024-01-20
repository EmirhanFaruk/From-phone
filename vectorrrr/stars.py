import pygame
from math import cos, sin, pi
from random import randint

pygame.init()

infoObject = pygame.display.Info()

monitor_width, monitor_height = infoObject.current_w, infoObject.current_h

win = pygame.display.set_mode((monitor_width, monitor_height))

center = (monitor_width/2, monitor_height/2)

class Ball:
    def __init__(self, x, y, r, vector, speed, colour):
        self.x, self.y, self.r, self.vector, self.speed, self.colour = x, y, r, [0, 0], speed, colour
        self.planet = False
        
        self.vector[0] = self.speed * ((self.x - center[0]) / 100)
        self.vector[1] = self.speed * ((self.y - center[1]) / 100)
        self.grow = 0
        
        
    """
    def change_vector(self):
        self.degree += self.degree_change
        rad = (self.degree * pi) / 180
        self.vector[0] = cos(rad) * self.speed
        self.vector[1] = sin(rad) * self.speed
    """
    
    def respawn(self):
        if self.x + self.r < 0 or self.x - self.r > monitor_width or self.y + self.r < 0 or self.y - self.r > monitor_height:
            #while abs(self.x - center[0]) < 100 or abs(self.y - center[1]) < 100:
            self.x, self.y = randint(10, monitor_width-10), randint(10, monitor_height-10)
            self.vector[0] = self.speed * ((self.x - center[0]) / 100)
            self.vector[1] = self.speed * ((self.y - center[1]) / 100)
            if abs(self.vector[0])<10 and abs(self.vector[1])<10:
                self.x = monitor_width + 200
            if False:#2 == randint(0, 100):
                self.grow = self.vector[0]/1000 + self.vector[1]/1000
                self.planet = True
                self.colour = (randint(100, 255), randint(100, 255), randint(100, 255))
                self.vector[0] /= 100
                self.vector[1] /= 100
                self.r = 1
            else:
                self.grow = 0
                self.planet = False
                self.colour = (255, 255, 255)
                self.r = 1
            
    
    def move(self):
        self.x += self.vector[0]
        self.y += self.vector[1]
        self.r += self.grow
        
    
    def draw(self):
        #pygame.draw.circle(win, (255, 255, 255), (self.x, self.y), self.r, 2)
        pygame.draw.line(win, self.colour, (self.x, self.y), (self.x - self.vector[0], self.y - self.vector[1]))
        #pygame.draw.circle(win, self.colour, (self.x, self.y), self.r)




balls = []
#balls.append(Ball(monitor_width/2, monitor_height/2, 20, [0, 0], 7, 0, -1, (200, 100, 50)))
#balls.append(Ball(monitor_width/2, monitor_height/2 - 200, 20, [0, 0], 20, 0, 1, (150, 50, 150)))

for i in range(50):
    balls.append(Ball(randint(100, monitor_width-100), randint(100, monitor_height-100), 1, [0, 0], 10, (255, 255, 255)))


clock = pygame.time.Clock()

running = True
#ball_size = 1

while running:
    win.fill((0, 0, 0))#(250, 150, 150))#(100, 0, 100))
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #pygame.draw.circle(win, (20, 170, 100), (center[0], center[1]), ball_size)
    #ball_size += 0.1
    
    for ball in balls:
        ball.respawn()
        ball.move()
        ball.draw()
    
    pygame.display.flip()