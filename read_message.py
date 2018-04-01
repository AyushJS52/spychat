from steganography.steganography import Steganography
from select_friend import select_a_friend
from spy_details import friends, ChatMessage


def read_message():
    sender = select_a_friend()

    output_path = raw_input("What is the name of the file?")
    secret_text = Steganography.decode(output_path)
    print(secret_text)

    # add the chat to sender
    new_chat = ChatMessage(secret_text, False)
    friends[sender].chats.append(new_chat)
    print("Your secret message has been saved.")
