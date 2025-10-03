import pygame

pygame.init()

screen_dim = 1080
screen = pygame.display.set_mode((screen_dim, screen_dim)) # set display screen
clock = pygame.time.Clock()
running = True

bg = pygame.image.load('fishing_bg.png')
bg = bg.convert_alpha() # better read on transparency

still_cat = pygame.image.load('default_kitty.png')
still_cat = still_cat.convert_alpha() # better read on transparency

def background_img(image): # function = def
    size = pygame.transform.scale(image, (screen_dim, screen_dim))
    screen.blit(size, (0,0)) 
def kitty_spawn(image):
    size = pygame.transform.scale(image, (screen_dim, screen_dim))
    screen.blit(size, (0,0)) # render sprite at size at coordinates (0,0)


#comeback to switch between idles and whatnot
# class Player():

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
    
    if pygame.time.get_ticks() % 500 == 9:
        print("fishy fishy")
        #pygame.time.wait(1)
        b1 = pygame.image.load('cat_blink1.png')
        b2 = pygame.image.load('cat_blink2.png')
        b3 = pygame.image.load('cat_blink3.png')
        b4 = pygame.image.load('cat_blink4.png')
        blink_sequence = [b1, b2, b3, b4]
        for img in blink_sequence:
            kitty_spawn(img)
            pygame.display.update()
            pygame.time.wait(400)
        pygame.time.wait(900)
        kitty_spawn(b3)
        pygame.display.update()
        pygame.time.wait(400)
        kitty_spawn(b4)
        pygame.display.update()
        pygame.time.wait(2800)

    background_img(bg)
    kitty_spawn(still_cat)
    pygame.display.update()
    #pygame.display.update()# do this after function call to render sprite
    
    clock.tick(60)