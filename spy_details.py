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