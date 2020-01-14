from aiogram import types
from src.forms import RegisterForm
from src.core import dp, bot
from src.serializers import MessageSerializers
from src.modules import storage


@dp.message_handler(commands='help')
async def command_help(message: types.Message):
    """
    Conversation's entry point
    """
    # Set state

    # a = await message.answer("Suck my dick< Fucking stupid chicken?")
    serializer = MessageSerializers(message=message)
    await serializer.delete()

    # await message.reply("Suck my dick< Fucking stupid chicken?")
    # await bot.delete_message(message.chat.id, message.message_id)
