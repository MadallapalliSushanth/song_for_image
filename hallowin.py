import pygame
from time import sleep
pygame.init()
window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
image = pygame.image.load('hallowin.jpg')
window.blit(image, (0,0))
pygame.display.update()
sleep(10)
