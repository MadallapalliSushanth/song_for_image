import pygame
from time import sleep
pygame.init()
window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
#first image will display
image = pygame.image.load('hallowin.jpg')
window.blit(image, (0,0))
pygame.display.update()
sleep(4)
#then second music will paly after 3seccods
pygame.mixer.init()
pygame.mixer.music.load('horror-nightmare.mp3')
pygame.mixer.music.play()
sleep(6)
print("hallowin done")
