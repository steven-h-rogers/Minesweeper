import pygame, sys
import Constants
from Board import Board
from MapGenerator import MapGenerator



pygame.init()


screen = pygame.display.set_mode((50*32,50*32), pygame.SCALED | pygame.FULLSCREEN)
clock = pygame.time.Clock()

dimensions = (50,50)
num_bombs = 250

map_gen = MapGenerator(dimensions, num_bombs)
board = Board(map_gen.get_display_map(), screen)

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
                board.handle_l_click(board_x_pos, board_y_pos)
            if event.button == 3:
                print('right click')
                raw_x_pos, raw_y_pos = pygame.mouse.get_pos()
                board_x_pos, board_y_pos = raw_x_pos//Constants.TILE_SIZE, raw_y_pos//Constants.TILE_SIZE
                board.handle_r_click(board_x_pos, board_y_pos)

    board.render_board()
    



    pygame.display.flip()
    clock.tick(30)