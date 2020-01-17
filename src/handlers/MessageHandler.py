import aiogram.utils.markdown as md
from aiogram import types

from aiogram.dispatcher import FSMContext
from aiogram.types import ParseMode

from src.forms import RegisterForm
from src.modules import logging, storage
from src.core import dp, bot


@dp.message_handler()
async def echo(message: types.Message):
    print(storage.data)
    print(message)
