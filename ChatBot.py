
def get_response(user_input):
    user_input = user_input.lower().strip()

    if user_input in ["hello", "hi", "hey"]:
        return "Hi! How can I help you?"

    elif user_input == "how are you":
        return "I'm fine, thanks! How about you?"

    elif user_input in ["what is your name", "your name"]:
        return "I'm ChatBot, your virtual assistant."

    elif user_input in ["thank you", "thanks"]:
        return "You're welcome!"

    elif user_input in ["what can you do", "help"]:
        return "I can greet you, answer simple questions, and chat with you."

    elif user_input in ["bye", "goodbye", "exit"]:
        return "Goodbye! Have a nice day."

    else:
        return "Sorry, I don't understand that. Please try another message."


def chatbot():
    print("=" * 40)
    print("       WELCOME TO CHATBOT")
    print("=" * 40)
    print("Type 'help' to know what I can do.")
    print("Type 'bye' to end the conversation.")

    while True:
        user_input = input("\nYou: ")

        if user_input.strip().lower() in ["bye", "goodbye", "exit"]:
            print("ChatBot:", get_response(user_input))
            break

        response = get_response(user_input)
        print("ChatBot:", response)


chatbot()
