from abc import ABC, abstractmethod


class AbstractMenu(ABC):

    @abstractmethod
    def builder_menu(self, keyboard_markup):
        """
            This method generate menu  for telegram
            :return InlineKeyboardMarkup or ReplyKeyboardMarkup:
        """

    @abstractmethod
    async def send(self, chat_id, user_id):
        """
        Send menu to user depend by type
        :return None:
        """
