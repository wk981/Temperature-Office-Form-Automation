import telebot
import sys
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv('API_KEY')
print(API_KEY)
chat_id = os.getenv('CHAT_ID')

bot = telebot.TeleBot(API_KEY)
bot.send_message(chat_id, "-----")
bot.send_message(chat_id, "First picture")

sys.exit('Bot is done')