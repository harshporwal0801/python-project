# Program to send message
# on Instagram using Python.

# importing Bot form instabot library.
from typing_extensions import Self
from instabot import Bot

# Creating bot variable.
bot = Bot()

# Login using bot.
bot.login(username="gun_gsss_",password="Ashish1@")

# Make a list of followers/friends
urer_ids = ["president_harshporwal"]

# Message
text = "Hi "

# Sending messages
bot.send_messages(text, urer_ids)


