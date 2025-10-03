import pygame

pygame.init()

screen_dim = 1080
screen = pygame.display.set_mode((screen_dim, screen_dim)) # set display screen
clock = pygame.time.Clock()
running = True

bg = pygame.image.load('fishing_bg.png')
bg = bg.convert_alpha() # better read on transparency

cat = pygame.image.load('default_kitty.png')
cat = cat.convert_alpha() # better read on transparency

def background_img(image): # function = def
    size = pygame.transform.scale(bg, (screen_dim, screen_dim))
    screen.blit(size, (0,0)) 
def kitty_spawn(image):
    size = pygame.transform.scale(cat, (screen_dim, screen_dim))
    screen.blit(size, (0,0)) # render sprite at size at coordinates (0,0)

        
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

    background_img(bg) 
    kitty_spawn(cat)
    pygame.display.update()# do this after function call to render sprite
    
    clock.tick(60)