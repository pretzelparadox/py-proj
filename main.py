# Program: Hangman
# Start Date: 1/25/22
# End Date: 1/31/22 

import game

choice = 'Y' # player choice to start new game

while choice is 'N':
    choice = input('Ready to play Hangman? (Y/N)\n')

while choice is 'Y':
    game.start()

    game.reset()
    choice = 'N'

    while choice is 'N':
        choice = input('Ready to play Hangman? (Y/N)\n')
    

