# This file contains the default spy data which would be imported in the main.py
# Importing required modules
from datetime import datetime


# This class defines the specifications of a spy
class Spy:
    # below are the spy methods
    # constructor for initialization of a spy

    def __init__(self, spyname, salutation, age, rating):
        self.spyname = spyname
        self.salutation = salutation
        self.age = int(age)
        self.rating = float(rating)
        self.spy_is_online = True
        self.status = None
        self.pool_of_status = []
        self.friend_list = []
        self.chats = []

    # accessor method to get spy name

    def get_name(self):
        return self.spyname

    # accessor method to get spy salutation

    def get_salutation(self):
        return self.salutation

    # accessor method for spy age

    def get_age(self):
        return self.age

    # accessor method for spy rating

    def get_rating(self):
        return self.rating

    # it takes a string as argument and sets the string as spy's status
    # it appends the status to the pool of status
    def update_spy_status(self, input_status):
        self.status = input_status
        self.pool_of_status.append(input_status)

    # When called it prints the status on screen
    def show_status(self):
        print(self.status)

    # When called shows the previous statuses if any
    def show_previous_status(self):
        j = 1
        for i in self.pool_of_status:
            print("{}. {}".format(j, i))
            j = j + 1

    # Takes argument a spy object which is friend of spy
    # and appends it to the spy's function
    def add_spy_friend(self, friend):
        self.friend_list.append(friend)


# This function takes as argument a Spy object for which friend is to be selected
# then it displays the friends online if any else it prints appropriate message for user
# it returns the index of friend to chat with in the spy,s friend list
# if no friend is online it returns None
def select_a_friend(spy):
    i = 1
    if len(spy.friend_list) > 0:
        for friend in spy.friend_list:
            print("{}. {} {} age: {} and rating: {} is  online ".format(i, friend.salutation,
                                                                        friend.spyname, friend.age, friend.rating))
            i = i + 1
        choice = int(input("choose a friend : "))
        return choice - 1
    else:
        print("you have no friends online ")
        return None


# function to evaluate message for spy based on rating
def message_for_spy(rating):
    if rating > 4.5:
        print("Great one!!! Keep it up ")
    elif 4.5 >= rating > 3.5:
        print("You are a Good one!!! ")
    elif 3.5 >= rating > 2.5:
        print("You can always do better!!! ")
    elif rating <= 2.5:
        print("We can always take someone's help ")
    else:
        print("You didn't provide a valid rating ")


# function to check spy eligibility return true if spy is eligible else false
def check_spy_eligibility(age):
    if 12 < age < 50:
        return True
    else:
        return False


# A class called chat defined which is a message with a timestamp
class Chat:
    # constructor for chat object
    def __init__(self, message, sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me
