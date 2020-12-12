import minimax as minimax
import display_functions as display_funcs
from random import choice

"""

 Functions dealing with the tic tac toe board.

"""


# Function that returns an empty tic tac toe board used to start a new game.
#
# @return a 2D array with dimensions 3x3 and every value is 0 where 0 
#         denotes an empty spot on the board and not an O value.
def return_empty_board():
	empty_board = [[0,0,0],
				   [0,0,0],
				   [0,0,0]]
	return empty_board

# Function that shows if the game is over by using the did_win() function
# to see if the player that made the last move won win that move.
#
# @param board_state [2D array of ints] which is the current board.
# @return is_over [boolean] which is true if the game is over
#         and false if not
def is_game_over(board_state):
	is_over = did_win(1, board_state) or did_win(-1, board_state)
	return is_over

# Function that shows the location of empty spaces remaining on the board.
#
# @param board_state [2D array of ints] which is the current board.
# @return empty_cells_list [2D array of ints] which is an array of 
#         location values on the board that currently do not have an X or O.
def empty_cells_on_board(board_state):
	empty_cells_list = []

	for x, row in enumerate(board_state):
		for y, cell in enumerate(row):
			if cell == 0:
				empty_cells_list.append([x, y])

	return empty_cells_list

# Function that shows if a player has won the game.
#
# @param player [int] which is a 1 for the user and -1 for the computer.
# @param board_state [2D array of ints] which is the current board.
# @return a boolean which is True if the player passed to the function 
#         has won the game. False if the player passed to the function 
#         has not won.
def did_win(player, board_state):
	win_state = [
		[board_state[0][0], board_state[0][1], board_state[0][2]],
		[board_state[1][0], board_state[1][1], board_state[1][2]],
		[board_state[2][0], board_state[2][1], board_state[2][2]],
		[board_state[0][0], board_state[1][0], board_state[2][0]],
		[board_state[0][1], board_state[1][1], board_state[2][1]],
		[board_state[0][2], board_state[1][2], board_state[2][2]],
		[board_state[0][0], board_state[1][1], board_state[2][2]],
		[board_state[2][0], board_state[1][1], board_state[0][2]],
	]

	if [player, player, player] in win_state:
		return True
	else:
		return False

# Function that makes sure a move is only made on empty positions by using
# the empty_cells_on_board() function.
#
# @param row [int] the row that a player is trying to move to
# @param column [int] the column that a player is trying to move to.
# @param board_state [2D array of ints] which is the current board.
# @return a boolean which is True if the location represents an empty space
#         on the board, and false if the location is already occupied
#         by an X or O.
def is_valid_move(row, column, board_state):
	if [row, column] in empty_cells_on_board(board_state):
		return True
	else:
		return False

# Function that places an X or O onto the board after checking if the move
# is valid with the is_valid_move() function.
#
# @param row [int] the row that a player is trying to move to
# @param column [int] the column that a player is trying to move to.
# @param board_state [2D array of ints] which is the current board.
# @param player [int] which is a 1 for the user and -1 for the computer.
# @return new_board_state [2D array of ints] which is the new board after
#         the new X or O has been placed. If the move is not valid return
#         the board_state value passed as parameter.
def set_move(row, column, player, board_state):
	if is_valid_move(row, column, board_state):
		new_board_state = board_state
		new_board_state[row][column] = player
		return new_board_state
	else:
		return board_state

# Function that handles how the computer takes its turn. Uses the minimax
# function from minimax.py to chose the best position, the 
# set_move() function to place the X or O on the board, is_game_over()
# to make sure the game has not ended, and clean() and render() from the 
# display_functions.py file.
#
# @param player_choice an X or O representing which value the user chose.
# @param computer_choice an X or O value representing the value with which
#        the computer is playing.
# @param board_state [2D array of ints] which is the current board.
# @return new_board_state [2D array of ints] which is the new board after
#         the new X or O has been placed. If the move is not valid return
#         the board_state value passed as parameter.
def ai_turn(player_choice, computer_choice, board_state):
	depth = len(empty_cells_on_board(board_state))

	if depth == 0 or is_game_over(board_state):
		return board_state

	display_funcs.clean()
	display_funcs.render(board_state, player_choice, computer_choice)

	if depth == 9:
		row = choice([0, 1, 2])
		column = choice([0, 1, 2])
	else:
		move = minimax.minimax(board_state, depth, -1)
		row, column = move[0], move[1]

	new_board_state = set_move(row, column, -1, board_state)
	return new_board_state

# Function that handles how the user takes their turn.
#
# @param player_choice an X or O representing which value the user chose.
# @param computer_choice an X or O value representing the value with which
#        the computer is playing.
# @param board_state [2D array of ints] which is the current board.
# @return new_board_state [2D array of ints] which is the new board after
#         the new X or O has been placed. If the move is not valid return
#         the board_state value passed as parameter.
def player_turn(player_choice, computer_choice, board_state):
	depth = len(empty_cells_on_board(board_state))

	if depth == 0 or is_game_over(board_state):
		return board_state

	moves = {1: [0, 0], 2: [0, 1], 3: [0, 2],
			 4: [1, 0], 5: [1, 1], 6: [1, 2],
			 7: [2, 0], 8: [2, 1], 9: [2,2]}
	display_funcs.clean()
	display_funcs.render(board_state, player_choice, computer_choice)
	move = -1
	while move < 1 or move > 9:
		try:
			move = int(input('Choose a position on the board between 1 and 9: '))
			board_position = moves[move]
			if is_valid_move(board_position[0], board_position[1], board_state):
				new_board_state = set_move(board_position[0], board_position[1], 1, board_state)
				return new_board_state
			else:
				print('Invalid move')
				move = -1

		except (EOFError, KeyboardInterrupt):
			print('Exiting')
			exit()
		except (KeyError, ValueError):
			print('Error: bad choice')
