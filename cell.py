'''
Game of Life
Cell class
Martin A. Aaberge
Modified by Melvin to work on the CZ2020 and Pixel badge
'''

class Cell:
    def __init__(self):
        '''
        Class holding init status of cell (dead).
        Ability to set- and fetch new statuses with functions
        '''
        self._status = 'Dead'

    def set_dead(self):
        '''
        method sets the cell status to DEAD
        '''
        self._status = 'Dead'

    def set_alive(self):
        '''
        method sets the cell status to ALIVE
        '''
        self._status = 'Alive'

    def is_alive(self):
        '''
        method checks if the cell is ALIVE
        returns True if it is alive, False if not.
        '''
        if self._status == 'Alive':
            return True
        return False

    def get_print_character(self):
        '''
        method returning a status character of our choice to print on the board
        '''
        if self.is_alive():
            return 1
        return 0
