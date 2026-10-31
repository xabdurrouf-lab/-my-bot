from flask import Flask, request
import telebot
import os
TOKEN = os.environ.get("TOKEN")
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Salom! Vercel da ishlayapman ✅")
@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.send_message(message.chat.id, f"Siz: {message.text}")
@app.route('/api', methods=['POST'])
def webhook():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return 'ok', 200
@app.route('/')
def home():
    return 'Bot ishlayapti!'
