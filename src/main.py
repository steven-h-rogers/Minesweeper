import pygame
import Game

pygame.init()
screen = pygame.display.set_mode((32*100,32*100))


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()