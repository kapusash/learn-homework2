"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

"""
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem
import logging
import datetime

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot1.log'
                    )
now = str(datetime.datetime.now())

planets = ('Mars','Neptune')

def planet_ephem(bot, update):
    user_text = update.message.text.split()
    planet = user_text[-1]
    print(getattr(ephem,planet))
    if planet in planets:
        update.message.reply_text(ephem.constellation(getattr(ephem, planet)(now)))
    else:
        update.message.reply_text('Такой планеты не сущетсвует')

def word_count(bot, update):
    user_text = update.message.text.split()
    if '-' in user_text:
        user_text.remove('-') #в случае ввода символа - 
    user_text = user_text[1:]
    update.message.reply_text(f'Количество слов: {len(user_text)}')

def next_full_moon(bot, update):
    user_text = update.message.text.split()
    if len(user_text) == 1:
        update.message.reply_text(f'Повторите снова и укажите дату')
    else:
        update.message.reply_text(ephem.next_full_moon(user_text[1]))

def main():
    mybot = Updater("907371138:AAGn-c7o5in-bBCen9M9FOVsob8XWvgIQbI", request_kwargs=PROXY)
    
    logging.info('Бот запускается')

    dp = mybot.dispatcher 
    dp.add_handler(CommandHandler('planet', planet_ephem))
    dp.add_handler(CommandHandler('wordcount', word_count))
    dp.add_handler(CommandHandler('next_full_moon', next_full_moon))

    mybot.start_polling()
    mybot.idle()

main()