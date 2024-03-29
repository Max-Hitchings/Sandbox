import string

import requests
import os


class HangMan:
    def __init__(self, playerName):
        self.lives = 5
        self.name = playerName
        self.letters = []
        self.word = ""
        self.rightGuesses = 0
        self.wrongGuesses = 0


    def createWord(self):
        wordRequest = requests.get("https://random-word-api.herokuapp.com/word")

        # wordRequest.json()
        self.word = wordRequest.text.replace('"', '').replace('[', '').replace(']', '')


    def makeGuess(self):
        pass

    def clear(self):
        os.system('clear')

    def loseGame(self):
        if input("you have run out of lives.\nplay again? (y/n)") == 'y':
            self.startGame()
        else:
            print("Thanks for playing")

    def winGame(self):
        if input("you have won.\nplay again? (y/n)") == 'y':
            self.startGame()
        else:
            print("Thanks for playing")


    def inputGuess(self, guess):
        if guess.replace(' ', '') != '' and len(guess) == 1 and guess not in self.letters and guess in string.ascii_lowercase:
            self.letters.append(guess)

            for l in self.word:
                if guess == l:
                    self.rightGuesses += 1
            if guess in self.word:
                ## TO-DO ##
                if self.rightGuesses > len(self.word):
                    self.winGame()

                print("correct guess no:", self.rightGuesses)
            else:
                self.lives -= 1
                self.wrongGuesses += 1
                print("lives left:", self.lives)
            if self.lives < 0:
                self.loseGame()
        else:
            print(f"Invalid guess\nlives left {self.lives}")

    def startGame(self):
        self.createWord()
        # self.word = "test"
        print("DEBUG word:", self.word)

        self.rightGuesses = 0

        while self.rightGuesses < len(self.word):
            guess = input("guess a letter")
            self.inputGuess(guess)
        self.winGame()

name = input("Welcome to hangman\nPlease enter your name\n")
game = HangMan("name")
game.startGame()
