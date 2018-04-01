from steganography.steganography import Steganography
from select_friend import select_a_friend
from spy_details import friends, ChatMessage


def send_message():
    friend_choice = select_a_friend()

    original_image = raw_input("What is the name of the image?")
    output_path = 'output.jpg'
    text = raw_input("What do you want to say?")
    Steganography.encode(original_image, output_path, text)

    # the message will be stored in chat message class
    new_chat = ChatMessage(text, True)

    # along the name of friend with whom we add message
    friends[friend_choice].chats.append(new_chat)

    # Successful message after encoding
    print("Your message encrypted successfully.")

    # name of the friend along which we add message.
    friends[friend_choice].chats.append(new_chat)
    print("your secret message is ready.")
