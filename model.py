import random
# store words in array
words = ['Bulbasaur', 'Ivysaur', 'Venusaur', 'Charmander', 'Charmeleon',
        'Charizard']


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



# random generate a word from word array
w_rand = words[random.randrange(len(words))] # random generated word from list ***** testing bulbasaur
W_LEN = len(w_rand) # length of chosen word
W_IDX = 12 # row which contains word on game board
revealed_count = 0
lives_remaining = 6
guesses = ''
BOARD_R_LEN = len(board[0])
board[W_IDX] = blank_tiles[W_LEN - 1] # mod board based on word length
# starting position for this rand word
first_loc = int((BOARD_R_LEN - (W_LEN * 2)) / 2)





