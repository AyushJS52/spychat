from spy_details import Spy, friends ,ChatMessage ,chats
from spy_details import spy_1
from steganography.steganography import Steganography
from datetime import datetime
from termcolor import colored
import csv


# #add a new friend
def add_friend():
    # using class user
    new_friend = Spy(" ", " ", 0, 0.0)

    # ask user for name
    new_friend.name = raw_input("Please add your friend's name: ")

    # user name validation.
    if len(new_friend.name) > 0:
        if len(new_friend.name) > 20:
            print("Your name length is big.")
    else:
        print("Name should be not empty or length is less then 20 char.")
        return add_friend()

    new_friend.salutation = raw_input("What to call Mr. or Ms.?: ")

    # user salutation validation
    if len(new_friend.salutation) > 0:
        if len(new_friend.salutation) > 5:
            print("Your salutation is too big.")
    else:
        print("Salutation empty or check length")
        return add_friend()

    # concatination for full name
    new_friend.name = new_friend.salutation + " " + new_friend.name

    # ask for age of the friend
    new_friend.age = int(raw_input("Age: "))

    if 12 < new_friend.age < 50:
        True
    else:
        print colored("Age should be in between 12 to 50","red")
        return add_friend()

    #ask for rating of friend, using float
    new_friend.rating = float(raw_input("Spy rating? "))

    if new_friend.rating > 0.0:
        True
    else:
        print("Rating should be more than 0.0")
        return add_friend()

    # add friend if all conditions check
    friends.append(new_friend)
    print('Friend Added!')
    with open("friends.csv", "a") as friends_data:
        writer = csv.writer(friends_data)
        writer.writerow([new_friend.name, new_friend.salutation, new_friend.age, new_friend.rating, new_friend.is_online])

    #total no of friends
    return len(friends)
#default_status
STATUS_MESSAGES = ['My name is Ujjwal Sharma.', 'I love to learn', 'Location: New Delhi']
#select one friend from many friends
def select_a_friend():
    item_position = 1
    # showing the all friends from friends dictionary
    for friend in friends:
        print("%d. %s age: %s with ratting %.2f is online" %(item_position,friend.name,friend.age,friend.rating))
        item_position=item_position+1
    friend_choice=int(raw_input("choose your friend"))
    friend_choice_position=friend_choice-1
    return friend_choice_position
#special message
special_words = ['SAVE ME', 'SOS' , 'HELP', 'help', 'sos']

#send message in SpyChat
def send_a_message():
    friend_choice = friends[select_a_friend()].name

    original_image = raw_input("What is the name of the image?")
    output_path = 'output.jpg'
    text = raw_input("What do you want to say?")
    if text in special_words:
        text = colored(text + ": IT'S EMMERGENCY!!", "red")
    #encoding the message
    Steganography.encode(original_image, output_path, text)

    # the message will be stored in chat message class
    new_chat = ChatMessage(spy_name=spy_1.name, friend_name=friend_choice, time=datetime.now().strftime("%d %B %Y"), message=text)

    # name of the friend along which we add message.
    chats.append(new_chat)
    print("your secret message is ready.")

    with open('chats.csv', 'a') as chats_data:
        writer = csv.writer(chats_data)
        writer.writerow([new_chat.spy_name, new_chat.friend_name, new_chat.time, new_chat.message])

#read message in SpyChat
def read_a_message():
    sender = select_a_friend()

    output_path = raw_input("What is the name of the file?")
    secret_text = Steganography.decode(output_path)
    print(secret_text)

    # add the chat to sender
    chat = ChatMessage(spy_name=spy_1.name, friend_name=sender, time=datetime.now().strftime("%d %B %Y"), message=secret_text)
    friends[sender].chats.append(chat)
    print("Your secret message has been saved.")
    # writing chats in chats.csv
    with open("chats.csv", 'a') as chat_record:
        writer = csv.writer(chat_record)
        writer.writerow([chat.spy_name, chat.friend_name, chat.time, chat.message])

  #Read chats
def readchat(choice):
    name_friend = friends[choice].name
    with open('Chats.csv', 'rU') as chats_data:
        reader = csv.reader(chats_data)
        for row in reader:
            try:
                c = ChatMessage(spy_name=row[0], friend_name=row[1], time=row[2], message=row[3])
                # checking the chats of the current spy with selected friend
                if c.spy_name == spy_1.name and c.friend_name == name_friend:
                    print colored("You sent message to the Spy name: %s "%name_friend,"red")
                    print colored("On Time: [%s]"%c.time,"blue")
                    print("Message: %s"% c.message)
                    return 1
            except IndexError:
                pass
            continue


