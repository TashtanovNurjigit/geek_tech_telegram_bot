from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from handlers.client.info import students_dict
from bot import dp

from states.students import StudentFSMAdmin


students_list = list(students_dict.keys())


async def choice_students(message: types.Message):
    name_students = ''
    for name in students_list:
        name_students += f'{name}\n'
    await message.reply(f'Введите имя ученика:\n{name_students}')

    @dp.message_handler()
    async def get_grade(message: types.Message):
        await message.reply(students_dict.get(message.text))


# @dp.message_handler(commands=['request'], state=None)
async def create_student(message: types.Message):
    # await StudentFSMAdmin._id
    await StudentFSMAdmin.name.set()

    await message.reply('Введите ваше имя')

    # await message.answer('Отправьте фото')

    # await StudentFSMAdmin.course


# @dp.message_handler(state=StudentFSMAdmin.name)
async def set_student_name(message: types.Message, state: FSMContext):
    # print(dir(state))
    # await state.set_state(StudentFSMAdmin.name)
    # print('='*80)
    async with state.proxy() as data:
        # print(data)
        data['name'] = message.text
        # print(state.data)
        current_state = await state.get_state()
        # print(current_state)
        # print(StudentFSMAdmin.states_names.index(current_state) + 1)
        await StudentFSMAdmin.photo.set()

    await message.reply('Отправьте фото')
    await StudentFSMAdmin.next()
    # await StudentFSMAdmin.photo.set()

    # await stat.set_state(StudentFSMAdmin.photo)


# @dp.message_handler(state=StudentFSMAdmin.photo)
async def set_student_photo(message: types.Message, state: FSMContext):
    print('-' * 80)
    async with state.proxy() as data:
        print(data)
        print('=' * 80)
        # data['photo'] = message.photo[0].file_id
    await StudentFSMAdmin.next()
    await message.answer('Выберите курс (Python, JavaScript, etc..)')


# # @dp.message_handler(commands=['course'], state=StudentFSMAdmin.course)
# async def set_student_course(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         # data['course'] = message.text
#         pass

#     async with state.proxy() as data:
#         await message.answer(str(data))
#         # add data to database here

#     await state.finish()
#     await message.answer('Готово')


def register_student_handler(dp: Dispatcher):
    dp.register_message_handler(choice_students, commands=['grade'])
    dp.register_message_handler(create_student, commands=['request'], state=None)
    dp.register_message_handler(set_student_name, state=StudentFSMAdmin.name)
    dp.register_message_handler(set_student_photo, state=StudentFSMAdmin.photo)
    # dp.register_message_handler(set_student_course, state=StudentFSMAdmin.course)
