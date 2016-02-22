# Created By: Jason R. Pittman
# Created on 2/13/2016
# Created during a testing session on Codeacademy.com
# Created using their code
# Created to have a copy of the working game.

print "Welcome to the Pig Latin Translator"


pyg = 'ay' # second part of the code



# This will print on the screen and allow the user to type.

original = raw_input("Please enter a word:") 


#This will lowercase whatever the user typers

word = original.lower() 

#this takes the first letter of the word entered

first = original[0] 

#only prints the the word minus the first letter.

word[1:] 
new_word = word[1] + first + pyg




#this statement will check to make sure the word only has letters in it.

if len(original) > 0 and original.isalpha(): 

#it also checks to see if anything was typed.

	print new_word

else:

	print "empty" 




