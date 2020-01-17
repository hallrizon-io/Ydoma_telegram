# https://aiogram.readthedocs.io/en/latest/examples/middleware_and_antiflood.html
# https://surik00.gitbooks.io/aiogram-lessons/content/chapter5.html
import uvloop
import asyncio
from aiogram.utils import executor

from src.core import dp
from src.commands import *
from src.handlers import *

if __name__ == '__main__':
    uvloop.install()
    executor.start_polling(dp, skip_updates=False)
