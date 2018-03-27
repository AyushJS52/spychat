from menu import start_chat

print("WELCOME TO SPYCHAT")

spy_name = raw_input("Whats your spy name")

if len(spy_name) > 0:

    spy_salutation = raw_input("What should we call you (Mr. or Ms.)?")  ##taking the salutation

    spy_name = spy_salutation + "" + spy_name #concatenating

    print("Alright " + spy_name + " I'd like to know a little bit more about you...")

else:
    print("Please provide us with your name first!")
    # valid entry




print("WELCOME TO SPYCHAT")

default_user = raw_input("Do you wish to continue with the default user(Y or N)? ,If No create a new user")

# press 'Y' for the default user & 'N' to create a new user #

# for default user #
if default_user == 'Y'or default_user == 'y':
    print("continue")
    import spy_details    ##import the spy details from another spy_details file #

    print("Welcome to the spy chat " + spy_salutation + " " + spy_name) ### printing details of a default user####
    print("Alright " + spy_salutation + " " + spy_name + " I'd like to know a little bit more about you...")


# for a new user #
elif default_user == 'N' or default_user == 'n':
    # asking new spy name
    spy_name = raw_input("What's your name?")
    # checking length of the name
    if len(spy_name) > 0:
        #welcome new user
        print("Welcome "+spy_name+" Glab to have you with us")
        # asking for spy salutation
        spy_salutation = raw_input("What would you like us to call you (Mr., Ms. or Mrs.) ?")
        # welcoming spy
        print("Welcome to the spy chat " + spy_salutation + " " + spy_name)
        print("Alright " + spy_salutation + " " + spy_name + " I'd like to know a little bit more about you...")
    # name not provided
    else:
        print("Please provide us with your name first!")
        # valid entry
else:
    print("Please enter default or create.")
        # checking spy age
spy_age = int(raw_input("What's your age?"))
if spy_age > 12 and spy_age < 50:
    # checking spy rating
    spy_rating = float(raw_input("What is your spy rating?"))
    if spy_rating > 4.5:
        print("Outstanding!")
    elif spy_rating > 3.5 and spy_rating <= 4.5:
        print("Amazing!")
    elif spy_rating >= 2.5 and spy_rating <= 3.5:
        print("You can surely improve!")
    else:
        print("Don't Worry! We'll help you!")
        # if spy is online
else:
    print("You are not ready to be a spy yet!")
            # name not provided

spy_is_online = True
            # welcome with details
print("Authentication complete. Welcome " + spy_name + " age: " + str(spy_age) + " and rating of: " + str(spy_rating) + " Proud to have you onboard")
        # age is not eligible

#starting the chat application
start_chat()
