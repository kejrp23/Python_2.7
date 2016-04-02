"""
Created on 3/26/27
Created for Codeacademy Training exersize.
Written by: Jason R. Pittman
Note: All comments are my own for information purpose and future building ideas.
Note: They reflect my ideas and my ideas alone
This is a calendar program for Command Line. 

The program should behave in the following way:

Print a welcome message to the user
Prompt the user to view, add, update, or delete an event on the calendar
Depending on the user's input: view, add, update, or delete an event on the calendar
The program should never terminate unless the user decides to exit
"""
#This is the main structural requirements for the Calendar
from time import sleep,strftime #save time and import both at once
#MY_FIRST_NAME = "Jason" #at some point let the user do this through raw_input()
calendar = {} #dictionaries use values and pairs so we will use Dates and events
#Above here we have the time elements a Consant name to work with and a dictionary
#ok from here on is the Calendar
def welcome():#This is the Splash screen or Welcome area for getting started.
  #This is a possible line for adding a raw_input for the users name
  MY_FIRST_NAME = raw_input("Lets Get Started\n Please enter your first name: ")
  print "Welcome " + MY_FIRST_NAME + "."
  print "Opening your Calendar one moment please"
  sleep(2)
  print "Today's date is: " + strftime("%A %B %d,%Y") 
  print "the Current time is " + strftime("%I:%M:%S")
  print "What would you like to do? "
#time to set how the calendar runs until exit  
def start_calendar():
  welcome()
  start = True
  while start:#keeps the program running unless exited by choice
    user_choice = raw_input('A to add, U to Update, V to View, D to Delete, X to Exit: ')
    user_choice = user_choice.upper()
    #check these indentions i don't think they are right
#   	if user_choice == 'V':
