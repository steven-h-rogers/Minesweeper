import pygame, sys
from Game import Game
import Constants


pygame.init()
screen = pygame.display.set_mode((50*32,50*32), pygame.SCALED | pygame.FULLSCREEN)
clock = pygame.time.Clock()
game = Game((50,50), 300, screen)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                raw_x_pos, raw_y_pos = pygame.mouse.get_pos()
                board_x_pos, board_y_pos = raw_x_pos//Constants.TILE_SIZE, raw_y_pos//Constants.TILE_SIZE
                game.board.board[board_y_pos][board_x_pos].reveal()


    pygame.display.flip()
    clock.tick(30)