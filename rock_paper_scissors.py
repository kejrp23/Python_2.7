# Created as a project for CodeAcademy
# Author: Jason R. Pittman
# Created on 2/27/2016

# This project was made with my own little twist to it

"""
This is a program for Rock. Paper, Scissors,
Over the course of this program we will 
have the user to select an option, then
have the computer pick a random option.
Compare both of their choices and determine
a winner. At that point we then inform the winner.

							~Jason R. Pittman~

"""

from random import randint
from time import sleep

options = ["R", "P", "S"]
YOU_LOSE = "You are a Loser!"
YOU_WIN = "You are a Winner!"

def decide_winner(user_choice,computer_choice):
  print "You Selected %s" % user_choice
  print "Computer Selecting....."
  sleep(1)
  print "The Computer has Selected %s" % computer_choice
  sleep(1)  
  user_choice_index = options.index(user_choice)
  computer_choice_index = options.index(computer_choice)
	
  if user_choice_index == computer_choice_index:
    print "You both picked the same choice therefore it's a tie!"
  elif user_choice_index == 0 and computer_choice_index == 2:
    print YOU_WIN
  elif user_choice_index == 1 and computer_choice_index == 0:
    print YOU_WIN
  elif user_choice_index == 2 and computer_choice_index == 1:
    print YOU_WIN
  elif user_choice_index > 2:
    print "Come on man you had one job and that's Rock, Paper, Scissors pick one!"
    return
  else:
    print "YOU LOSE!!!"
    
def play_RPS():
  print "Initializing............"
  sleep(2)
  print "Loading possible outcomes......."
  sleep(2)
  print "Welcome to Rock, Paper, Scissors"
  user_choice = raw_input("Please Select R for Rock, P for Paper, or S for Scissors: ")
  sleep(1)
  user_choice = user_choice.upper()
  computer_choice = options[randint(0,len(options)-1)]
  decide_winner(user_choice,computer_choice)

play_RPS()
