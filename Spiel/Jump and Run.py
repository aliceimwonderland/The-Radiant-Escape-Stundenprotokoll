import pygame
from sys import exit 

pygame.init()

screen = pygame.display.set_mode((900,700))
pygame.display.set_caption('Jump and Run')
clock = pygame.time.Clock()

colour_surface = pygame.Surface((900,100))
colour_surface.fill('burlywood4')
surface_part2 = pygame.Surface((900,20))
surface_part2.fill('burlywood3')
surface_himmel = pygame.Surface((900,580))
surface_himmel.fill('cornsilk3')

character = pygame.image.load('Bilder/character.png')
character_rect = character.get_rect(topleft = (200,500))
character_gravity = 0
character_right = 0
character_left = 0
vel = 1


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

                             
    screen.blit(colour_surface,(0,600))
    screen.blit(surface_part2,(0,500))
    screen.blit(surface_himmel,(0,0))

    character_gravity += 1
    character_rect.y += character_gravity
    character_rect.x += character_right
    character_rect.x += character_left

    if character_rect.bottom >= 580: character_rect.bottom = 580
    screen.blit(character,character_rect)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        character_gravity = -10 
    elif keys[pygame.K_d]:
        character_right = +1
    elif keys[pygame.K_a]:
        character_left = -1

    

    pygame.display.update()
    clock.tick(60)

  