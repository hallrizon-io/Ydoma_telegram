from .MainMenu import MainMenu
from .CategoryMenu import CategoryMenu
from .MenuTypes import MenuTypes


class FactoryMenu:
    @staticmethod
    def get_menu(_type: str):
        if _type == MenuTypes.category:
            return CategoryMenu()
        elif _type == MenuTypes.main:
            return MainMenu()
