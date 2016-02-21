"""
Program made during a codeacademy training excersize, this program is basically a dice game with 
the computer being the dice. I mean seriously who doesn't like a game of dice.
The house shouldn't always win and we are here to make sure of that.
So strap in and lets roll!
"""



from random import randint
from time import sleep

def get_user_guess():
  user_guess = int(raw_input("Please guess a number: "))
  return user_guess
 
def roll_dice(number_of_sides):
 		first_roll = randint(1,number_of_sides)
 		second_roll = randint(1,number_of_sides)
		max_val = number_of_sides * 2
		print "The maximum value is: " + str(max_val)
		sleep(1)
		user_guess = get_user_guess()

		if user_guess > max_val:
 			print "You have entered and number that is too large for a set of dice"
 			return
		else:
 			print "Rolling..."
			sleep(2)
			print "The First roll is: %d" % first_roll
			sleep(1)
			print "The Second Roll is: %d" % second_roll
			sleep(1)
			total_roll = first_roll + second_roll
			print "And the total is!!"
			sleep(2)
			print total_roll
		if user_guess > total_roll:
			print "Congratulations YOU WIN!!!"
			return
		else:
			print "YOU LOSE!!"
			print "Better LUCK next time"
			return

roll_dice(6)
