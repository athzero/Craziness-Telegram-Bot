from aiogram import Bot, types 
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os 
import config

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands=['Start'])
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, 'l\'m a crazy bot, I will repeat every thing you will write :)')

@dp.message_handler()
async def echo_send(message: types.Message):
    await message.answer(message.text)
executor.start_polling(dp, skip_updates =True)