def add_status(current_status_message):
    if current_status_message !=None:
        print("your current status is:"+current_status_message)
    else:
        print colored("you don't have any current messeage","red")
    question=raw_input("do you want to select status from old status? y/n")
    # append new_status to STATUS_MESSAGE
    if question.upper()=="N":
        new_status=raw_input("enter your new status ")
        if len(new_status)>0:
            STATUS_MESSAGES.append(new_status)
            return(new_status)
        else:
            print("invalid new status need to be enter ")
    # if user want to select from STATUS_MESSAGE
    elif question.upper()=="Y":
        # showing all old status
        for i in range(len(STATUS_MESSAGES)):
            print(str(i)+"."+STATUS_MESSAGES[i])
        message_selection=int(raw_input("\n choose from above status"))
        # if user enter more than the no of  status in STATUS MESSAGE
        if len(STATUS_MESSAGES)>message_selection:
            update_status_message=STATUS_MESSAGES[message_selection]
        else:
            print colored("selected message is not in older status ", "red")
        return update_status_message
# Menu option
def start_chat(spy_name, spy_age, spy_rating):
    current_status_messesge = None
    print("your current status is " + str(current_status_messesge))

    # load_friends() is a function which loads all the friends stored in friends.csv
    def load_friends():
        with open('friends.csv', 'rU') as friends_data:
            reader = csv.reader(friends_data)
            for row in reader:
                try:
                    friends.append(Spy(name=row[0], salutation=(row[1]), age=int(row[2]), rating=float(row[3])))
                except IndexError:
                    pass
                continue

    # load_chats()
    def load_chats():
        with open("chats.csv", 'rU') as chat_data:
            reader = csv.reader(chat_data)
            for row in reader:
                try:
                    chats.append(ChatMessage(spy_name=row[0], friend_name=row[1], time=row[2], message=row[3]))
                except IndexError:
                    pass
                continue


    # load friend and chat to csv
    load_friends()
    load_chats()

    continue_option = "Y"

    while (continue_option == 'Y' or continue_option == 'y'):

        menu_option = int(raw_input(
            "What would you like to do \n 1. Add a status update \n 2. Add a friend \n 3. Send a message \n 4. Read a secret message \n 5. Read chats from a user \n 6. Close the application"))

        # displaying menu option for user
        while (menu_option<=6):
            if menu_option == 1:
                print("You choose update the status ")

                current_status_messesge = str(add_status(current_status_messesge))
                # calls the add_status_message from the add_status file
                print colored("Your selected status is:" +current_status_messesge,"blue") #Displays the status chosen or entered by the spy
                break
            elif menu_option == 2:
                print("Adding a friend")
                # add a new friend
                number_of_friends = add_friend()
                print('You have %d friends' % number_of_friends) #prints the number of friends
                break
            elif menu_option == 3:
                print("Sending a  message")
                send_a_message()
                break
            elif menu_option == 4:
                print("Read a secret message")
                read_a_message()
                break
            elif menu_option == 5:
                print("Reading chat from user")
                print "select a friend whose chat you want to see"
                choice = select_a_friend()
                readchat(choice)
                break
            elif menu_option ==6:
                print("Exiting")
                exit()
        continue_option = raw_input("Would you like to perform another operation (Y/N)")
    print("Thank you for your time")

spy_is_online = False  # status of the spy
user_option = raw_input(
    "Would you like to continue as "+spy_1.salutation+" "+spy_1.name +" or create your own(Y/N)")
# for creating new user

if user_option == 'N' or user_option == 'n' :
    spy_name = raw_input("Welcome to SpyChat, you must tell me your Spyname first:")
    if len(spy_name) > 0: # to calculate the length of the string
        print('Welcome ' + spy_name + ' Glad to have you with us.')
        spy_salutation = raw_input("What should I call you Mr. or Ms. ?")
        print(
            'Alright ' + spy_salutation + '.' + spy_name + ' I\'d like to know a little bit more about you before we proceed')
    else:
        print('A spy needs to have a valid name. Please try again.')
    spy_age = int(raw_input('What is your age? '))  # age of the spy
    if spy_age > 12 and spy_age < 50:
        spy_rating = float(raw_input('What is your spy rating? '))
        if spy_rating > 4.5:
            print('Great Ace!')
        elif spy_rating > 3.5 and spy_rating <= 4.5:
            print('You are one of the good ones.')
        elif spy_rating >= 2.5 and spy_rating <= 3.5:
            print('You can always do better')
        else:
            print('We can always use somebody to help in the office. ')
    else:
        print('Sorry you are not of the correct age to become a spy.')  # entered age is not between 12 and 50
    print(
        'Authentication Complete. We are glad to have you with us. Welcome ' + spy_salutation + '.' + spy_name + ", Your spy rating is " + str(
            spy_rating))  # float value to string value
    spy_is_online = True
    print('Changing the status of spy from offline to online ' + str(
        spy_is_online))
    #call start chat
    start_chat(spy_name, spy_age, spy_rating)
# for continuing as a default user
elif user_option == 'Y' or user_option == 'y':

    print colored(
        'Authentication Complete. We are glad to have you with us. Welcome ' + spy_1.salutation + '.' + spy_1.name + ", Your spy rating is " + str(spy_1.rating),"blue")  # float value to string value
    spy_is_online = True

    start_chat(spy_1.name, spy_1.age, spy_1.rating)  # calling menu option
else:
    print colored("Please select default user or create a new one.","red")