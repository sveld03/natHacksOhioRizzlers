import pygame

guess = 7

image = pygame.image.load("images/thispersondoesnotexist-" + str(guess+20) + ".com.jpeg")

# Init pygame
pygame.init()
screen = pygame.display.set_mode((1920, 1080))

req = False;
while(not req):

    screen.fill((0, 0, 0))
    screen.blit(image, (460,40))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key== pygame.K_RETURN:
                req = True;