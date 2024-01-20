import os

print(os.listdir(os.getcwd() + '/Animation'))
anim_list = os.listdir(os.getcwd() + '/Animation')
anim_list.reverse()
print(anim_list)


import pygame

pygame.init()

infoObject = pygame.display.Info()
width, height = infoObject.current_w, infoObject.current_h
win = pygame.display.set_mode((width, height))

alp = []
for e in anim_list:
    alp.append(pygame.image.load("Animation/" + e))

didle = pygame.image.load("idle/bandit.png")

for i in range(len(alp)):
    if height > width:
        alp[i] = pygame.transform.scale(alp[i], (width//4, width//4))
    else:
        alp[i] = pygame.transform.scale(alp[i], (height//4, height//4))

if height > width:
    didle = pygame.transform.scale(didle, (width//4, width//4))
else:
    didle = pygame.transform.scale(didle, (height//4, height//4))


running = True
counter = 0
clock = pygame.time.Clock()
while running:
    win.fill((30, 150, 70))
    clock.tick(30)
    
    if int(counter) < len(alp):
        win.blit(alp[int(counter)], (width//4, height//4))
        counter += 0.5
    elif counter > len(alp) + 30:
        win.blit(didle, (width//4, height//4))
        counter = 0
    else:
        win.blit(didle, (width//4, height//4))
        counter += 1
    pygame.display.flip()