import random

conversation_responses = {
    'hi':['Hiii...'],
    'good morning':['Good morning buddy...'],
    'good evening':['Good evening bubby...'],
    'good afternoon':['Good afternoon buddy...'],
    'good night':['Good night buddy...'],
    'how are you':['iam Good,thanks for asking...hopping You good!'],
    'what is your name':['My name is chatbot'],
    'what are you do':['iam here to talk with you...'],
    'can you eat food':['no i cannot eat because iam machine!'],
    'do you have feelings':['No...machines donot have any feelings!'],
    'who is your boss':['my boss is dileep medisetti'],
    
}


def chatbot():
    print("Hello BUDDY! I'm your chatbot.I am here to chat with you,how can i help you..!")
    while True:
        user_input = input("You: ").lower()
        if user_input == "bye":
            print("Byee bubby!...see you later, Have a great day!")
            break
        response = conversation_responses.get(user_input, ["I'm not sure what to say to that."])
        print("Bot:", random.choice(response))



if __name__ == "__main__":
    chatbot()