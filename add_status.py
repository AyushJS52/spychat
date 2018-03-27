from spy_details import current_status_message


def status_message():
    #check current status message
    if current_status_message != None:
        print('Your current status message is %s \n' % current_status_message)
    else:
        print('You don\'t have any status message currently \n')
