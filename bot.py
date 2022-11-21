from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import os
from decouple import config


storage = MemoryStorage()
TOKEN = config('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)

