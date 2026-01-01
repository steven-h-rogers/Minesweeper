import pygame
from Game import Game

pygame.init()
screen = pygame.display.set_mode((32*100,32*100))
# TODO: create another class that Preloads all of the constant data and stores it in memory.
game = Game((50,50), 50)


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()