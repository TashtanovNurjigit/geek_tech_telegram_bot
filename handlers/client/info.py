from aiogram.types import Message
from aiogram import Dispatcher
from aiogram.types import ReplyKeyboardRemove


from bot import bot
from keyboards.client.info import client_keyboard


# students_list = [
#     "Аскаров Акыл",
#     "Акылбек у Арсен",
#     "Садырбеков Бекберди",
#     "Асланов Руслан", 
#     "Гусев Михаил", 
#     "Савенко Кирилл",
#     "Жолдошбеков Искендер", 
#     "Туратбеков Улукбек",  
#     "Жээнбеков Нурсултан", 
#     "Эрбол Салымбаев", 
#     "Таштанов Нуржигит",  
# ]


# example
# async def get_students(message: Message):
#     students = ""
#     for i in students_list:
#         students += f'{i}\n'
#     await message.answer(students)
##################


async def start_command(message: Message):
    await message.answer('Choose your next option', reply_markup=client_keyboard)


async def get_address(message: Message):
    await message.answer('Ибраимова 103')


async def get_courses_list(message: Message):
    await message.answer('Python, JavaScript, UI/UX, Android')



def register_client_handler(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start', 'help'])
    dp.register_message_handler(get_address, commands=['address'])
    dp.register_message_handler(get_courses_list, commands=['courses_list'])
    
    # dp.register_message_handler(get_students, commands=['python_students_list'])
