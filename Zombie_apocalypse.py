"""
Student portion of Zombie Apocalypse mini-project
"""

import random
import poc_grid
import poc_queue
import poc_zombie_gui

# global constants
EMPTY = 0 
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = 5
HUMAN = 6
ZOMBIE = 7


class Apocalypse(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list = None, 
                 zombie_list = None, human_list = None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)  
        else:
            self._human_list = []
        
    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        poc_grid.Grid.clear(self)
        self._zombie_list = []
        self._human_list = []
        
    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row,col))
        #print self.compute_distance_field(ZOMBIE)       
    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)       
          
    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        for zombie in self._zombie_list:
            yield zombie       

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row, col))
        #print self.compute_distance_field(HUMAN)
        
    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)
    
    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        for human in self._human_list:
            yield human
        
    def compute_distance_field(self, entity_type):
        """
        Function computes and returns a 2D distance field
        Distance at member of entity_list is zero
        Shortest paths avoid obstacles and use four-way distances
        """
        visited = [[EMPTY for dummy_col in range(self._grid_width)]\
                   for dummy_row in range(self._grid_height)]
        distance_field = [[self._grid_width * self._grid_height \
                          for dummy_col in range(self._grid_width)]\
                          for dummy_row in range(self._grid_height)]                          
        boundary = poc_queue.Queue()
        if entity_type == HUMAN:
            for human in self._human_list:                
                boundary.enqueue(human)
        elif entity_type == ZOMBIE:
            for zombie in self._zombie_list:                
                boundary.enqueue(zombie)
        for item in boundary.__iter__():
            visited[item[0]][item[1]] = FULL
            distance_field[item[0]][item[1]] = 0
        while boundary.__len__() != 0:
            current_cell = boundary.dequeue()
            neighbors = self.four_neighbors(current_cell[0], current_cell[1])
            for neighbor in neighbors:
                if visited[neighbor[0]][neighbor[1]] == EMPTY:
                    visited[neighbor[0]][neighbor[1]] = FULL
                    boundary.enqueue(neighbor)
                    distance_field[neighbor[0]][neighbor[1]] = \
                    distance_field[current_cell[0]][current_cell[1]] + 1
        return distance_field
            
    def move_humans(self, zombie_distance_field):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        human_list = []
        for human in self._human_list:
            best_move = ()
            moves = self.eight_neighbors(human[0], human[1])
            moves.append((human[0], human[1]))
            max_distance = 0
            for move in moves:
                if zombie_distance_field[move[0]][move[1]] > max_distance and self.is_empty(move[0],move[1]):
                    max_distance = zombie_distance_field[move[0]][move[1]]
                    best_move = move
            if best_move:  
                human_list.append(best_move)
        self._human_list = human_list
    def move_zombies(self, human_distance_field):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        zombie_list = []        
        for zombie in self._zombie_list:
            best_move = ()
            moves = self.four_neighbors(zombie[0], zombie[1])
            moves.append((zombie[0], zombie[1]))
            min_distance = float("inf")
            print moves
            alt_moves = []
            for move in moves:
                if self.is_empty(move[0],move[1]):
                    alt_moves.append(move)
            print alt_moves
            for move in alt_moves:                
                if human_distance_field[move[0]][move[1]] <= min_distance:
                    min_distance = human_distance_field[move[0]][move[1]]
                    best_move = move
            if best_move:        
                zombie_list.append(best_move)
        self._zombie_list = zombie_list

# Start up gui for simulation - You will need to write some code above
# before this will work without errors
#ap = Apocalypse(30, 40)
#ap.compute_distance_field(HUMAN)
poc_zombie_gui.run_gui(Apocalypse(30, 40))
