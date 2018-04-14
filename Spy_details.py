# creating class
class Spy:
    def __init__(self,name,salutation,age,rating):
        self.name= name
        self.salutation = salutation
        self.age= age
        self.rating= rating
        self.is_online=True
        self.chats=[]
        self.current_status_message= None

# chats between spies
class ChatMessage:
        def __init__(self, spy_name, friend_name, time, message):
            self.spy_name = spy_name
            self.friend_name = friend_name
            self.time = time
            self.message = message


# define spy_name, age, rating)
spy_1=Spy('Ayush Jaiswal','Mr',20,3.3)

# lists of friends
friends=[]
# list of chats
chats = []