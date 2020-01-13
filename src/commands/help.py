from aiogram import types
from src.forms import RegisterForm
from src.core import dp


@dp.message_handler(commands='help')
async def command_help(message: types.Message):
    """
    Conversation's entry point
    """
    # Set state
    print('qwe')
    await message.answer("Suck my dick< Fucking stupid chicken?")
    await message.reply("Suck my dick< Fucking stupid chicken?")
