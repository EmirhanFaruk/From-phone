import pygame
import time
import datetime
from random import randint, choice
from os import listdir
from math import sqrt
"""
e = datetime.datetime.now()
print ("Current date and time = %s" % e)
print ("Today's date:  = %s/%s/%s" % (e.day, e.month, e.year))
print ("The time is now: = %s:%s:%s" % (e.hour, e.minute, e.second))
"""
def get_files(path):
    fl = listdir(path)
    log_info(str(fl))
    for i in range(len(fl)):
        fl[i] = pygame.image.load(path + "/" + fl[i])
    return fl

def get_time_str():
    e = datetime.datetime.now()
    return f"{str(e.day)}-{str(e.month)}-{str(e.year)}   {str(e.hour)}:{str(e.minute)}:{str(e.second)}"

def log_info(text):
    tr = open("Logs.txt", "a")
    tr.write("\n")
    tr.write(text)
    tr.write("\n")
    tr.close()

def put_line():
    return "=" * 40

def start_log():
    w = open("Logs.txt", "w")
    w.write("")
    w.close()
    log_info(put_line())
    log_info(get_time_str())
    return time.time(), time.process_time()
    
def end_log(st, stp, ex=""):
    if ex != "":
        log_info("The program has stopped due an error. The error:\n" + ex)
    log_info(get_time_str())
    log_info("The program has run for " + str(time.time() - st) + " seconds in real life.")
    log_info("The program has run for " + str(time.process_time() - stp) + " seconds in cpu time.")
    


st, stp = start_log()

pygame.init()

def rotate_list(refl):
    newl = []
    for i in range(len(refl)):
        newl.append(pygame.transform.rotate(refl[i], 90))
    return newl

def scale_list(sl, scale):
    for i in range(len(sl)):
        sl[i] = pygame.transform.scale(sl[i], scale)
    return sl


infoObject = pygame.display.Info()

monitor_width, monitor_height = infoObject.current_w, infoObject.current_h

log_info("The screen width and height is: " + str(monitor_width) + "/" + str(monitor_height))

bg = pygame.display.set_mode((monitor_width, monitor_height))

class Base:
    def __init__(self, x, y, w, h, food):
        self.x, self.y, self.w, self.h, self.food = x, y, w, h, food
    def draw(self):
        bg.blit(base, (self.x - self.w/2, self.h - self.h/2))

class Old_Target:
    def __init__(self, x, y, w, h):
        self.x, self.y, self.w, self.h = x, y, w, h

class Leaf:
    def __init__(self, x, y, w, h, nut):
        self.x, self.y, self.w, self.h, self.nut = x, y, w, h, nut
        self.nutf = self.nut
    
    def draw(self):
        if self.nut > self.nutf * 3 / 4:
            bg.blit(leaf_img[3], (self.x - self.w/2, self.y - self.h/2))
        elif self.nut > self.nutf / 2:
            bg.blit(leaf_img[1], (self.x - self.w/2, self.y - self.h/2))
        elif self.nut > self.nutf / 4:
            bg.blit(leaf_img[2], (self.x - self.w/2, self.y - self.h/2))
        else:
            bg.blit(leaf_img[0], (self.x - self.w/2, self.y - self.h/2))


