from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import os

storage = MemoryStorage()


bot = Bot(token="5726284724:AAGKcpJcXgE9ruzVzt07tP0jyzyYmJ4uNfY")
dp = Dispatcher(bot, storage=storage)

