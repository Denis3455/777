import telebot
from flask import Flask, request
import os

API_TOKEN = '7866948143:AAEDfS3gfFQfIOIWboZZ2ck-fsJON4p56qE'
bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

# Команда /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Это бот на Render.com!")

# Обработка всех текстов
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Вы сказали: " + message.text)

# Webhook обработчик
@app.route('/' + API_TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://your-app-name.onrender.com/' + API_TOKEN)
    return "Webhook установлен!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