class Ant:
    def __init__(self, x, y, w, h, vel, base = None):#, hp, atk, job):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.x, self.y = int(base.x) , int(base.y)
        self.vel = vel
        self.rl = choice([True, False])#make a better move system mf
        if self.rl:
            self.r = choice([True, False])
            self.l = not(self.r)
            self.u, self.d = False, False
        else:
            self.u = choice([True, False])
            self.d = not(self.u)
            self.r, self.l = False, False
        self.target = None
        self.base = base
        
        #walk
        self.wlkc = randint(1, 30)#give random walk time
        self.wtc = 30
        #animation counters
        self.wc = 0
        self.ac = 0
        #food counter and leaf thing
        self.old_target_loc = None
        self.food = 0
        self.detection_range = 256
    
    
    def distance(self, tcp):
        return sqrt((tcp[0] - self.x)**2 + (tcp[1] - self.y)**2)
    def diff(self, p1, p2):
        return abs(p2 - p1)
    
    def hipotenus(self, a, b):
        return sqrt(a**2 + b**2)
    
    def detect_target(self, leaves):
        for leaf in leaves:
            if self.distance((leaf.x, leaf.y)) < self.detection_range + self.hipotenus(leaf.w/2, leaf.w):
                self.target = leaf
                return True
        return False
    
    
    def stock_base(self):
        self.target.food += self.food
        self.food = 0
        self.target = None
    
    def eat(self, leaves):
        if self.food < 30:
            if self.target.nut - 1 > 0:
                self.target.nut -= 1
                self.food += 1
                #self.attacking = True
            else:
                self.move_random(leaves)
        else:
            self.target = self.base

                    
    
    def move_random(self, leaves):
        if self.food < 30 and not(self.detect_target(leaves)):
            if randint(0, 5) > 2 and self.wlkc == 0:
                rwd = choice(["left", "right", "up", "down"])
                if rwd == "left":
                    self.l = True
                    self.r = False
                    self.u = False
                    self.d = False
                elif rwd == "right":
                    self.l = False
                    self.r = True
                    self.u = False
                    self.d = False
                elif rwd == "up":
                    self.l = False
                    self.r = False
                    self.u = True
                    self.d = False
                elif rwd == "down":
                    self.l = False
                    self.r = False
                    self.u = False
                    self.d = True
                self.wlkc = randint(30, 60)
                self.wtc = 0
                return
            else:
                self.wtc = randint(10, 30)
                self.wlkc = 0
                return
        elif self.food >= 30:
            self.target = self.base
            if self.distance((self.target.x, self.target.y)) > self.target.w/4:
                self.stock_base()
                
                
        else:
            if self.distance((self.target.x, self.target.y)) > self.target.w:
                if self.target.x - self.target.w/2 > self.x:
                    self.l = False
                    self.r = True
                    self.u = False
                    self.d = False
                elif self.target.x + self.target.w/2 < self.x:
                    self.l = True
                    self.r = False
                    self.u = False
                    self.d = False
                elif self.target.y - self.target.h/2 > self.y:
                    self.l = False
                    self.r = False
                    self.u = False
                    self.d = True
                elif self.target.y + self.target.h/2 < self.y:
                    self.l = False
                    self.r = False
                    self.u = True
                    self.d = False
                return
            else:
                self.l = False
                self.r = False
                self.u = False
                self.d = False
                self.eat(leaves)
                return
            
        return
            
            
    
    def move(self, mw, mh):
        if self.wlkc > 0:
            self.wlkc -= 1
        if self.wtc > 0:
            self.wtc -= 1
        
        if self.wtc == 0 and self.wlkc > 0:
            if self.r and self.x + self.w + self.vel < mw:
                self.x += self.vel
            elif self.l and self.x - self.vel > 0:
                self.x -= self.vel
            elif self.u and self.y - self.vel > 0:
                self.y -= self.vel
            elif self.d and self.y + self.h + self.vel < mh:
                self.y += self.vel
                
                
    def draw(self):
        if self.wtc == 0:
            if self.wc >= len(ant_walk):
                self.wc = 0
            if self.u:
                bg.blit(ant_walk[0][int(self.wc%len(ant_walk[0]))], (self.x - self.w/2, self.y - self.h/2))
            elif self.l:
                bg.blit(ant_walk[1][int(self.wc%len(ant_walk[1]))], (self.x - self.w/2, self.y - self.h/2))
            elif self.d:
                bg.blit(ant_walk[2][int(self.wc%len(ant_walk[2]))], (self.x - self.w/2, self.y - self.h/2))
            elif self.r:
                bg.blit(ant_walk[3][int(self.wc%len(ant_walk[3]))], (self.x - self.w/2, self.y - self.h/2))
            self.wc += 0.7
        if self.wtc > 0:
            if self.u:
                bg.blit(ant_walk[0][1], (self.x - self.w/2, self.y - self.h/2))
            elif self.l:
                bg.blit(ant_walk[1][1], (self.x - self.w/2, self.y - self.h/2))
            elif self.d:
                bg.blit(ant_walk[2][1], (self.x - self.w/2, self.y - self.h/2))
            elif self.r:
                bg.blit(ant_walk[3][1], (self.x - self.w/2, self.y - self.h/2))
        #pygame.draw.rect(bg, (10, 255, 50), pygame.Rect(self.x, self.y, self.w, self.h))
    


