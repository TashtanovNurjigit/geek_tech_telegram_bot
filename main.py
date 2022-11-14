from aiogram import executor

from bot import dp
from handlers.client.info import register_client_handler


async def on_startup(_):
    print('Запустился наш телеграм бот')


register_client_handler(dp)


if "__main__" == __name__:
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
