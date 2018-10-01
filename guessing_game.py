'''This is a classic number guessing game. '''

from random import randint


def play_game():
	# Collect and check guess. Provide feedback to user. Tracks the number of guesses - without double counting repeat guesses
	secret_number = randint(1, 16)
	won_game = False
	number_of_guesses = 0
	print 'Welcome to the guessing game. Enter a guess between 1 and 15.'
	while won_game == False:
		guess = int(raw_input('Enter your guess: '))
		if guess < 1 or guess > 15:
			print 'Invalid guess. Try again'
		elif guess == secret_number:
			print 'You win! It took you %s guesses!' % (number_of_guesses+1)
			won_game = True
		elif guess > secret_number:
			print 'Your guess is too high! Try again.'
			if repeat_guess(guess) == False:
				number_of_guesses += 1
		else:
			print 'Your guess is too low! Try again.'
			if repeat_guess(guess) == False:
				number_of_guesses += 1


def repeat_guess(value):
	# Checks if number has already been guessed to avoid double counting 
	global previous
	if value in previous:
		return True
	else:
		previous.append(value)
		return False

# Stores values of previous guesses
previous = []

play_game()