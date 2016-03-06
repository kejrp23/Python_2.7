# Created By: Jason R. Pittman
# Created On: 2/23/2016
# Wriiten for: Python 2.7

"""
This program is a simple address book program.
It is something that I could use for work or life.
I have programs that will provide me the solution that
I am looking for but this will also help me with my skills
as I am learning Python. 

"""



from time import sleep

addresses = {"Name" :[],
              "Phone Number" :[],
              "Email Address" :[],
              }

print "initializing program................"
sleep(3)

print " importing address database please wait "
sleep(3)

print " Welcome to Address Book 1.0 "

def initial_opening_screen():
  choices = raw_input("Please type a selection: Scan - Scan Address Book, Add - New Entry:  ")
  if choices.lower == "scan" :
    print "This option isn't ready yet, sorry!"
    return initial_opening_screen()
  elif choices.lower == "add" :
    print "Loading Entry Screen......"
    return adding_addresses()
  else:
    return initial_opening_screen()




def adding_addresses(name, phone, email):
  name = raw_input("Please enter the name: ")
  phone = raw_input("Pleaes enter Phone number: ")
  email = raw_input("Please enter Email Address: ")
  return name + phone + email
  
adding_addresses(name, phone, email)
  
