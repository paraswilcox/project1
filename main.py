# Spy chat program to send secret message b/w spies
# importing Chat class
# importing Spy class and its associated methods
# stand alone functions will come in handy also
from spy_details import Spy, Chat, check_spy_eligibility, message_for_spy, select_a_friend
# importing Steganography class and its associated methods
# for encoding and decoding messages
from stegano import lsb


# a function that updates the status using Spy methods
# it checks if there is a status update already
#   if that,s the case then it shows the the current status and user has two options
#   Either choose status from previous status updates or add a new one altogether
# if there is no status update then it asks to add a new status altogether
# in either of the cases at last it shows the current status
def status_update():
    pass


# This function asks user to enter friend details and if they fulfill the criteria for a spy
# then it adds the friend to the friends list of our spy
# if a friend is added it notifies the user by printing the message "friend added"
def add_a_friend():
    pass


# This function uses Steganography to encode the message and send it to the desired friend
# it calls the Spy method named select_a_friend to select a friend out of online friends
def send_secret_msg():
    pass


def read_secret_msg():
    pass


def read_chats():
    pass


# This function shows menu to the user
# there are 6 choices to choose from
# each choice calls a function to handle that choice
# valid choices result in call to the corresponding function
# 6th and any other choice halts the program
def show_menu():
    menu_choice = int(input("What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret "
                            "message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application "
                            "\n "))
    if menu_choice == 1:
        status_update()
    elif menu_choice == 2:
        num_of_friends = add_a_friend()
        print("You have {} friends".format(num_of_friends))
        show_menu()
    elif menu_choice == 3:
        send_secret_msg()
    elif menu_choice == 4:
        read_secret_msg()
    elif menu_choice == 5:
        read_chats()
    else:
        exit()


# A function that asks the user to entered the details if user isn't the default user
# it creates a spy object that overrides the default one
def make_a_spy():
    spy_name = input("What is your name : ")
    # if user will enter a name only then further processing would take place
    if len(spy_name) > 0:
        spy_salutation = (input("Welcome! {} What should we call you (Mr. or Ms.) ".format(spy_name)).capitalize())
        spy_age = int(input("What is your age : "))
        spy_is_eligible = check_spy_eligibility(spy_age)
        if spy_is_eligible:
            spy_rating = float(input("Enter your rating out of 5 : "))
            message_for_spy(spy_rating)

            # Creating a Spy object with user provided details and welcoming
            # user using methods from spy class so
            # to encapsulate the variables of the class
            newspy = Spy(spy_name, spy_salutation, spy_age, spy_rating)
            return newspy
        else:
            print("Sorry, you are not eligible")
            exit()
    else:
        print("Error: You did'nt entered  a valid name")
        exit()


# Starting the application with a welcome note
print("Welcome to Spy chat Application ")

# creating a default spy with parameters as under
spy = Spy("Bond", "Mr.", 30, 4.8)

# Assigning our default spy some number of statuses to choose from pool of statuses
spy.pool_of_status = ["I'm Bond", "At your service", "bow down to the king"]

# Assigning our spy some friends
# we create to Spy objects and assign them name "friend1" & "friend2"
# we then add these friends to spy's friend list
friend1 = Spy("Paras", "Mr", 21, 4.99)
friend2 = Spy("Sam", "Mr", 21, 2.99)
spy.add_spy_friend(friend1)
spy.add_spy_friend(friend2)

# Asking user to continue as the spy we made above
choice = input("Do you want to continue as {} {} (Y or N) ".format(spy.get_salutation(), spy.get_name()))

# Checking if user is a default one or not
if choice == "Y" or choice == "y":
    ask_for_info = False
else:
    ask_for_info = True

# if user was not the default one we let the "make_a_spy" method handle the task of collecting spy info
# otherwise welcome him as default spy
if ask_for_info:
    spy = make_a_spy()

# Welcome the spy (We use the spy object and its methods)
print("Welcome {} {} age : {}, rating : {:0.2f}"
      .format(spy.get_salutation(), spy.get_name(), spy.get_age(), spy.get_rating()))

# We call the "show_menu" function to let the user make a choice from the menu
show_menu()
