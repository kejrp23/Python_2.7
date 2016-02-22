"""

This Program is being written to incorporate all 
things Python that I have learned thus far.

I am writing this in windows notepad to better test
my ablility to do proper spacing and indentions
without having a proper tool that will handle small
things for me.

I'm unsure at the time of this writing where this 
program will go. My main goal is or it to just work.


Created by: Jason R. Pittman
Creation start Date: 2/22/2016 10:18am

"""

from datetime import datetime
from time import sleep
from math import *

print "Initializing application.............."
Sleep(3)
print "Welcome to Python Adventures............"
sleep(4)

User_name =raw_input("Please enter your name so I know whom to refer to: "

work_bag = [
"Laptop", 
"SSD",
"FlashDrive",
"Binder",
"Pens",
"Name Badge"
]

lunch_box = [
"apple,
"soup",
"Ukrop's rolls",
"mountain dew"
]


preparing_for_work = [
"Shower",
"Brush Teeth",
"get dressed"
]

def getting_ready():
	print "Good morning " + User_name + " it's time to get ready for work!"
	answer = user_input("Are you going to work today? yes or no please: "
		if answer.lower() is == "yes":
			print "OK make sure you do these things! " + preparing_for_work
		
		else:
			print "Well enjoy your day off and we will se you next time!"
		return
getting_ready()



		