TOKEN = '965421230:AAHTHNNa-8TQ8eI-255g7GKpBDvZb-ZTcqs'
'https://docs.aiogram.dev/en/latest/install.html'

import aiogram.utils.markdown as md
from aiogram import types

from aiogram.dispatcher import FSMContext

from aiogram.types import ParseMode
from aiogram.utils import executor

from src.forms import RegisterForm
from src.modules import logging
from src.core import dp, bot
from src.commands import *

@dp.message_handler(state=RegisterForm.name)
async def process_name(message: types.Message, state: FSMContext):
    """
    Process user name
    """

    async with state.proxy() as data:
        data['name'] = message.text

    await RegisterForm.next()
    await message.reply("How old are you?")


# Check age. Age gotta be digit
@dp.message_handler(lambda message: not message.text.isdigit(), state=RegisterForm.age)
async def process_age_invalid(message: types.Message):
    """
    If age is invalid
    """
    return await message.reply("Age gotta be a number.\nHow old are you? (digits only)")


@dp.message_handler(lambda message: message.text.isdigit(), state=RegisterForm.age)
async def process_age(message: types.Message, state: FSMContext):
    # Update state and data
    await RegisterForm.next()
    await state.update_data(age=int(message.text))

    # Configure ReplyKeyboardMarkup
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add("Male", "Female")
    markup.add("Other")

    await message.reply("What is your gender?", reply_markup=markup)


@dp.message_handler(lambda message: message.text not in ["Male", "Female", "Other"], state=RegisterForm.gender)
async def process_gender_invalid(message: types.Message):
    """
    In this example gender has to be one of: Male, Female, Other.
    """
    return await message.reply("Bad gender name. Choose your gender from the keyboard.")


@dp.message_handler(state=RegisterForm.gender)
async def process_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['gender'] = message.text

        # Remove keyboard
        markup = types.ReplyKeyboardRemove()
        # And send message
        logging.info('Cancelling state %r', message.message_id)

        for i in range(0, message.message_id):
            try:
                await bot.delete_message(state.chat, i)
            except:
                pass

        await bot.send_message(
            message.chat.id,
            md.text(
                md.text('Hi! Nice to meet you,', md.bold(data['name'])),
                md.text('Age:', md.code(data['age'])),
                md.text('Gender:', data['gender']),
                sep='\n',
            ),
            reply_markup=markup,
            parse_mode=ParseMode.MARKDOWN,
        )

    # Finish conversation
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
