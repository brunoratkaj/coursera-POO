"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """   
    result = []
    index = 0
    merged = False
    for dummy in range(len(line)):
        result.append(0)
    for num in line:
        if num != 0 and index > 0 and num == result[index - 1]:
            result[index - 1] *= 2
            index += 1
            merged = True
        elif num != 0 and merged:
            result[index - 1] = num
            merged = False
        elif num != 0:            
            result[index] = num
            index += 1             
    return result

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self.rows = grid_height
        self.columns = grid_width
        self.grid = []
        self.direction_dict = {UP: [(0, dummy_col) for dummy_col in range(self.columns)], #UP
                              DOWN: [(self.rows - 1, dummy_col) for dummy_col in range(self.columns)], #DOWN 
                              LEFT: [(dummy_row, 0) for dummy_row in range(self.rows)] , #LEFT	
                              RIGHT: [(dummy_row, self.columns - 1) for dummy_row in range(self.rows)] #RIGHT	
        }
        self.reset()
    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self.grid = [[0 for dummy_col in range(self.columns)] for dummy_row in range(self.rows)] 
        self.new_tile()
        self.new_tile()
        
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        grid_str = ''
        for row in range(self.rows):
            grid_str += str(self.grid[row]) + '\n'
        return grid_str
        

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.rows

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.columns

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        direct = OFFSETS[direction]       
        initital = self.direction_dict[direction]
        new_grid = []
        if direction == UP or direction == DOWN:
            steps = self.columns
            line = self.rows
        elif direction == LEFT or direction == RIGHT:
            steps = self.rows
            line = self.columns
        for step in range(steps):
            temp_list = []
            for element in range(line):
                row = initital[step][0] + element * direct[0]
                col = initital[step][1] + element * direct[1]
                temp_list.append(self.grid[row][col])
            new_grid.append(merge(temp_list))
        print 'New grid', new_grid
        
        new_sorted_grid = []
        if direction == UP:
            for row in range(self.rows):
                row_list = []
                for col in range(self.columns):
                    row_list.append(new_grid[col][row])
                new_sorted_grid.append(row_list)
            if new_sorted_grid != self.grid:    
                self.grid = new_sorted_grid
                self.new_tile()
            
        elif direction == DOWN:
            for row in range(self.rows):
                row_list = []
                for col in range(self.columns):
                    row_list.append(new_grid[col][row])                
                new_sorted_grid.append(row_list)
            new_sorted_grid.reverse()
            #if new_sorted_grid != self.grid:
            if new_sorted_grid != self.grid:    
                self.grid = new_sorted_grid
                self.new_tile()
            

        
        elif direction == LEFT:
            if new_grid != self.grid:    
                self.grid = new_grid
                self.new_tile()
                        
            

            
        elif direction == RIGHT:
            for row in range(self.rows):
                new_grid[row].reverse()
            if new_grid != self.grid:    
                self.grid = new_grid
                self.new_tile()

            
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """      
        free = False
        while not free:
            row = random.randrange(0, self.rows)
            column = random.randrange(0, self.columns)
            if self.grid[row][column] == 0:
                free = True
        if random.randint(1, 10) == 10:
            tile = 4
            self.grid[row][column] = tile
        else:
            tile = 2
            self.grid[row][column] = tile
            print row,column
            print self.grid             

                
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self.grid[row][col]
    

#import user42_q0uxpBvVapx21UG as merge_testsuite
#merge_testsuite.run_suite(TwentyFortyEight(5, 4))

poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
