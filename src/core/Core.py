import os
from dotenv import load_dotenv

from aiogram import Dispatcher, Bot
from src.modules import storage

load_dotenv()

API_TOKEN = os.getenv("TELEGRAM_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)
