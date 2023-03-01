import os
from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, CallbackQueryHandler, Filters




from main import(inline_handlerlar,back,city,start,Duvo,Toshkent,Fargona,Andijon,Namangan,Buxoro,Guliston,Jizzax,Zarafshon,Qarshi,Nukus,Navoiy,Samarqand,Termiz,Denov,Xiva,Urganch)

app = Flask(__name__)

# bot
TOKEN = os.environ['TOKEN']
bot = Bot(token=TOKEN)


@app.route('/webhook', methods=['POST', 'GET'])
def main():
    if request.method == 'GET':
        return 'hello'

    elif request.method == 'POST':
        data = request.get_json(force=True)

        dispatcher:Dispatcher = Dispatcher(bot, None , workers=0)

        update:Update = Update.de_json(data, bot)
# Add handler for photo message
#        dp.add_handler(MessageHandler(Filters.photo,photo))
        dp.add_handler(MessageHandler(Filters.text('🕌 Zarafshon'),Zarafshon))
        dp.add_handler(MessageHandler(Filters.text('🕌 Jizzax'),Jizzax))
        dp.add_handler(MessageHandler(Filters.text('🕌 Guliston'),Guliston))
        dp.add_handler(MessageHandler(Filters.text('🕌 Buxoro'),Buxoro))
        dp.add_handler(MessageHandler(Filters.text('🕌 Namangan'),Namangan))
        dp.add_handler(MessageHandler(Filters.text('🕌 Qarshi'),Qarshi))
        dp.add_handler(MessageHandler(Filters.text('🕌 Navoiy'),Navoiy))
        dp.add_handler(MessageHandler(Filters.text('🕌 Nukus'),Nukus))
        dp.add_handler(MessageHandler(Filters.text('🕌 Samarqand'),Samarqand))
        dp.add_handler(MessageHandler(Filters.text('🕌 Termiz'),Termiz))
        dp.add_handler(MessageHandler(Filters.text('🕌 Denov'),Denov))
        dp.add_handler(MessageHandler(Filters.text('🕌 Xiva'),Xiva))
        dp.add_handler(MessageHandler(Filters.text('🕌 Urganch'),Urganch))

        dp.add_handler(MessageHandler(Filters.text('🕌 Fargʻona'),Fargona))
        dp.add_handler(MessageHandler(Filters.text('🕌 Andijon'),Andijon))
        dp.add_handler(MessageHandler(Filters.text('🕌 Toshkent'),Toshkent))
        dp.add_handler(MessageHandler(Filters.text('🗒 Duvo'),Duvo))
        dp.add_handler(MessageHandler(Filters.text('♻️ Orqaga'),start))

        dispatcher.process_update(update)
    return "Assalomu alaykum"


#if __name__ == '__main__':
    
 #   app.run()
bot=Bot(TOKEN)

#print(bot.set_webhook('https://ramazontaqvimibot.pythonanywhere.com/webhook'))
#print(bot.delete_webhook())
#print(bot.get_webhook_info())

