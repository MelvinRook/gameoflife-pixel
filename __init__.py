'''
Game of Life
Martin A. Aaberge
Modified by Melvin to work on the CZ2020 badge
'''

from .board import Board
import time

def main():
    # create a board:
    game_of_life_board = Board(4, 4)

    # run the first iteration of the board:
    game_of_life_board.draw_board()

    while True:
        game_of_life_board.update_board()
        if (game_of_life_board.draw_board()):
            game_of_life_board.generate_board()
        time.sleep_ms(1200) # refresh time


main()
