from aiogram import executor

from bot import dp
from handlers.client import info
from handlers.student import student 


async def on_startup(_):
    print('Запустился наш телеграм бот')


info.register_client_handler(dp)
student.register_student_handler(dp)


if "__main__" == __name__:
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
