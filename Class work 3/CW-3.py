import pygame
 
FPS = 60
W = 700  # ширина екрана
H = 300  # висота екрана
WHITE = (255, 255, 255)
BLUE = (0, 70, 225)
RIGHT = "to the right"
LEFT = "to the left"
STOP = "stop"
pygame.init()
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
 
# координати і радіус круга
x = W // 2
y = H // 2
r = 50

H_Rad=25
 
motion = STOP
 
while 1:
    sc.fill(WHITE)
 
    pygame.draw.circle(sc, BLUE, (x, y), r)
 
    pygame.display.update()
 
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                motion = LEFT
                if x<2*H_Rad:
                   x= W-H_Rad
            elif i.key == pygame.K_RIGHT:
                motion = RIGHT
                if x>(W-H_Rad):
                   x= H_Rad
        elif i.type == pygame.KEYUP:
            if i.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                motion = STOP
 
    if motion == LEFT:
        x -= 3
    elif motion == RIGHT:
        x += 3
 
    clock.tick(FPS)