"""Chat bot project

The code comes from:
https://towardsdatascience.com/
building-a-chatbot-in-python-the-beginners-guide-2743ad2b4851
AUTHOR: Behic Guven
MINOR REVISION: James ODonnell
DATE: March 11, 2021
"""
import random

user_name = input("BOT: What do you want me to call you?")

bot_template = "BOT : {0}"
user_template = user_name + " : {0}"

prompt = "BOT: hello, " + user_name + " what would you like to talk about? "
name = "Funny Bot 101" 
weather = "rainy" 
mood = "Happy"

responses = { 
    "what's your name?": [ 
        "They call me {0}".format(name), 
        "I usually go by {0}".format(name), 
        "My name is the {0}".format(name) ],
    "what's today's weather?": [ 
        "The weather is {0}".format(weather), 
        "It's {0} today".format(weather), 
        "Let me check, it looks {0} today".format(weather) ],
    "are you a robot?": [ 
        "What do you think?", 
        "Maybe yes, maybe no!", 
        "Yes, I am a robot with human feelings.", ],
    "how are you?": [ 
        "I am feeling {0}".format(mood), 
        "{0}! How about you?".format(mood), 
        "I am {0}! How about yourself?".format(mood), ],
    "": [ 
        "Hey! Are you there?", 
        "What do you mean by saying nothing?", 
        "Sometimes saying nothing tells a lot :)", ],
    "default": [ 
        "Hey! Are you there?", 
        "What do you mean by saying nothing?", 
        "Sometimes saying nothing tells a lot :)",] }

def respond(message):
    if message in responses: 
        bot_message = random.choice(responses[message])
    else: 
        bot_message = random.choice(responses["default"])
    return bot_message

def related(x_text):
    if "name" in x_text:
        y_text = "what's your name?"
    elif "weather" in x_text:
        y_text = "what's today's weather?"
    elif "robot" in x_text:
        y_text = "are you a robot?"
    elif "how are" in x_text:
        y_text = "how are you?"
    else:
        y_text = ""
    return y_text

def send_message(message):  
  print(user_template.format(message))
  response = respond(message) 
  print(bot_template.format(response))

while 1:
  my_input = input(prompt) 
  my_input = my_input.lower() 
  related_text = related(my_input) 
  send_message(related_text)
  prompt = "is there anything else, {}".format(user_name)
  #my_input = input()
  if my_input == "exit" or my_input == "stop":
      break


