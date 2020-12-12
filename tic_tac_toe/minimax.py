import board_functions as board_funcs
from math import inf

"""
 Functions that handle how the computer decides where to place its
 X or O using the minimax algorithm to make the best choice which will
 always result in either a draw or a win for the computer.
"""

# Function the computer uses to make score a possible move 
# based on whether or not the move results in a win, lose, or draw 
# for the computer.
# Uses the did_win() function from the board_functions.py file.
# 
# @param board_state [2D array of ints] which is the current board.
# @return score [int] which is -1 if the player wins, 1 if the computer wins,
#         and 0 if there is a draw.
def evaluate(board_state):
	if board_funcs.did_win(-1, board_state):
		score = 1
	elif board_funcs.did_win(1, board_state):
		score = -1
	else:
		score = 0

	return score

# Function that implements the minimax algorithm which goes through 
# and scores every possible move that can be made and chooses the move which
# has the best score.
# Uses the is_game_over(), and empty_cells_on_board() functions 
# from the board_functions.py file.
#
# @param board_state [2D array of ints] which is the current board.
# @param depth [int] which is the number of empty cells on the current board.
# @param player [int] which is a 1 for the user and -1 for the computer.
# @return best [array of ints] in which the first value is the best row,
#         the second value is the best column, 
#         and the third value is the best score.
def minimax(board_state, depth, player):
	if player == -1:
		best = [-1, -1, -inf]
	else:
		best = [-1, -1, inf]

	if depth == 0 or board_funcs.is_game_over(board_state):
		score = evaluate(board_state)
		return [-1, -1, score]

	for cell in board_funcs.empty_cells_on_board(board_state):
		row, column = cell[0], cell[1]
		board_state[row][column] = player
		score = minimax(board_state, depth -1, -player)
		board_state[row][column] = 0
		score[0], score[1] = row, column

		if player == -1:
			if score[2] > best[2]:
				best = score
		else:
			if score[2] < best[2]:
				best = score

	return best