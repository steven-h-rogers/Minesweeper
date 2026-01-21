import pygame, sys
from Game import Game

pygame.init()
screen = pygame.display.set_mode((50*32,50*32), pygame.SCALED | pygame.FULLSCREEN)
clock = pygame.time.Clock()
game = Game((50,50), 175, screen)


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            running = False
    pygame.display.flip()
    clock.tick(30)