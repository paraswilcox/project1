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
    if spy.status is None:
        print("You do not have any status ")
        input_status = input("Enter Status to update")
        spy.update_spy_status(input_status)
        print("Your status : ")
        spy.show_status()
    else:
        print("Your current Status is : ")
        spy.show_status()
        user_choice = input("Enter y if you want to update status from previous status updates : ")
        if user_choice == "Y" or user_choice == "y":
            print("These are your previous status updates :")
            spy.show_previous_status()
            user_choice1 = int(input("Enter the number of the status update: "))
            spy.update_spy_status(spy.pool_of_status[user_choice1 - 1])
            print("Your status : \n")
            spy.show_status()
        else:
            input_status = input("Enter Status to update")
            spy.update_spy_status(input_status)
            print("Your status : ")
            spy.show_status()
    show_menu()


# This function asks user to enter friend details and if they fulfill the criteria for a spy
# then it adds the friend to the friends list of our spy
# if a friend is added it notifies the user by printing the message "friend added"
def add_a_friend():
    friend_name = input("What is your friend's name: ")
    if len(friend_name) > 0:
        friend_salutation = input("What should we call your friend (Mr or Ms): ").capitalize()
        friend_age = int(input("Age: "))
        if check_spy_eligibility(friend_age):
            friend_rating = float(input("Enter the rating: "))
            if friend_rating >= spy.rating:
                friend = Spy(friend_name, friend_salutation, friend_age, friend_rating)
                spy.add_spy_friend(friend)
                print("Friend added!")
            else:
                print("Your friend has lower rating than you and we can't allow that")
        else:
            print("Age is not valid")
    else:
        print("You didn't entered a valid name")
    return len(spy.friend_list)


# This function uses Steganography to encode the message and send it to the desired friend
# it calls the Spy method named select_a_friend to select a friend out of online friends
def send_secret_msg():
    friend_to_chat = select_a_friend(spy)
    if friend_to_chat is None:
        show_menu()
    else:
        input_image = input("Enter the name of the image with extension: ")
        message = input("Type in the message ")
        file_name = input_image.split(".")
        if 0 < len(message):
            encoded_message = lsb.hide(input_image, message)
            encoded_message.save(file_name[0] + "output." + file_name[1])
            new_chat = Chat(message, True)
            spy.friend_list[friend_to_chat].chats.append(new_chat)
            urgent_message = message.find("SAVE ME" or "SOS")
            if urgent_message == -1:
                print("Your secret message is encoded in image! ")
            else:
                print('\033[1;31mWe are coming to help you Sir...\033[1;m')
                print("Your secret message is encoded in image! ")
        else:
            print("Sorry! Your message was empty\n")
    show_menu()


# This function uses steganography to decode message received from friend and appends it the spy's chat list
# This function deletes a spy if they talk too much more than 100 words
def read_secret_msg():
    sender = select_a_friend(spy)
    file_name = input("What is the name of the file?")
    decoded_message = lsb.reveal(file_name)
    # We split the message with space as separator
    # as we have to delete a spy based on words not alphabets
    num_of_words = decoded_message.split()
    if len(num_of_words) < 100:
        new_chat = Chat(decoded_message, False)
        spy.friend_list[sender].chats.append(new_chat)
        print("Your secret message has been saved!")
    else:
        print("Can't read that much ")
        del (spy.friend_list[sender])
        print("Removed from Friend List")
    show_menu()


# this fxn shows chat history b/w our spy and a friend our spy chooses
def read_chats():
    read_chat_of = select_a_friend(spy)
    print("chat history b/w you and {}: ".format(spy.friend_list[read_chat_of].spyname))
    print('\n')
    for a_chat in spy.friend_list[read_chat_of].chats:
        if a_chat.sent_by_me:
            print("Time: {} \nSender:\033[1;31mYou\033[1;m\nMessage: {}\nReceiver: {}"
                  .format('\033[1;34m' + str(a_chat.time) + '\033[1;m', a_chat.message,
                          spy.friend_list[read_chat_of].spyname))
            print("\n")
            print("\n")
        else:
            print("Time: {} \nSender: {}\nMessage: {}"
                  .format('\033[1;34m' + str(a_chat.time) + '\033[1;m',
                          '\033[1;31m' + spy.friend_list[read_chat_of].spyname
                          + '\033[1;m', a_chat.message))
            print("\n")
            print("\n")
    show_menu()


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
