####### Information Of A Default User #######
from datetime import datetime

# default status
current_status_message = None

# list of default status
status = ['My name is Ayush.', 'MRIU']


class User:
    # create class
    def __init__(self, uname, salutation, age, rating):
        self.uname = uname
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class ChatMessage:
    def __init__(self, message, sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me


# define user_name, age, rating
user_1 = User('Ayush', 'Mr.', 19, 3.7)


# details of some existing friends
friend_one = User('Lowe', 'Mr.', 21, 4.1)
friend_two = User('Purab', 'Mr.', 20, 3.9)
friend_three = User('Shivam', 'Mr.', 21, 3.7)

# lists of friends
friends = [friend_one, friend_two, friend_three]
