from aiogram import types
from src.forms import RegisterForm
from src.core import dp, bot
from src.serializers import MessageSerializers
from src.modules import storage
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from src.menu.FactoryMenu import FactoryMenu
from src.menu.AbstractMenu import AbstractMenu


def create_bottom_menu():
    button1 = KeyboardButton('1️⃣')
    button2 = KeyboardButton('2️⃣')
    button3 = KeyboardButton('3️⃣')

    markup3 = ReplyKeyboardMarkup().add(
        button1).add(button2).add(button3)

    markup4 = ReplyKeyboardMarkup().row(
        button1, button2, button3
    )

    markup5 = ReplyKeyboardMarkup().row(
        button1, button2, button3
    ).add(KeyboardButton('Средний ряд'))

    button4 = KeyboardButton('4️⃣')
    button5 = KeyboardButton('5️⃣')
    button6 = KeyboardButton('6️⃣')
    markup5.row(button4, button5)
    markup5.insert(button6)
    return markup5


@dp.message_handler(commands='help')
async def command_help(message: types.Message):
    """
    Conversation's entry point
    """
    # Set state

    # a = await message.answer("Suck my dick< Fucking stupid chicken?")
    # v = create_bottom_menu()
    # await message.reply("Пятое - добавляем ряды кнопок", reply_markup=v)

    # markup_request = ReplyKeyboardMarkup(resize_keyboard=True).add(
    #    KeyboardButton('Отправить свой контакт ☎️', request_contact=True)
    # ).add(
    #    KeyboardButton('Отправить свою локацию 🗺️', request_location=True)
    # )
    # await MainMenu.show_menu(message)

    menu = FactoryMenu.get_menu(_type='main')
    serializer = MessageSerializers(message=message)
    await menu.send(chat_id=serializer.data.chat_id, user_id=serializer.data.user_id)
    del menu
    await serializer.delete()

    # await message.reply("Suck my dick< Fucking stupid chicken?")
    # await bot.delete_message(message.chat.id, message.message_id)
