import pygame
from math import cos, sin, pi, sqrt
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
        self.vector[1] = abs(self.vector[1])
        if self.degree%360 < 360 and self.degree%360 > 180:
            self.degree -= 180
    
    def change_vector(self):
        self.degree += self.degree_change
        rad = (self.degree * pi) / 180
        self.vector[0] = (cos(rad) * self.speed)
        if self.vector[0] > 0:
            self.vector[0] += 1
        elif self.vector[0] < 0:
            self.vector[0] -= 1
        self.vector[1] += (sin(rad) * self.speed) + 0.81
        #self.r = sqrt(self.vector[0]**2 + self.vector[1]**2)
        
    
    def ricochet(self):
        if self.x - self.r <= 0 and self.vector[0] < 0:
            self.degree = 180 -self.degree
            self.vector[0] *= 0.9
            self.speed -= 0.3
            if self.speed <= 0:
                self.speed = 0
        if self.x + self.r >= monitor_width and self.vector[0] > 0:
            self.degree = 180 -self.degree
            self.vector[0] *= 0.9
            self.speed -= 0.3
            if self.speed <= 0:
                self.speed = 0
        if self.y + self.r >= monitor_height and self.vector[1] > 0:
            self.vector[1] = - abs(self.vector[1])*9/10
            self.vector[0] *= 0.9
            self.speed -= (self.speed/5 + 0.1)
            if self.speed <= 0:
                self.speed = 0
    
    def move(self):
        self.change_vector()
        #self.speed += self.speed/1000
        self.older_point = self.old_point
        self.old_point = (self.x, self.y)
        self.x += self.vector[0]
        if self.x - self.r <= 0:
            self.x = self.r
        if self.x + self.r >= monitor_width:
            self.x = monitor_width - self.r
        self.y += self.vector[1]
        if self.vector[1] > 1:
            self.speed += 0.05
        if self.speed <= 0:
            self.speed = 0
        if self.y + self.r > monitor_height:
            self.y = monitor_height - self.r
    
    def draw(self):
        #pygame.draw.circle(win, (self.colour[0] - 70, self.colour[1] - 70, self.colour[2] - 50), self.older_point, self.r)
        #pygame.draw.line(win, self.colour, (self.x, self.y), self.old_point)#(self.x - self.vector[0], self.y - self.vector[1]))
        #pygame.draw.circle(win, (255, 255, 255), (self.x, self.y), self.r, 2)
        pygame.draw.circle(win, self.colour, self.older_point, self.r, 2)
        pygame.draw.circle(win, self.colour, (self.x, self.y), self.r)
        


balls = []
#balls.append(Ball(monitor_width/2, monitor_height/2, 20, [0, 0], 7, 0, -1, (200, 100, 50)))
#balls.append(Ball(monitor_width/2, monitor_height/2 - 200, 20, [0, 0], 20, 0, 1, (150, 50, 150)))

for i in range(1):
    balls.append(Ball(randint(100, monitor_width-100), randint(0, monitor_height), 0, [0, 0], 5, randint(1, 355), 0, (randint(150, 255), randint(150, 255), randint(150, 255))))#(randint(70, 170), randint(170, 255), randint(100, 200))))#(120, 250, 150)))


clock = pygame.time.Clock()

running = True
comp = 0
while running:
    win.fill((0, 0, 0))#(250, 150, 150))#(100, 0, 100))
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    for ball in balls:
        if ball.speed == 0:
            balls.remove(ball)
            continue
        #ball.change_vector()
        ball.ricochet()
        ball.move()
        ball.draw()
    comp += 1
    if comp %1 ==0:
        balls.append(Ball(randint(100, monitor_width-100), randint(0, monitor_height), 20, [0, 0], 5, randint(1, 355), 0, (randint(150, 255), randint(150, 255), randint(150, 255))))
    pygame.display.flip()