leaf_img = get_files("assets/leaf")
#leaf_img[0], leaf_img[-1] = leaf_img[-1], leaf_img[0]
leaf_img = scale_list(leaf_img, (256, 256))
leaves = []
for i in range(1):
    leaves.append(Leaf(randint(256, monitor_width - 256), randint(256, monitor_height - 256), 256, 256, 500))

ants = []
ant_walk = pygame.image.load("assets/ant/walk/ant_w1.png")
ant_attack = get_files("assets/ant/attack")
ant_img = pygame.image.load("assets/ant/ant.png")
ant_attack.insert(0, ant_img)
ant_walk_rev = pygame.transform.flip(ant_walk, True, False)
ant_walk = [[ant_walk, ant_img, ant_walk_rev, ant_img]]
ant_img = [ant_img]
for i in range(3):
    ant_img.append(pygame.transform.rotate(ant_img[i], 90))
for i in range(3):
    ant_walk.append(rotate_list(ant_walk[i]))

ant_attack = [ant_attack]
for i in range(3):
    ant_attack.append(rotate_list(ant_attack[i]))

bx = randint(256, monitor_width - 256)
by = randint(256, monitor_height - 256)
da_base = Base(256, 256, 256, 256, 0)
for i in range(1):
    ants.append(Ant(0, 0, 10, 10, 3, da_base))
    
    
base = pygame.image.load("assets/base/Base.png")
base = pygame.transform.scale(base, (256, 256))




end_logged = False


counter = -1
clock = pygame.time.Clock()
bg_clr1 = (20, 180, 50)
sc_r =False
running = True
while running:
    if counter > 0:
        counter -= 1
    if counter == 0:
        running = False
    bg.fill(bg_clr1)
    #bg.blit(base, (monitor_width/2 - 128, monitor_height/2 - 128))
    pygame.draw.rect(bg, (255, 255, 255), pygame.Rect(0, 0, monitor_width, monitor_height), 2)
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end_log(st, stp)
            running = False
            end_logged = True
        if event.type == pygame.VIDEORESIZE:#make a good resize func mf
            #sc_r = not(sc_r)
            #infoObject = pygame.display.Info()
            #monitor_width, monitor_height = infoObject.current_w, infoObject.current_h
            monitor_width, monitor_height = monitor_height, monitor_width
            log_info("The screen width and height have changed to: " + str(monitor_width) + "/" + str(monitor_height))
        
    da_base.draw()
    for leaf in leaves:
        leaf.draw()
    for ant in ants:
        ant.move_random(leaves)
        ant.move(monitor_width, monitor_height)
        ant.draw()
        log_info("‐------------------")
        log_info("Ant no:" + str(ants.index(ant)))
        log_info(str(ant.base.x) + "\n" + str(ant.base.y) + "\n" + str(ant.base.food))
        log_info(str(ant.x) + "\n" + str(ant.y) + "\n" + str(ant.food) + "\n" + str(ant.target))
        if ant.target != None:
            log_info(str(ant.target.x) + "\n" + str(ant.target.y))
            log_info(str(ant.distance((ant.target.x, ant.target.y)) > ant.target.w))
            log_info(str(ant.r) + str(ant.l) + str(ant.u) + str(ant.d))
    
    
    
    pygame.display.flip()

if not(end_logged):
    end_log(st, stp)