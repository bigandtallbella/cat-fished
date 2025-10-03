import pygame

pygame.init()

screen_dim = 1080
screen = pygame.display.set_mode((screen_dim, screen_dim))
clock = pygame.time.Clock()
running = True

while running:

    keyDown = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()
        if keyDown[pygame.K_ESCAPE]:
            running = False
            pygame.quit()
            print("Hit any key to quit")
            exit()
    screen.fill("white")

    pygame.display.update()

    clock.tick(60)