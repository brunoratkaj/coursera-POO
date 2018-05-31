"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 100         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player

# Constants
#EMPTY = 1
#PLAYERX = 2
#PLAYERO = 3 
#DRAW = 4

# Add your functions here.
def mc_trial(board, player):
    """ 
    This function takes a current board and the next player to move.
    """
    current_player = player
    win = False
    while not win:
        empty_squares = board.get_empty_squares()
        #print empty_squares
        #print board
        square_coord = random.choice(empty_squares)
        board.move(square_coord[0], square_coord[1], current_player)
        if board.check_win():
            win = True
            #print 'Win \n', board
            return
            #print board
            #print board.check_win()
            #return board
        else:
            current_player = provided.switch_player(current_player)
            

def mc_update_scores(scores, board, player):
    """ 
    This function takes a grid of scores (a list of lists) with the same dimensions as the Tic-Tac-Toe board, 
    a board from a completed game, and which player the machine player is.
    """
    board_dim = board.get_dim()
    winner = board.check_win()
    if winner == provided.DRAW:
        pass
    else:
        for row in range(board_dim):
            for col in range(board_dim):
                if winner == player:
                    square = board.square(row, col)
                    if square == player:
                        scores[row][col] += SCORE_CURRENT
                    elif square == provided.EMPTY:
                        pass
                    else:
                        scores[row][col] -= SCORE_OTHER
                else:
                    square = board.square(row, col)
                    if square == player:
                        scores[row][col] -= SCORE_CURRENT
                    elif square == provided.EMPTY:
                        pass
                    else:
                        scores[row][col] += SCORE_OTHER


def get_best_move(board, scores):
    """ 
    This function takes a current board and a grid of scores. 
    """
    empty_squares = board.get_empty_squares()
    moves_score = []
    best_moves = []
    for coord in empty_squares:
        moves_score.append(scores[coord[0]][coord[1]])       
    best_move_score = max(moves_score) 
    for coor in empty_squares:
        if scores[coor[0]][coor[1]] == best_move_score:
            best_moves.append((coor[0],coor[1]))       
    return random.choice(best_moves)
        

def mc_move(board, player, trials):
    """ 
    This function takes a current board, which player the machine player is, and the number of trials to run
    """
    score_list = [[0 for dummy_col in range(board.get_dim())] for dummy_row in range(board.get_dim())]   
    for dummy in range(trials):  
        starting_board = board.clone()
        mc_trial(starting_board, player)
        mc_update_scores(score_list, starting_board, player)
        #print 'NUM', dummy
    return get_best_move(board, score_list)
        
        
        
    
    
    
    
#score = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]        
#mc_trial(provided.TTTBoard(3), provided.PLAYERX)  
#mc_update_scores(score, mc_trial(provided.TTTBoard(3), provided.PLAYERX), provided.PLAYERX)
#print score
#print get_best_move(provided.TTTBoard(3), [[1, 0, 3], [0, 0, 3], [0, 2, 3]])
#print mc_move(provided.TTTBoard(3), provided.PLAYERX, NTRIALS) 

#provided.play_game(mc_move, NTRIALS, False)        
#poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
