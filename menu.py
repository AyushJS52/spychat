from add_status import status_message
from add_friend import add_friend


def start_chat():
    from spy_details import current_status_message
    show_menu = True
    while show_menu:
        menu_choices = "What do you want to do? \n 1. Add a status update \n " \
                   "2. Add a friend \n 3. Send a secret message \n " \
                   "4. Read a secret message \n 5. Read chats from a user \n 6. Close application \n"
        menu_choice = int(raw_input(menu_choices))

        if menu_choice == 1:
            current_status_message = status_message(current_status_message)

        elif menu_choice == 2:
            number_of_friends = add_friend()
            print('You have %d friends' % number_of_friends)

        elif menu_choice == 3:
            # send a secret message
            print('send secret msg')

        elif menu_choice == 4:
            # read the secret message sent by friend
            print('Read secret msg')

        elif menu_choice == 5:
            # read the chat history
            print('Read chats form a user')

        elif menu_choice == 6:
            # close application
            print('close application')
            show_menu = False

        # if user chooses other than menu choices.
        else:
            print("wrong choice try again.")
            exit()
