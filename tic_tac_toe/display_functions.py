import platform
from os import system

"""
 Functions to handle the rendering of the board in the terminal,
 and ensuring that the terminal doesn't become cluttered with boards
 other than the board representing the most recent state of the game.
"""

# Function that cleans up the terminal to avoid having too many boards
# visible at the same time. 
#
# Takes no parameters and returns nothing. Only cleans things up.
def clean():
	os_name = platform.system().lower()
	if 'windows' in os_name:
		system('cls')
	else:
		system('clear')

# Function that handles printing the board representing the current state
# of the game.
#
# @param board_state [2D array of ints] which is the current board.
# @param player_choice an X or O representing which value the user chose.
# @param computer_choice an X or O value representing the value with which
#        the computer is playing.
# Returns nothing. Only prints the current board. 
def render(board_state, player_choice, computer_choice):
	chars = {
		-1: player_choice,
		+1: computer_choice,
		0: ' '
	}
	str_line = '---------------'

	print('\n' + str_line)
	for row in board_state:
		for cell in row:
			symbol = chars[cell]
			print(f'| {symbol} |', end='')

		print('\n' + str_line)