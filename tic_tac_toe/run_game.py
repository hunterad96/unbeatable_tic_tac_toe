import board_functions as board_funcs
import display_functions as display_funcs
import time

"""
 Function that uses functions from board_functions.py and 
 display_functions.py to play the game.
"""

def run_game():
	player = 1
	computer = -1
	board = board_funcs.return_empty_board()
	player_choice = ''
	computer_choice = ''
	player_first_Y_or_N = ''

	while player_choice != 'O' and player_choice != 'X':
		try:
			player_choice = input('Choose X or O:\nChoice: ').upper()
		except(EOFError, KeyboardInterrupt):
			print('Exiting')
			exit()
		except(KeyError, ValueError):
			print('Error: bad choice')

	if player_choice == 'X':
		computer_choice = 'O'
	else:
		computer_choice = 'X'

	display_funcs.clean()
	while player_first_Y_or_N != 'Y' and player_first_Y_or_N != 'N':
		try:
			player_first_Y_or_N = input('Do you want to go first? Choose Y or N:\nChoice: ').upper()
		except (EOFError, KeyboardInterrupt):
			print('Exiting')
			exit()
		except (KeyError, ValueError):
			print('Error: bad choice')

	while len(board_funcs.empty_cells_on_board(board)) > 0 and not board_funcs.is_game_over(board):
		if player_first_Y_or_N == 'N':
			board = board_funcs.ai_turn(player_choice, computer_choice, board)
			player_first_Y_or_N = ''

		board = board_funcs.player_turn(player_choice, computer_choice, board)
		board = board_funcs.ai_turn(player_choice, computer_choice, board)
		time.sleep(1)

	if board_funcs.did_win(player, board):
		print('You win')
	elif board_funcs.did_win(computer, board):
		print('You lose')
	else:
		print('Draw')

	
	exit()

run_game()
