"""
Mini-max Tic-Tac-Toe Player
"""

import poc_ttt_gui
import poc_ttt_provided as provided

# Set timeout, as mini-max can take a long time
import codeskulptor
codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

def mm_move(board, player):
    """
    Make a move on the board.
    
    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    if board.check_win() != None: 
        return SCORES[board.check_win()], (-1, -1)
    
    else:
        empty_squares = board.get_empty_squares()                
        if player == provided.PLAYERX:
            best_score_x = -1
            best_move = ()
            for square in empty_squares:
                board_clone = board.clone()
                board_clone.move(square[0], square[1], player)           
                score, _ = mm_move(board_clone, provided.PLAYERO)
                if score == SCORES[provided.PLAYERX]: 
                    return SCORES[provided.PLAYERX], (square[0], square[1])
                elif score > best_score_x:
                    best_score_x = score
                    best_move = (square[0], square[1])
            return best_score_x , best_move 
        if player == provided.PLAYERO:
            best_score_o = 1
            best_move = ()
            for square in empty_squares:
                board_clone = board.clone() 
                board_clone.move(square[0], square[1], player)
                score, _ = mm_move(board_clone, provided.PLAYERX)
                if score == SCORES[provided.PLAYERO]:
                    return SCORES[provided.PLAYERO], (square[0], square[1])
                elif score < best_score_o:
                    best_score_o = score
                    best_move = (square[0], square[1])
            return best_score_o, best_move

            
            

            
def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

#provided.play_game(move_wrapper, 1, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)
