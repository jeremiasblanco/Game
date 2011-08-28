import sys, pygame

pygame.init()

size = width, height = 800, 600
screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.bmp")
ballrect = ball.get_rect()

speed = [1, 1]

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_q: sys.exit()

    keystate = pygame.key.get_pressed()

    if keystate[pygame.K_UP]:    ballrect = ballrect.move([0, -1])
    if keystate[pygame.K_DOWN]:  ballrect = ballrect.move([0, 1])
    if keystate[pygame.K_LEFT]:  ballrect = ballrect.move([-1, 0])
    if keystate[pygame.K_RIGHT]: ballrect = ballrect.move([1, 0])

    screen.fill([128, 0, 0])
    screen.blit(ball, ballrect)
    pygame.display.flip()
