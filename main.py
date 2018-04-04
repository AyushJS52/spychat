# Importing the details of the spy
from spy_details import spy, Spy, friends, ChatMessage


from steganography.steganography import Steganography


STATUS_MESSAGES = ['My name is Ayush', "Live and Let Die",
                   "Diamonds are forever", "Disappointed and not surprised"]

# Let's start by greeting.
print("Hello!")

# Ask the spy whether he wants to continue with the default spy or create a new user
question = "Do you want to continue as the default user-" + spy.salutation + " " + spy.name + " or create a new user? (Y/N): "
existing = raw_input(question,)


# Adding a status
def add_status():
    updated_status_message = None

    # check if current status message is set or not
    if spy.current_status_message is not None:
        print 'Your current status message is %s \n' % spy.current_status_message
    else:
        print 'You don\'t have any status message currently \n'

    # Asking if the user wants to select a default status or a status which is already present
    default = raw_input("Do you want to select from the older status (y/n)? ")

    # .upper() converts from any case to upper case
    if default.upper() == "N":
        # ask the user to enter a new status
        new_status_message = raw_input("What status message do you want to see?: ")

        # if valid status message is entered
        if len(new_status_message) > 0:
            # in the existing status list add the new status
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message

    # A spy wants to choose from the existing status
    elif default.upper() == 'Y':

        # To give an index number to the statuses
        item_position = 1

        # To show all the default statuses
        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        # Ask the user which index of the list he wants to choose.
        message_selection = int(raw_input("\nChoose the index of the status: "))

        # Check if the position exists
        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    # When the user chooses neither yes nor no
    else:
        print 'The option you chose is not valid! Press either Y or N.'

    # When the status message is updated
    if updated_status_message:
        print 'Your updated status message is:',
        print(updated_status_message)

    # When it is not updated
    else:
        print('You did not update your status message')

    # The updated message will be read
    return updated_status_message


# Function to add a friend to this chat
from spy_details import Spy, friends


def add_friend():
    # using class user in spy_details
    new_friend = Spy(" ", " ", 0, 0.0)
    
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

    # concatination
    new_friend.name = new_friend.salutation + " " + new_friend.name

    # ask for age of friend
    new_friend.age = int(raw_input("Age: "))

    if 12 < new_friend.age < 50:
        True
    else:
        print("Age should be in between 12 to 50")
        return add_friend()

    new_friend.rating = float(raw_input("Spy rating? "))

    if new_friend.rating > 0.0:
        True
    else:
        print("Ratting should be more than 0.0")
        return add_friend()

    # add friend if all conditions check
    friends.append(new_friend)
    print('Friend Added!')

    # check total no of friends in a list.
    return len(friends)


# Function to select a friend from the friends list
def select_a_friend():
    # indexing the position of a friend
    item_number = 0

    # To select a friend with the indexing
    for friend in friends:
        print '%d. %s %s aged %d with rating %.2f is online' % (item_number + 1, friend.salutation, friend.name, friend.age, friend.rating)

        item_number = item_number + 1

    # Ask the user which friend he want to have a chat with
    friend_choice = raw_input("Choose the index of the friend: ")
    # The friend will be selected
    friend_choice_position = int(friend_choice) - 1

    # Check if the user chooses index out of range
    if friend_choice_position + 1 > len(friends):
        print("Sorry,This friend is not present.")
        exit()

    else:
        # returns the selected friend to perform the options
        return friend_choice_position


# Function to send a secret message
def send_a_message():
    # Select a friend
    friend_choice = select_a_friend()

    # Select the image
    original_image = raw_input("What is the name of the image?: ")

    # the output path of the image
    output_path = "output.jpg"
    # write the secret message
    text = raw_input("What do you want to say? ")

    # The library steganography that helps to encode the message
    Steganography.encode(original_image, output_path, text)

    # The text message wil be stored in chat messages
    new_chat = ChatMessage(text, True)

    # Along with the name of the friend we add the message
    friends[friend_choice].chats.append(new_chat)

    # After the encoding is done the message is ready.
    print("Your secret message image is ready!")


