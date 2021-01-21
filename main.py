import random 
HANGMAN = ['''
+---+
|   |
	|
	|
	|
	|
=========''', '''
+---+
|	|
O 	|
	|
	|	
	|
=========''', '''
+---+
| 	|
O 	|
| 	|
	|
	|
=========''', '''
 +---+
 | 	 |
 O 	 |
/| 	 |
	 |
	 |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
	 |
	 |
=========''', '''
 +---+
 | 	 |
 O 	 |
/|\  |
/ 	 |
	 |
=========''', '''
 +---+
 |	 |
 O	 |
/|\  |
/ \  |
	 |
=========''']


def randomWord(wordList):
  return  random.choice(wordList)


def getUserGuess(guessedLetters):
	while True:
		userGuess = input("Chose a letter: ")
		if len(userGuess) !=1 :
			print("Your input is invaild. Try again.")

		elif not userGuess.isalpha():
			print("You can only guess alphabetical letters. Try again.")
		elif userGuess in guessedLetters:
			print("You've already guessed this letter. Try again.")
		else: 
			return userGuess

def displayBoard(HANGMAN, missedLetters, correctLetters, word):
	print(HANGMAN[len(missedLetters)])
	print(f"You've taken {len(missedLetters)} incorrect guess(es).")
	#Print out the incorrect letter, if any.
	for letter in missedLetters:
		print(letter)

	blanks = ["_."]*len(word)

	for i in range(len(word)):
		if word[i] in correctLetters:
			blanks[i] = word[i] + "."

	print("".join(blanks))

def main():
	words = ["forest", "mail","light,", "cliff", "wagon", "free", "dark", "calm","round", "sunny", "far", "bison", "pouch", "dress", "apple", "cord", "moon", "fox", "long", "hand" ]
	print("Hello, welcome to Hangman.")
	initialPromt = input("Would you like to play? y/n.")

	if initialPromt == "y":
		playGame = True

	elif initialPromt == "n":
		print("Goodbye!")
		playGame = False

#Game Variables

	targetWord = randomWord(words)
	win = False
	correctLetters = ""
	missedLetters = ""

	while playGame:
		displayBoard(HANGMAN, missedLetters, correctLetters, targetWord)
		userGuess = getUserGuess(correctLetters+missedLetters)
		if userGuess in targetWord:
			correctLetters+= userGuess
			allGuessesAreCorrect = True

		for i in range(len(targetWord)):
			if targetWord [i] not in correctLetters:
				allGuessesAreCorrect = False
				break

		if allGuessesAreCorrect == True:
			displayBoard(HANGMAN, missedLetters, correctLetters, targetWord)
			print("You win!")
			win = True

		else:
			missedLetters += userGuess
			if len(missedLetters) == len(HANGMAN)-1:
				displayBoard(HANGMAN, missedLetters, correctLetters, targetWord)
				print("You've Lost."
				)
				print(f"The correct answer is {targetWord}")
				win = True

		if win:
			finalPrompt = input("Play again? y/n  ")

			if finalPrompt == "y":
				win = False
				targetWord = randomWord(words)
				correctLetters = ""
				missedLetters = ""
			else:
				print("Game Over")
				playGame = False


main()
