from aiogram import types
from src.core import dp, bot
from src.serializers import MessageSerializers
from src.modules import storage
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from .AbstractMenu import AbstractMenu


class MainMenu(AbstractMenu):

    def __init__(self):
        self.markup = self.builder_menu(ReplyKeyboardMarkup)

    def builder_menu(self, keyboard_markup):
        button1 = KeyboardButton('1️⃣')
        button2 = KeyboardButton('2️⃣')
        button3 = KeyboardButton('3️⃣')
        button4 = KeyboardButton('aaa')

        return keyboard_markup(resize_keyboard=True).row(
            button1, button2, button3, button4)

    async def send(self, chat_id, user_id):
        await storage.set_data(chat=chat_id, user=user_id, data={
            'action': 'main'
        })
        await bot.send_message(chat_id=chat_id, parse_mode='Markdown', text='Главное меню',
                               reply_markup=self.markup)
