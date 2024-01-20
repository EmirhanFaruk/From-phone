import pygame
from math import cos, sin, pi
from random import randint

pygame.init()

infoObject = pygame.display.Info()

monitor_width, monitor_height = infoObject.current_w, infoObject.current_h

win = pygame.display.set_mode((monitor_width, monitor_height))


class Ball:
    def __init__(self, x, y, r, vector, speed, degree, degree_change, colour):
        self.x, self.y, self.r, self.vector, self.speed, self.degree, self.degree_change, self.colour = x, y, r, [0, 0], speed, degree, degree_change, colour
        self.old_point = (self.x, self.y)
        self.change_vector()
        self.older_point = self.old_point
    
    def change_vector(self):
        self.degree += self.degree_change
        rad = (self.degree * pi) / 180
        self.vector[0] = cos(rad) * self.speed
        self.vector[1] = sin(rad) * self.speed
    
    def ricochet(self):
        if self.x - self.r - 1 < 0:
            self.vector[0] = abs(self.vector[0])
            self.degree = 180 - self.degree 
            self.change_vector()
            #self.degree += randint(90, 270)
            #self.speed = randint(15, 30)
        if self.x + self.r + 1 > monitor_width:
            self.vector[0] = -abs(self.vector[0])
            self.degree = 180 - self.degree
            self.change_vector()
            #self.degree += randint(90, 270)
            #self.speed = randint(15, 30)
        if self.y - self.r - 1< 0:
            self.vector[1] = abs(self.vector[1])
            self.degree = 360 - self.degree
            self.change_vector()
            #self.degree += randint(90, 270)
            #self.speed = randint(15, 30)
        if self.y + self.r + 1 > monitor_height:
            self.vector[1] = - abs(self.vector[1])
            self.degree = 360 - self.degree
            self.change_vector()
            #self.degree += randint(90, 270)
            #self.speed = randint(15, 30)
    
    def move(self):
        self.older_point = self.old_point
        self.old_point = (self.x, self.y)
        self.x += self.vector[0]
        if self.x - self.r < 0:
            self.x = self.r
        if self.x + self.r > monitor_width:
            self.x = monitor_width - self.r
        self.y += self.vector[1]
        if self.y - self.r < 0:
            self.y = self.r
        if self.y + self.r > monitor_height:
            self.y = monitor_height - self.r
    
    def draw(self):
        #pygame.draw.line(win, (200, 100, 50), self.older_point, self.old_point)
        #pygame.draw.line(win, self.colour, (self.x, self.y), self.old_point)#(self.x - self.vector[0], self.y - self.vector[1]))
        
        pygame.draw.circle(win, self.colour, (self.x, self.y), self.r)
        #pygame.draw.circle(win, (255, 255, 255), (self.x, self.y), self.r, 2)
        


balls = []
#balls.append(Ball(monitor_width/2, monitor_height/2, 20, [0, 0], 7, 0, -1, (200, 100, 50)))
#balls.append(Ball(monitor_width/2, monitor_height/2 - 200, 20, [0, 0], 20, 0, 1, (150, 50, 150)))

for i in range(50):
    balls.append(Ball(randint(100, monitor_width-100), randint(100, monitor_height-100), 20, [0, 0], 30, randint(1, 355), 0, (randint(100, 255), randint(100, 255), randint(100, 255))))#(255, 255, 0)))#(randint(100, 255), randint(100, 255), randint(100, 255))))#(randint(70, 170), randint(170, 255), randint(100, 200))))#(120, 250, 150)))


clock = pygame.time.Clock()

running = True

while running:
    win.fill((0, 0, 0))#(250, 150, 150))#(100, 0, 100))
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    for ball in balls:
        #ball.change_vector()
        ball.ricochet()
        ball.move()
        ball.draw()
    
    pygame.display.flip()