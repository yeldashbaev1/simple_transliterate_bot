from transliterate import to_cyrillic, to_latin
import telebot

TOKEN = '6916790488:AAH1x00bCVi0lCaWTo25ijG4WhDrWT2ycTo' # You can ues your bot's token
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):  
    hi = "Welcome to our transliterator bot! \nInput any text:"
    bot.reply_to(message, hi)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    txt = message.text
    answer = lambda txt: to_cyrillic(txt) if txt.isascii() else to_latin(txt)
    bot.reply_to(message, answer(txt))

bot.polling()

