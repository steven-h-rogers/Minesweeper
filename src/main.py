import pygame, sys
import Constants
from Board import Board
from MapGenerator import MapGenerator



pygame.init()

# TODO: Make the screen zoomable and moveable a bit
# TODO: Fix bug where user can click off the right and left hand side of the board and still activate tiles
screen = pygame.display.set_mode((50*32,50*32), pygame.SCALED | pygame.FULLSCREEN)
clock = pygame.time.Clock()

# TODO: add a main menu/deathscreen where user can pick dimensions and num_bombs
def generate_new_game(dimensions=(50,50), num_bombs=250):
    map_gen = MapGenerator(dimensions, num_bombs)
    board = Board(map_gen.get_display_map(), num_bombs, screen)
    return board


board = generate_new_game(dimensions=(5,5), num_bombs=2)

running = True
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or running == False:
            print('quitting')
            pygame.quit()
            sys.exit()
        
        # TODO: cleanup the gameloop by implementing an eventhandler object?
        if event.type == pygame.MOUSEBUTTONDOWN:
            raw_x_pos, raw_y_pos = pygame.mouse.get_pos()
            board_x_pos, board_y_pos = raw_x_pos//Constants.TILE_SIZE, raw_y_pos//Constants.TILE_SIZE
            print(raw_x_pos, raw_y_pos, board_x_pos, board_y_pos)
            if board_x_pos in range(0, board.cols) and board_y_pos in range(0, board.rows):
                if event.button == 1:
                    if board.handle_l_click(board_x_pos, board_y_pos) == 'GAME OVER':
                        game_over = True
                        print("GAME OVER")
                if event.button == 3:
                    print('right click')
                    board.handle_r_click(board_x_pos, board_y_pos)
                if board.check_for_win() == 'YOU WON':
                    print("YOU WON!")
                    game_over = True
            else: print("not in range")
        if event.type == pygame.KEYDOWN:
            if game_over == True and event.key == pygame.K_r:
                board = generate_new_game()
            if event.key == pygame.K_q:
                running = False
    

    board.render_board()
    



    pygame.display.flip()
    clock.tick(30)