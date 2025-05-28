import logging
import webbrowser
from functools import partial

import psycopg as ps
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QPushButton
from icecream import ic
from psycopg import sql

from core import Database
from windows_design import SummaryWindow


def open_telegram(username):
    webbrowser.open(f"https://t.me/{username}")


class SummaryInfo(QMainWindow):
    def __init__(self, manager):
        super().__init__()

        self.manager = manager
        self.connect: ps.connect = Database.get_connection()
        self.count_of_deliveries = None
        self.count_of_couriers = None

        self._ui = SummaryWindow()
        self._ui.setupUi(self)
        self.setup_actions()
        self.show_info()

    def setup_actions(self):
        self._ui.reports.triggered.connect(self.manager.show_reports)

    def show_info(self):
        self.get_orders_summary_info()
        self.get_deliveries_summary_info()
        self.get_couriers_summary_info()
        self.get_problematic_couriers_summary_info()

    def get_orders_summary_info(self):
        """
        label -> orders_summary
        Количество заказов, общая сумма купленных товаров, самая популярная категория
        :return:
        """
        total_amount_purchased_products = 0
        most_ordered_category = ''

        get_count_of_deliveries = (sql.SQL(
            "SELECT COUNT(*) FROM delivery;"
        ))

        get_total_amount_purchased_products = (sql.SQL(
            """SELECT COALESCE(SUM(p.product_price), 0)
FROM delivery d 
JOIN "order" o ON o.order_id = d.order_id 
JOIN added a ON o.order_id = a.order_id 
JOIN product p ON a.product_article = p.product_article;"""
        ))

        get_most_ordered_category = (sql.SQL(
            """WITH user_category_stats AS (
        SELECT 
            p.product_category,
            COUNT(*) AS total_ordered
        FROM 
            users u
        JOIN 
            client c ON u.user_id = c.user_id
        JOIN 
            "order" o ON c.client_id = o.client_id
        JOIN 
            added a ON o.order_id = a.order_id
        JOIN 
            product p ON a.product_article = p.product_article
        GROUP BY 
            p.product_category
    ),
    max_ordered AS (
        SELECT MAX(total_ordered) AS max_count
        FROM user_category_stats
    )
    SELECT 
        ucs.product_category,
        ucs.total_ordered
    FROM 
        user_category_stats ucs
    CROSS JOIN 
        max_ordered mo
    WHERE 
        ucs.total_ordered = mo.max_count
    ORDER BY 
        ucs.product_category;
            """
        ))

        try:
            with self.connect.cursor() as cur:
                self.count_of_deliveries = cur.execute(get_count_of_deliveries).fetchone()[0]
                total_amount_purchased_products = cur.execute(get_total_amount_purchased_products).fetchone()[0]
                most_ordered_category = cur.execute(get_most_ordered_category).fetchall()
        except ps.Error as p:
            logging.exception(f"Произошла ошибка при выполнении запроса: {p}")

        msg = (f"Общая информация о заказах\n"
               f"Общее количество заказов в системе: {self.count_of_deliveries}\n"
               f"Общая сумма купленных товаров: {round(total_amount_purchased_products, 2)}\n"
               f"Наиболее часто заказываемая категория товаров: {', '.join([category[0] for category in most_ordered_category]) or "еще нет заказов"}\n")

        self._ui.orders_summary.setText(msg)

    def get_deliveries_summary_info(self):
        """
        label -> delivery_summary
        Количество заказов с оценкой 5 звезд (+процентное соотношение)
        и тд
        :return:
        """
        query = (sql.SQL(
            """SELECT r.rating, COUNT(d.delivery_id) AS count
FROM generate_series(1, 5) AS r(rating)
LEFT JOIN delivery d ON d.delivery_rating = r.rating
GROUP BY r.rating
ORDER BY r.rating DESC;
            """
        ))
        try:
            with self.connect.cursor() as cur:
                data = cur.execute(query).fetchall()
                if not self.count_of_deliveries:
                    self.count_of_deliveries = cur.execute("SELECT COUNT(*) FROM delivery").fetchone()[0]
        except ps.Error as p:
            logging.exception(f"Произошла ошибка при выполнении запроса: {p}")

        msg = 'Общая информация о рейтинге доставок\n'
        for item in data:
            ending = ("" if item[1] == 1 else
                      "а" if item[1] in [2, 3, 4] else
                      "ов")
            msg += f'{item[0]} 🌟 - {item[1]} заказ{ending}, {round(item[1] / self.count_of_deliveries * 100, 2)}% от общего числа заказов\n'
        self._ui.delivery_summary.setText(msg)

    def get_couriers_summary_info(self):
        """
        label -> couriers_summary
        Общее количество курьеров, количество свободных курьеров, количество занятых курьеров (процентное соотношение)
        Курьер с наивысшим рейтингом
        Курьер с низшим рейтингом
        :return:
        """
        query = (sql.SQL(
            """SELECT COUNT(*) FROM courier WHERE courier_is_busy_with_order = false AND courier_rating >= 4.10
UNION ALL SELECT COUNT(*) FROM courier WHERE courier_is_busy_with_order = true AND courier_rating >= 4.10
UNION ALL SELECT COUNT(*) FROM courier WHERE courier_rating < 4.10;
            """
        ))
        try:
            with self.connect.cursor() as cur:
                if not self.count_of_couriers:
                    self.count_of_couriers = cur.execute("SELECT COUNT(*) FROM courier").fetchone()[0]
                data = cur.execute(query).fetchall()
        except ps.Error as p:
            logging.exception(f"Произошла ошибка при выполнении запроса: {p}")

        data = [item[0] for item in data]

        msg = (f'Общая информация о курьерах\n'
            f'Свободных курьеров - {data[0]}, {round(data[0] / self.count_of_couriers * 100, 2)}% от общего числа курьеров\n'
            f'Занятых заказом курьеров - {data[1]}, {round(data[1] / self.count_of_couriers * 100, 2)}% от общего числа курьеров\n'
            f'Курьеров без возможности принимать заказы - {data[2]}, {round(data[2] / self.count_of_couriers * 100, 2)}% от общего числа курьеров')

        self._ui.couriers_summary.setText(msg)

    def get_problematic_couriers_summary_info(self):
        """
        label -> problematic_couriers_summary
        Количество "проблемных" курьеров и их оценки + кликабельная ссылка на пользователя в тг для быстрой связи
        :return:
        """
        query = (sql.SQL(
            """SELECT u.user_surname || ' ' || u.user_name || ' ' || u.user_patronymic AS "Курьер", c.courier_rating, u.user_tg_username
FROM courier c 
JOIN users u ON c.user_id = u.user_id 
WHERE c.courier_rating < 4.10;"""
        ))

        try:
            with self.connect.cursor() as cur:
                data = cur.execute(query).fetchall()
        except ps.Error as p:
            logging.exception(f"Произошла ошибка при выполнении запроса: {p}")

        if not data:
            return

        self._ui.problematic_couriers_summary.setRowCount(len(data))
        self._ui.problematic_couriers_summary.setColumnCount(len(data[0]))
        self._ui.problematic_couriers_summary.setHorizontalHeaderLabels(["ФИО", "Рейтинг", "Ссылка"])

        for r_idx, row in enumerate(data):
            for c_idx, col in enumerate(row):
                if c_idx == 2:
                    btn = QPushButton("Связаться с курьером")
                    btn.clicked.connect(partial(open_telegram, str(col)))
                    self._ui.problematic_couriers_summary.setCellWidget(r_idx, c_idx, btn)
                else:
                    item = QTableWidgetItem(str(col))
                    self._ui.problematic_couriers_summary.setItem(r_idx, c_idx, item)

        self._ui.problematic_couriers_summary.resizeColumnsToContents()
