from spy_details import user_1
from menu import start_chat


print("THE SPY CHAT!")

question = "Do you want to continue as " + user_1.uname + " (Y/N): "
existing = raw_input(question)


# for existing user
if existing.upper() == "Y":
        import spy_details
        print('WELCOME '+user_1.uname)
        # starting chat application.
        start_chat(user_1.uname, user_1.age, user_1.rating)

# for a new user
elif existing.upper() == "N":
        # asking names
        spy_name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")
        # checking length of the name
        if len(spy_name) > 0:
            # asking for salutation
            spy_salutation = raw_input("What would you like us to call you (Mr. or Ms.) ?")
            spy_name = spy_salutation + spy_name

            print("Alright " + spy_name + " I'd like to know a little bit more about you...")
            # checking age
            spy_age = int(raw_input("What's your age?"))
            if 12 < spy_age < 50:
                # checking rating
                spy_rating = float(raw_input("What is your spy rating?"))
                if spy_rating > 4.5:
                    print("Outstanding!")
                elif 3.5 < spy_rating <= 4.5:
                    print("Amazing!")
                elif 2.5 <= spy_rating <= 3.5:
                    print("You can surely improve!")
                else:
                    print("Don't Worry! We'll help you!")
                # if spy is online
                spy_is_online = True
                # welcome with details
                print("Authentication complete.")
                print("Welcome "+spy_name+" your age is "+str(spy_age)+" and rating is "+str(spy_rating)+"!")
                print("Proud to have you on board!")

                start_chat(spy_name, spy_age, spy_rating)
            # age is not eligible
            else:
                print("Sorry you are not of the correct age to be a spy")
        # name not provided
        else:
            print("Please provide us with your name first. Try again please.")
# entry not valid
else:
        print("Please enter default or create.")
