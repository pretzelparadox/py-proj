# Program: Hangman: Pokemon Edition
# Start Date: 1/25/22
# End Date: ???
'''
**************************
*-----H-A-N-G-M-A-N------*
*------------------------*
*----=========-----------*
*----| |=====|-----------*
*----| |----VVV----------*
*----| |---(O_0)---------*
*----| |---o-|-o---------*
*----| |-----|-----------*
*----| |----/-\----------*
*----| |-----------------*
*---==============-------*
*--_ _ _ _ _ _ _ _ _ _---*
*------------------------*
*------------------------*
**************************
'''
# constraints
# max word length = 10
import random
# store words in a array
words = ['Bulbasaur', 'Ivysaur', 'Venusaur', 'Charmander', 'Charmeleon',
        'Charizard']
#random_word = words[random.randrange(len(words))]
# ***** testing bulbasaur
rand_w = words[0]
W_LEN = len(rand_w)
choice = 'Y' 
W_IDX = 12
# word count limit: 1 - 10. indices: 0-9
blank_tiles = [
'*-----------_------------*',
'*----------_ _-----------*',
'*---------_ _ _----------*',
'*--------_ _ _ _---------*',
'*-------_ _ _ _ _--------*',
'*------_ _ _ _ _ _-------*',
'*-----_ _ _ _ _ _ _------*',
'*----_ _ _ _ _ _ _ _-----*',
'*---_ _ _ _ _ _ _ _ _----*',
'*--_ _ _ _ _ _ _ _ _ _---*'
        ]
# empty, 1. head, 2. body, 3. left leg, 4. right leg, 
# 5. left arm, 6. right arm
board = [
'**************************',
'*-----H-A-N-G-M-A-N------*',
'*------------------------*',
'*----=========-----------*',
'*----| |=====|-----------*',
'*----| |-----------------*',
'*----| |-----------------*',
'*----| |-----------------*',
'*----| |-----------------*',
'*----| |-----------------*',
'*----| |-----------------*',
'*---==============-------*',
'*--_ _ _ _ _ _ _ _ _ _---*',
'*------------------------*',
'*------------------------*',
'**************************'
]

BOARD_R_LEN = len(board[0])
lives = [
''' 
*----| |----VVV----------*
*----| |---(O_0)---------*
''',
''' 
*----| |-----|-----------*
*----| |-----|-----------*
''', 
''' 
*----| |---o-|-----------*
''', 
''' 
*----| |---o-|-o---------*
''', 
''' 
*----| |----/------------*
''', 
''' 
*----| |----/-\----------*
'''] 

# prompt user to play new game
while choice is 'N':
    choice = input('Ready to play Hangman? (Y/N))\n')

# start a new game
print('Game Started.')
# random generate a word from word array
#print('random word', rand_w)
#print('word length', W_LEN)
#print('underscores row length', len(blank_tiles[0]))
#print('game_board row length', len(board[0]))

# note: row index 12 contains word insertion location

# change word count on the board
# modify the board based on word length
board[W_IDX] = blank_tiles[W_LEN - 1]

# print empty board
for row in board:
    print(row)


# prompt user to input a letter guess
guess = input('Guess a letter (A-Z):\n')

# if random_word contains that letter, fill in underscore locations

# ****example test case:*****
# random_word: bulbasaur
# word length: 9
# first guess: a
# fill in index: 4, 6 with letter a





# iterate through letters of bulbasaur
for letter_idx in range(0, len(rand_w)):
    if guess is rand_w[letter_idx]:
        # idx = 4 is bulbAsaur
        # idx = 12 is A insert loc
        # first loc = 
       # print('phase: correct guess')
        first_loc = (BOARD_R_LEN - (W_LEN * 2)) / 2
        first_loc = int(first_loc)
        ins_i = first_loc + (letter_idx * 2)
       # print('first index tile loc', first_loc)
        board[W_IDX] = board[W_IDX][:ins_i] + guess + board[W_IDX][ins_i+1:]
       # print('modded word row', board[W_IDX])


# else draw a body part
for row in board:
    print(row)






# reset the game
# randomly select a word for current game 
# have a certain amount of "lives"
# draw a limb (wrong letter guess)
# reveal an underscore (correct letter guess)
