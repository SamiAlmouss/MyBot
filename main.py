#main command and bot creation

import telebot
#from decouple import config

BOT_TOKEN = '5584371909:AAFlpqyAxuBC-VP7iaYStee3U04Fn-aWfPw'

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["start","help"])
def welcome(message):
    bot.send_message(message.chat.id,"Willkommen bei bot")

@bot.message_handler(commands=["bye"])
def bye(message):
    bot.send_message(message.chat.id,"Auf Wiedersehen")

def isMsg(message):
    return True

@bot.message_handler(func=isMsg)
def reply(message):
    words = message.text.split()
    if words[0].lower() == 'hi':
        bot.reply_to(message,"Hi " + message.chat.username +" Wie geht es dir")
    elif words[0].lower() == 'sami':
        bot.reply_to(message,"مرحبا سامي كيف حالك ..")
bot.polling()



