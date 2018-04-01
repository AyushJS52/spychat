from spy_details import User, friends


def add_friend():
    # using class user in spy_details
    new_friend = User(" ", " ", 0, 0.0)

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

    # ask for age of friend
    new_friend.age = int(raw_input("Age: "))

    if 12 < new_friend.age < 50:
        True
    else:
        print("Age should be in between 12 to 50")
        return add_friend()

    #ask for rating of friend, using float
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
