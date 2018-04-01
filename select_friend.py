from spy_details import friends


# select friend from friend list.
def select_a_friend():

    # indexing position.
    counter = 1

    # to select a friend with indexing
    for friend in friends:
        print(str(counter) + ". " + friend.uname + " Age : " + str(friend.age))

        counter = counter + 1       # access all list.

    # ask user to select friend.
    friend_choice = int(raw_input("\nSelect from the list : "))
    #  selected friend to perform action
    friend_choice_position = int(friend_choice) - 1

    # Check if user has out of index choice.
    if friend_choice_position + 1 > len(friends):
        print("Sorry, this friend is not present.")
        exit()
    else:
        # returns the selected friend to perform actions
        return friend_choice_position
