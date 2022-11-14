#Day 1 - Guessing game

"""
User enters the number between 1 and 256. Every guess the program should
tell the user if guessed number is higher or lower. User can restart via 
console after completing the game.
"""

import random


class OutOfRangeError(Exception):
    pass

def guessingGame():
    numberToGuess = random.randint(1, 256)
    isSolved = False
    guessesCounter = 0
    while not isSolved:
        try:
            userGuess = int(input("Enter the number between 1 and 256 to guess the correct number!\n"))
            if userGuess > 256 or userGuess < 1:
                raise OutOfRangeError()
            guessesCounter += 1
            if userGuess > numberToGuess:
                print("Your entered number is too high, try again!\n")
            elif userGuess < numberToGuess:
                print("Your entered number is too low, try again!\n")
            else:
                print("Congrats!!! Your number is correct!\n")
                print(f'It took you {guessesCounter} tries.\n\n')
                gameOverButtonPress = input("Wanna play again? Press 'r' to replay, any other letter to quit.\n")
                if gameOverButtonPress != "r":
                    isSolved = True
                    return
                else:
                    numberToGuess = random.randint(1, 256)
                    guessesCounter = 0
        except ValueError:
            print("Enter a valid number!\n")
        except OutOfRangeError:
            print("Your number should be between 1 and 256, try again!\n")
        except:
            print("Something went wrong, try again.\n")
        

guessingGame()
