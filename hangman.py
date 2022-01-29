# Program: Hangman: Pokemon Edition
# Start Date: 1/25/22
# End Date: ???

import random

# store words in array
words = ['Bulbasaur', 'Ivysaur', 'Venusaur', 'Charmander', 'Charmeleon',
        'Charizard']
# random generate a word from word array
w_rand = words[random.randrange(len(words))] # random generated word from list ***** testing bulbasaur
W_LEN = len(w_rand) # length of chosen word
W_IDX = 12 # row which contains word on game board
revealed_count = 0
choice = 'Y' # player choice to start new game
lives_remaining = 6


# game board
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

# word row
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

# lives: head -> body -> legs x2  -> arms x2
# indices: head = 0,1; body = 2,3; 
# legL = 6; legR = 7;
# armL = 4; armR = 5

lives = [
'*----| |----VVV----------*', # head 0
'*----| |---(O_0)---------*', # head 1
'*----| |-----|-----------*', # body 2 
'*----| |---o-|-----------*', # armL 3
'*----| |---o-|-o---------*', # armR 4
'*----| |----/------------*', # legL 5
'*----| |----/-\----------*'  # legR 6
] 
BOARD_R_LEN = len(board[0])
board[W_IDX] = blank_tiles[W_LEN - 1] # mod board based on word length
# starting position for this rand word
first_loc = int((BOARD_R_LEN - (W_LEN * 2)) / 2)

# helper debug functions
def print_debug():
    # debug info
    print('Debug Info:')
    print('Random word:', w_rand)
    print('Word length:', W_LEN)
    print('Blank tiles row length:', len(blank_tiles[0]))
    print('Board row length:', len(board[0]))
    print('Word row', board[W_IDX])
    print('first index tile loc', first_loc)

def print_board():
    for row in board:
        print(row)
def draw_man():
    if lives_remaining == 6:
        # draw head; i = 5,6
        board[5] = lives[0]
        board[6] = lives[1]
    elif lives_remaining == 5:
        # draw body
        board[7] = lives[2]
        board[8] = lives[2]

    elif lives_remaining == 4:
        # draw left leg
        board[9] = lives[5]

    elif lives_remaining == 3:
        # draw right leg
        board[9] = lives[6]

    elif lives_remaining == 2:
        # draw left arm 
        board[7] = lives[3]

    elif lives_remaining == 1:
        # draw right arm 
        board[7] = lives[4]

# main menu: prompt user to play new game
while choice is 'N':
    choice = input('Ready to play Hangman? (Y/N))\n')

# new game has started
print('Game Started.')
print_board()

# keep asking for letter guesses
while lives_remaining > 0 and revealed_count is not W_LEN:
    # prompt user to input a letter guess
    guess = input('Guess a letter (A-Z):\n')
    
    if str(guess) in str(w_rand):
        # iterate through letters of bulbasaur (find insertion position)
        for char_idx in range(0, W_LEN):
            curr_letter = w_rand[char_idx].lower()
            # if random_word contains that letter
            if guess  ==  curr_letter:
                # insertion location for chosen letter (guess)
                ins_i = first_loc + (char_idx * 2)
                # draw letter on empty tile
                board[W_IDX] = board[W_IDX][:ins_i] + guess + board[W_IDX][ins_i+1:]
                revealed_count += 1
    else:     
        draw_man() # draw a limb on game board
        lives_remaining -= 1

    print_board()

# no more lives or all hidden tiles are revealed
if revealed_count is W_LEN:
    print('You win!')
else:
    print('You lose!')
    print('Answer:', w_rand)



