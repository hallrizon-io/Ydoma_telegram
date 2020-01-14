import uvloop
from aiogram.utils import executor

from src.core import dp
from src.commands import *
from src.handlers import *

if __name__ == '__main__':
    uvloop.install()
    executor.start_polling(dp, skip_updates=True)