# Read the secret message sent by a friend.
def read_a_message():
    # Select a friend to communicate with
    sender = select_a_friend()
    output_path = raw_input("What is the name of the image file?: ")
    secret_text = Steganography.decode(output_path)
    print "The secret message you read is"
    print (secret_text)


def start_chat(spy):
    # updated variable
    spy.name = spy.salutation + " " + spy.name
    # Age cannot be less than 12 or greater than 50
    if 12 < spy.age < 50:

        # Authentication complete
        # Show a message with all te spy details
        print"Authentication complete."
        print("Welcome " + str(spy.name))
        print("Your age:" + str(spy.age))
        print("Your rating:"+str(spy.rating))
        print("Bravo!Proud to have you on board.")

        show_menu = True
        while show_menu:
            menu_choices = "What do you want to do? \n 1. Add a status update \n" \
                           " 2. Add a friend \n 3. Send a secret message \n " \
                           "4. Read a secret message \n 5. Read Chats from a user \n" \
                           " 6. Close Application \n"
            # Taking the input of the choice
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    # Set your current status
                    spy.current_status_message = add_status()

                elif menu_choice == 2:
                    # Add a new friend
                    number_of_friends = add_friend()
                    print 'You have %d friends' % number_of_friends

                elif menu_choice == 3:
                    # Send a secret message
                    send_a_message()

                elif menu_choice == 4:
                    # Read the secret message sent by your friend
                    read_a_message()

                elif menu_choice == 5:
                    # Read the chat history
                    print('Read Chat history')

                elif menu_choice == 6:
                    # Close the app
                    print("Successfully closed")
                    show_menu = False

                # When the user chooses other than the menu choices.
                else:
                    print("That was a wrong choice.")
                    exit()

    else:
        # age is less than 12
        if spy.age <= 12:
            print("Sorry, you are too young to become a spy!")
        # age is greater than equal to 50
        elif spy.age >= 50:
            print("Sorry, you are too old to be a spy!")


# if the user chooses the default spy
if existing.upper() == "Y":
    # start the chat function is called
    start_chat(spy)
# the user wants to add a new user
elif existing.upper() == "N":
    # declare variables using a class
    spy = Spy(" ", " ", 0, 0.0)

    # Ask for the name
    spy.name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

    # Check if the name is entered or not
    if len(spy.name) > 0 and spy.name.isdigit() == False:
        # ask for the salutation
        spy.salutation = raw_input("What should we call you? Mr. or Ms.?")
        # check if salutation is entered or not
        if len(spy.salutation) > 0:

            # Ask for the age of the spy
            spy.age = raw_input("Please enter your age: ")

            if len(spy.age) > 0:
                # raw input always gives a string to typecast age to int.
                spy.age = int(spy.age)
                # Age cannot be less than 12 and greater than 50
                # nested if
                if 12 <= spy.age < 50:
                    print("Welcome to Spy community")

                    # Ask for spy_rating
                    spy.rating = raw_input("Please enter your spy rating: ")
                    if len(spy.rating) > 0:
                        # raw input always gives a string to typecast rating to float.
                        spy.rating = float(spy.rating)

                        # conditions to pass comments according to the spy_rating.
                        if spy.rating > 4.5:
                            print("Great Ace!")
                        elif 3.5 <= spy.rating <= 4.5:
                            print("You are one of the good ones!")
                        elif 2.5 <= spy.rating <= 3.5:
                            print("You can always do better.")
                        else:
                            print("We will get someone to help you.")

                        # Make the spy come online
                        spy.is_online = True

                        # Call the start_chat function to start
                        start_chat(spy)

                    # If spy rating is not entered
                    else:
                        print "Enter a valid spy rating"

                # valid age is not entered
                else:
                    # age is less than 12
                    if spy.age <= 12:
                        print("Sorry, you are too young to become a spy!")
                    # age is greater than equal to 50
                    elif spy.age >= 50:
                        print("Sorry, you are too old to be a spy!")
                    else:
                        print("Please enter a valid age")

            # if age is not entered
            else:
                print("Please enter your age")

        # the salutation is not entered
        else:
            print("Please enter a valid salutation")

    # the name is not entered
    else:
        print("Please enter a valid name")

else:
    print("You did not reply with a yes(Y) or no(N)!")
    print("Need to run the program again.")
    exit()
