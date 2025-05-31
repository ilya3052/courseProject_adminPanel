import random

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QDialog
from icecream import ic
from psycopg import sql
import psycopg as ps
import logging

from core import Database
from windows_design import AddDataWindow


class AddProduct(QDialog):
    def __init__(self):
        super().__init__()

        self._ui = AddDataWindow()
        self._ui.setupUi(self)

        self.connect = Database.get_connection()

        self._ui.category_input.hide()

        self.article = None
        self.name = None
        self.category = None
        self.price = None
        self.description = None
        self.image_path = None

        self.search_timer = QTimer()
        self.search_timer.setInterval(500)
        self.search_timer.setSingleShot(True)

        self.setup_actions()
        self.fill_preset_field()

    def setup_actions(self):
        self._ui.name_input.textChanged.connect(self.name_changed)


        self._ui.category_combobox.currentTextChanged.connect(self.category_changed)

        self._ui.existsing_category.clicked.connect(self.existing_category)
        self._ui.new_category.clicked.connect(self.new_category)

        self._ui.price_input.valueChanged.connect(self.price_changed)

        self._ui.description_input.textChanged.connect(self.description_changed)

        self._ui.load_img.clicked.connect(self.load_img)

        self._ui.save.clicked.connect(self.accept)
        self._ui.cancel.clicked.connect(self.reject)

        self.search_timer.timeout.connect(self.new_category_input)
        self._ui.category_input.textChanged.connect(self.search_timer.start)

    def fill_preset_field(self):
        self.set_article()
        self.set_categories()

    def set_article(self):
        self.article = self.get_article()
        self._ui.article_input.setText(str(self.article))

    def get_article(self) -> int:
        try:
            with self.connect.cursor() as cur:
                query = sql.SQL("SELECT product_article FROM product;")
                articles = cur.execute(query).fetchall()
                ic(articles)
            articles = [item[0] for item in articles]
            article: int = random.randint(0, 99999999)
            while article in articles:
                article = random.randint(0, 99999999)
            return article
        except ps.Error as p:
            logging.exception(f"При выполнении запроса произошла ошибка\n"
                              f"Класс ошибки: {type(p).__name__}\n"
                              f"SQLSTATE: {p.sqlstate}\n"
                              f"Описание: {p.diag.message_primary}\n"
                              f"Подробности: {p.diag.message_detail}\n"
                              f"Полный текст ошибки: {str(p)}\n"
                              f"---------------------------------------")

    def set_categories(self):
        categories = self.get_categories()
        for category in categories:
            self._ui.category_combobox.addItem(category)

    def get_categories(self):
        try:
            with self.connect.cursor() as cur:
                query = sql.SQL("SELECT DISTINCT product_category FROM product;")
                categories = cur.execute(query).fetchall()
            return [item[0] for item in categories]
        except ps.Error as p:
            logging.exception(f"При выполнении запроса произошла ошибка\n"
                              f"Класс ошибки: {type(p).__name__}\n"
                              f"SQLSTATE: {p.sqlstate}\n"
                              f"Описание: {p.diag.message_primary}\n"
                              f"Подробности: {p.diag.message_detail}\n"
                              f"Полный текст ошибки: {str(p)}\n"
                              f"---------------------------------------")

    def name_changed(self):
        pass

    def category_changed(self):
        self.category = self._ui.category_combobox.currentText()

    def new_category_input(self):
        self.category = self._ui.category_input.text()

    def price_changed(self):
        pass

    def description_changed(self):
        pass

    def load_img(self):
        pass

    def existing_category(self):
        self._ui.category_combobox.show()
        self._ui.category_input.hide()
        self.category = self._ui.category_combobox.currentText()

    def new_category(self):
        self._ui.category_combobox.hide()
        self._ui.category_input.show()
