'''
Game of Life
Martin A. Aaberge
Modified by Melvin to work on the CZ2020 and Pixel badge
'''

from .board import Board
import time

def main():
    # create a board:
    game_of_life_board = Board(8, 32)

    # run the first iteration of the board:
    game_of_life_board.draw_board()

    while True:
        game_of_life_board.update_board()
        if (game_of_life_board.draw_board()):
            game_of_life_board.generate_board()
        time.sleep_ms(100) # refresh time


main()
