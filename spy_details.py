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
