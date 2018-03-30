
# default status
current_status_message = None

# list of default status
status = ['My name is Ayush.', 'MRIU']


class User:
    def __init__(self, uname, salutation, age, rating):
        self.uname = uname
        self.salutation = salutation
        self.age = age
        self.rating = rating


user_1 = User('Ayush', 'Mr.', 19, 3.8)


friend_one = User('Lowe', 'Mr.', 21, 4.1)
friend_two = User('Purab', 'Mr.', 20, 3.9)
friend_three = User('Shivam', 'Mr.', 21, 3.7)


friends = [friend_one, friend_two, friend_three]
