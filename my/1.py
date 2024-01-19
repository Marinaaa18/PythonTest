from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import TOKEN
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands="test1")
async def cmd_test1(message: types.Message):
   await message.reply("Test 1")


@dp.message_handler()
async def echo_message(msg: types.Message):
   await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
   executor.start_polling(dp)

import asyncio
import requests
BASE_URL = 'https://api.telegram.org/bot'
TOKEN = 'Ваш токен'
def get_updates():
    r = requests.get(f'{BASE_URL}{TOKEN}/getUpdates')
    message = r.json()['result'][-1]['message']['text']
    user_id = r.json()['result'][-1]['message']['chat']['id']
    requests.get(f'{BASE_URL}{TOKEN}/sendMessage?chat_id={user_id}&text={message}')
get_updates()