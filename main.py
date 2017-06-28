# Spy chat program to send secret message b/w spies
# importing Chat class
# importing Spy class and its associated methods
# stand alone functions will come in handy also
from spy_details import Spy, Chat, check_spy_eligibility, message_for_spy, select_a_friend
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