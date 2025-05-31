from PySide6.QtWidgets import QDialog

from core import Database
from windows_design import AddDataWindow


class AddProduct(QDialog):
    def __init__(self):
        super().__init__()

        self._ui = AddDataWindow()
        self._ui.setupUi(self)

        self.connect = Database.get_connection()

        self.article = None
        self.name = None
        self.category = None
        self.price = None
        self.description = None
        self.image_path = None

        self.setup_actions()
        self.fill_preset_field()

    def setup_actions(self):
        pass

    def fill_preset_field(self):
        self.set_article()

    def set_article(self):
        pass

    def get_article(self) -> int:
        pass


