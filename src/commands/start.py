from aiogram import types
from src.forms import RegisterForm
from src.core import dp


@dp.message_handler(commands='start')
async def command_start(message: types.Message):
    """
    Conversation's entry point
    """
    # Set state
    await RegisterForm.name.set()

    await message.reply("Hi there! What's your name?")
