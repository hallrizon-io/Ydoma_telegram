import collections
from aiogram.utils.exceptions import MessageToDeleteNotFound
from src.core import bot

Message = collections.namedtuple('Message', 'message_id chat_id user_id first_name last_name username')


class MessageSerializers:
    def __init__(self, message):
        self.Message: Message = Message(message_id=message.message_id,
                                        chat_id=message.chat.id,
                                        user_id=message.from_user.id,
                                        last_name=message.from_user.last_name,
                                        first_name=message.from_user.first_name,
                                        username=message.from_user.username)

    @property
    def data(self):
        return self.Message

    async def delete(self):
        try:
            await bot.delete_message(chat_id=self.Message.chat_id, message_id=self.Message.message_id)
        except MessageToDeleteNotFound:
            pass
