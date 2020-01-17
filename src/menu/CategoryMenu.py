from src.core import bot
from src.modules import storage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from .AbstractMenu import AbstractMenu


class CategoryMenu(AbstractMenu):

    def __init__(self):
        self.markup = self.builder_menu(ReplyKeyboardMarkup)

    def builder_menu(self, keyboard_markup):
        button4 = KeyboardButton('aaa')

        return keyboard_markup(resize_keyboard=True).row(
            button4)

    async def send(self, chat_id, user_id):
        await storage.set_data(chat=chat_id, user=user_id, data={
            'action': 'main'
        })
        await bot.send_message(chat_id=chat_id, parse_mode='Markdown', text='Главное меню',
                               reply_markup=self.markup)
