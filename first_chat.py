"""Chat bot project

The code comes from:
https://towardsdatascience.com/
building-a-chatbot-in-python-the-beginners-guide-2743ad2b4851

Minor revision: James ODonnell
DATE: March 11, 2021
"""

import random

#prompt = "BOT: hello, " + user_name + " what would you like to talk about? "
bot_name = "Funny Bot 101" 
weather = "rainy" 
mood = "Happy"

user_name = input("BOT: What do you want me to call you?")
prompt = "{}: Great, {}! Do you have something to ask me?".format(bot_name,
                                                                       user_name)

response = input(prompt)
if "weather" in response:
    print("Today it is {}".format(weather))
