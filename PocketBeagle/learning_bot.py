# bot.py

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Chatpot")

trainer = ListTrainer(chatbot)


trainer.train([
    "sleep",
    "I'll just turn off for a while",
    "Ok going to sleep now",
    "I'm going to hibernate to conserve battery",
])


trainer.train([
    "shutdown",
    "Shutting down interface",
])

trainer.train([
    "exit",
    "Shutting down interface",
])

trainer.train([
    "restart",
    "Rebooting subroutines",
])

trainer.train([
    "Hello",
    "Hi",
    "Hello",
    "Hiya",
    "Heya",
    "Hey",
])







exit_conditions = ("quit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"~ {chatbot.get_response(query)}")