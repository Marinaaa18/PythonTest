#config.py
TOKEN='6919263526:AAFjgKqY8tYdy6ZgJhaaRG8FTukrMLWMZMM'

#bot.py
import asyncio
import requests
BASE_URL = 'https://api.telegram.org/bot'
from config import TOKEN
def get_updates():
    r = requests.get(f'{BASE_URL}{TOKEN}/getUpdates')
    message = r.json()['result'][-1]['message']['text']
    user_id = r.json()['result'][-1]['message']['chat']['id']
    requests.get(f'{BASE_URL}{TOKEN}/sendMessage?chat_id={user_id}&text={message}')
get_updates()