import sys, pygame

pygame.init()

size = width, height = 800, 600
screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.bmp")
ballrect = ball.get_rect()
color1 = (100, 10, 0)
color2 = (70, 100,10)

speed = [1, 1]

def traspaso_area(r):
    if r.x + r.w>width:
        return True
    if r.x <0:
        return True
    if r.y + r.h>height:
        return True
    if r.y <0:
        return True
    return False

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_q: sys.exit()

    keystate = pygame.key.get_pressed()

    if keystate[pygame.K_UP]:    ballrect = ballrect.move([0, 1])
    if keystate[pygame.K_DOWN]:  ballrect = ballrect.move([0, -1])
    if keystate[pygame.K_LEFT]:  ballrect = ballrect.move([1, 0])
    if keystate[pygame.K_RIGHT]: ballrect = ballrect.move([-1, 0])

    if traspaso_area(ballrect):
        screen.fill(color1)
    else:
        screen.fill(color2)

    screen.blit(ball, ballrect)
    pygame.display.flip()
