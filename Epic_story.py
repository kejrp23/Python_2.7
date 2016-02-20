"""
Welcome to the most awesome story ever, it's awesome because the user will help to write it,
so the code might can look better but there is a beginners story so who cares, 
alright lets get started shall we!!

Created by Jason R. Pittman on 2/20/2016 for Codeacademy Project
Written in Python 2.7
"""

print "Welcome to Mad Libs and interactive story program where you help write the story"

main_char = raw_input("Please enter a name for our main character: ")

adj1 = raw_input("Please enter and adjective for our story: ")
adj2 = raw_input("Please enter another adjective for our story: ")
adj3 = raw_input("Now we need just one more adjective: ")

verb1 = raw_input("Ok now for some verbs please enter the first verb: ")
verb2 = raw_input("Please think of another: ")
verb3 = raw_input("Ok, now we need just one more verb and we move on: ")

noun1 = raw_input("Ok, it's not a sentence with out nouns so lets do 4 of them what's the first one: ")
noun2 = raw_input("And the second: ")
noun3 = raw_input("Lets see how about another: ")
noun4 = raw_input("Can we have one more and I think that'll do it: ")

animal = raw_input("What's your Favorite animal? ")
food = raw_input("What's your favorite food? ")
fruit = raw_input("What's a fruit that you think would be a good addition to the story? ")
number = raw_input("Enter a number any number: ")
superhero = raw_input("Who's your favorite superhero: ")
country = raw_input("Name a Country: ")
dessert = raw_input("What's a good dessert: ")
year = raw_input("Pick a year for this story to take place in: ")


#The template for the story
STORY = "This morning I woke up and felt %s because %s was going to finally %s over the big %s %s. On the other side of the %s were many %ss protesting to keep %s in stores. The crowd began to %s to the rythym of the %s, which made all of the %ss very %s. %s tried to %s into the sewers and found %s rats. Needing help, %s quickly called %s. %s appeared and saved %s by flying to %s and dropping %s into a puddle of %s. %s then fell asleep and woke up in the year %s, in a world where %ss ruled the world."

print STORY % (adj1,main_char,verb1,
