# Program: Hangman
# Date: 1/25/22
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
words = ['dog', 'cat', 'giraffe', 'marble']
random_word = words[random.randrange(len(words))]
choice = 'N' 
picture = ''' 
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


# prompt user to play new game
while choice is 'N':
    choice = input('Ready to play Hangman? (Y/N))\n')

# start a new game
print('Game Started.')
# print board
print(picture)






# reset the game
# randomly select a word for current game 
# have a certain amount of "lives"
# draw a limb (wrong letter guess)
# reveal an underscore (correct letter guess)
