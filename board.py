
'''
Game of Life
Board Class
Martin A. Aaberge
Modified by Melvin to work on the CZ2020 badge
'''

from .cell import Cell
from time import time
from random import randint, seed, choice
import display

class Board:
    def __init__(self , rows , columns):
        '''
        constructor holds input from user and populates the grid with cells. 
        '''
        self._colour = 0x00FF00
        self._colours = [0x00FF00,0x0000FF,0xFF0000,0xB8E986,0xF8B700,0x50E3C2,0xFE13D4,0x9013FE]
        self._state = "0000000000000000"
        self._rows = rows
        self._columns = columns   
        self._grid = [[Cell() for column_cells in range(self._columns)] for row_cells in range(self._rows)]

        self.generate_board()

    def draw_board(self):
        '''
        method that draws the actual board in the terminal
        '''
        state = ""
        
        print('\n'*2)
        print('printing board')
        for row_no, row in enumerate(self._grid):
            for col_no, column in enumerate(row):
                #print ('debug: ',col_no, row_no)
                if (column.get_print_character()):
                    display.drawPixel(col_no, row_no, self._colour)
                    state + "1"
                else:
                    display.drawPixel(col_no, row_no, 0x000000)
                    state + "0"
                    
                print (column.get_print_character(),end='')
            print () # to create a new line pr. row.
            
        display.flush() # write to framebuffer
        
        # Check state
        result = (state == self._state)
        
        # Save state for next iteration
        self._state = state
        
        return result

    def generate_board(self):
        '''
        method that sets the random state of all cells.
        '''
        # select next colour
        self._colour = choice(self._colours)
        
        # improve randomness (taken from Simon Says)
        seed( int( 1000000 * time() ) % 1000000)

        for row in self._grid:
            for column in row:
                # there is a 33% chance the cells spawn alive.
                chance_number = randint(0,2)
                if chance_number == 1:
                    column.set_alive()

    def update_board(self):
        '''
        method that updates the board based on
        the check of each cell pr. generation
        '''
        #cells list for living cells to kill and cells to resurrect or keep alive
        goes_alive = []
        gets_killed = []

        for row in range(len(self._grid)):
            for column in range(len(self._grid[row])):
                #check neighbour pr. square:
                check_neighbour = self.check_neighbour(row , column)
                
                living_neighbours_count = []

                for neighbour_cell in check_neighbour:
                    #check live status for neighbour_cell:
                    if neighbour_cell.is_alive():
                        living_neighbours_count.append(neighbour_cell)

                cell_object = self._grid[row][column]
                status_main_cell = cell_object.is_alive()

                #If the cell is alive, check the neighbour status.
                if status_main_cell == True:
                    if len(living_neighbours_count) < 2 or len(living_neighbours_count) > 3:
                        gets_killed.append(cell_object)

                    if len(living_neighbours_count) == 3 or len(living_neighbours_count) == 2:
                        goes_alive.append(cell_object)

                else:
                    if len(living_neighbours_count) == 3:
                        goes_alive.append(cell_object)

        #sett cell statuses
        for cell_items in goes_alive:
            cell_items.set_alive()

        for cell_items in gets_killed:
            cell_items.set_dead()

    
    
    def check_neighbour(self, check_row , check_column):
        '''
        method that checks all the neighbours for all the cells
        and returns the list of the valid neighbours so the update 
        method can set the new status
        '''        
        #how deep the search is:
        search_min = -1
        search_max = 2

        #empty list to append neighbours into.
        neighbour_list = []
        for row in range(search_min,search_max):
            for column in range(search_min,search_max):
                neighbour_row = check_row + row
                neighbour_column = check_column + column 
                
                valid_neighbour = True

                if (neighbour_row) == check_row and (neighbour_column) == check_column:
                    valid_neighbour = False

                if (neighbour_row) < 0 or (neighbour_row) >= self._rows:
                    valid_neighbour = False

                if (neighbour_column) < 0 or (neighbour_column) >= self._columns:
                    valid_neighbour = False

                if valid_neighbour:
                    neighbour_list.append(self._grid[neighbour_row][neighbour_column])
        return neighbour_list

