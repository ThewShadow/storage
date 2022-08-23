import time
import telebot
import flask
import bitrix24 as b24
import socket
from telebot import async_telebot

local_ip = socket.gethostbyname(socket.gethostname())

token = '5237614948:AAF1sfGVhikBmAb9BeN_2YeQj-n2akZjDBA'
webhook_url = f'https//:{local_ip}/bots/helper/'
#bot = telebot.TeleBot(token)
bot = async_telebot.AsyncTeleBot(token)

#bot.delete_webhook(timeout=2)
#bot.set_webhook(webhook_url, certificate=open('webhook.crt', 'r'), max_connections=5)

app = flask.Flask(__name__)

@app.route('/bots/helper')
def webhook_handler():
    json_data = flask.request.get_data().decode('utf-8')
    bot.process_new_updates(telebot.types.Update.de_json(json_data))

@bot.message_handler(commands=['start'])
async def start(message):
    await bot.send_message(message.chat.id, 'work')
    await someone(message)



async def someone(message):

    await bot.send_message(message.chat.id, 'start')
    await asyncio.sleep(10)
    bot.send_message(message.chat.id, 'end')

application = app

if __name__ == '__main__':
    import asyncio
    print('start server')
    asyncio.run(bot.polling())


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
