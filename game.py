import random
import model
# helper debug functions
def print_debug():
    # debug info
    print('Debug Info:')
    print('Random word:', model.w_rand)
    print('Word length:', model.W_LEN)
    print('Blank tiles row length:', len(model.blank_tiles[0]))
    print('Board row length:', len(model.board[0]))
    print('Word row', model.board[W_IDX])
    print('first index tile loc', model.first_loc)

def print_guesses():
    print('Guessed Letters:')
    print(model.guesses)

def print_board():
    for row in model.board:
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

def won():
    print('You win!')

def lost():
    print('You lose!')
    print('Word:', w_rand)
    
def reset():
    # reset board
    # game board
    model.board = [
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
    
    # random generate a word from word array
    w_rand = words[random.randrange(len(words))] # random generated word from list ***** testing bulbasaur
    W_LEN = len(w_rand) # length of chosen word
    W_IDX = 12 # row which contains word on game board
    revealed_count = 0
    choice = 'Y' # player choice to start new game
    lives_remaining = 6
    guesses = ''
    BOARD_R_LEN = len(board[0])
    board[W_IDX] = blank_tiles[W_LEN - 1] # mod board based on word length
    # starting position for this rand word
    first_loc = int((BOARD_R_LEN - (W_LEN * 2)) / 2)
    
def prompt_guess(): 
    # prompt user to input a letter guess
    guess = input('Guess a letter (A-Z):\n')
    guesses = guesses + ' ' + guess


def draw_letter():
     # iterate through letters of bulbasaur (find insertion position)
     for char_idx in range(0, W_LEN):
         curr_letter = w_rand[char_idx].lower()
         # if random_word contains that letter
         if guess  ==  curr_letter:
             # insertion location for chosen letter (guess)
             ins_i = first_loc + (char_idx * 2)
             # draw letter on empty tile
             board[W_IDX] = board[W_IDX][:ins_i] + guess + board[W_IDX][ins_i+1:]


def end():
    # no more lives or all tiles revealed
    if revealed_count is W_LEN:
        game.won()
    else: 
        game.lost()
 
def start():
    print('Game Started.')
    print_board()
    # keep asking for letter guesses
    while lives_remaining > 0 and revealed_count is not W_LEN:
        prompt_guess()
        if str(guess) in str(w_rand):
            draw_letter()
            revealed_count += 1
        else:     
            draw_man() # draw a limb on game board
            lives_remaining -= 1
    
        print_board()
        print_guesses()

    end()
