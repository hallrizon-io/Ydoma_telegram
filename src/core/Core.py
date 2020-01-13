from aiogram import Dispatcher, Bot
from src.modules import storage

API_TOKEN = '965421230:AAHTHNNa-8TQ8eI-255g7GKpBDvZb-ZTcqs'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)
