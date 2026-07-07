# Rule based AI chatbot
def get_input():
    raw_input = input("You : ")
    clean_input = raw_input.strip().lower()
    return clean_input

def process(user_input):
    responses = {
        "hello": "Hello! How can I help you today?",
        "hi": "Hi there! What can I do for you?",
        "how are you": "I'm doing well, thank you for asking!",
        "what is your name": "I'm AI chatbot.",
        "what can you do": "I can answer simple questions and chat with you.",
        "thank you": "You're welcome!",
        "thanks": "No problem!",
        "bye": "Goodbye! Have a great day!",
        "help": "Try saying hello, asking how I am, or asking what I can do."
    }
    reply = responses.get(user_input)
    if not reply:
        if "name" in user_input:
            reply = "I'm AI chatbot."
        elif "help" in user_input or "what" in user_input:
            reply = "I can answer simple questions like greeting, asking how I am, or saying thanks."
        else:
            reply = "I'm sorry, I don't understand that."
    print("Bot : " + reply)

print("Welcome to the chatbot. Type 'exit' to quit.")
while True:
    user_input = get_input()
    if user_input == "exit":
        print("Bot : Goodbye! Have a great day!")
        break
    process(user_input)
