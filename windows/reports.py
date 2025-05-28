import logging

import psycopg as ps
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem
from icecream import ic

from core import Database
from windows_design import ReportsWindow

reports_col = ['Курьер', 'Номер заказа', 'Получатель', 'Адрес доставки', 'Оценка доставки', 'Отзыв']

reports_problematic_couriers_col = ['Курьер', 'ID курьера', 'Рейтинг', 'Номер заказа', 'Оценка доставки', 'Комментарий']


def get_key_by_index(data: dict, index: int):
    for i, key in enumerate(data.keys()):
        if i == index:
            return key


class Reports(QMainWindow):
    def __init__(self, manager):
        super().__init__()
        self.manager = manager
        self._ui = ReportsWindow()
        self._ui.setupUi(self)
        self.couriers = dict()
        self.connect: ps.connect = Database.get_connection()

        self.current_courier_id = 0
        self.setup_actions()
        self._ui.groupBox_2.setVisible(False)
        self.show_full_report()

    def setup_actions(self):
        self._ui.summary.triggered.connect(self.manager.show_summary)
        self._ui.full_analytical_report.triggered.connect(self.show_full_report)
        self._ui.report_by_courier.triggered.connect(self.show_report_by_courier)
        self._ui.courier_listbox.currentIndexChanged.connect(self.change_cur_courier)
        self._ui.generate_report.clicked.connect(self.generate_report_by_courier)
        self._ui.problematic_couriers.triggered.connect(self.show_problematic_courier_report)

    def change_cur_courier(self):
        self.current_courier_id = get_key_by_index(self.couriers, self._ui.courier_listbox.currentIndex())

    def show_full_report(self):
        self._ui.groupBox_2.setVisible(False)
        try:
            with self.connect.cursor() as cur:
                data = cur.execute("SELECT * FROM full_analytical_report;").fetchall()

            self._ui.reports_fields.setRowCount(len(data))
            self._ui.reports_fields.setColumnCount(len(data[0]))

            for r_idx, row in enumerate(data):
                for c_idx, item in enumerate(row):
                    self._ui.reports_fields.setHorizontalHeaderItem(c_idx,
                                                                    QTableWidgetItem(str(reports_col[c_idx])))
                    self._ui.reports_fields.setItem(r_idx, c_idx, QTableWidgetItem(str(item)))
            self._ui.reports_fields.resizeColumnsToContents()
        except ps.Error as p:
            logging.exception(f"Произошла ошибка при выполнении запроса: {p}")

    def get_couriers(self):
        try:
            with self.connect.cursor() as cur:
                data = cur.execute("""SELECT c.courier_id, 
                u.user_surname || ' ' || u.user_name || ' ' || u.user_patronymic AS "Курьер" 
                FROM courier c 
                JOIN users u ON c.user_id = u.user_id;""").fetchall()
        except ps.Error as p:
            logging.exception(f"Произошла ошибка при выполнении запроса: {p}")

        self._ui.courier_listbox.clear()
        for item in data:
            self.couriers[item[0]] = item[1]
            self._ui.courier_listbox.addItem(item[1])

    def show_report_by_courier(self):
        self._ui.reports_fields.clear()
        self._ui.reports_fields.setColumnCount(0)
        self._ui.reports_fields.setRowCount(0)
        self._ui.groupBox_2.setVisible(True)
        self.get_couriers()

    def generate_report_by_courier(self):
        try:
            with self.connect.cursor() as cur:
                data = cur.execute("SELECT full_analytical_report_by_courier(%s);",
                                   (self.current_courier_id,)).fetchall()
            ic(data[0][0][0])
        except ps.Error as p:
            logging.exception(f"Произошла ошибка при выполнении запроса: {p}")
        self._ui.reports_fields.setRowCount(len(data))
        self._ui.reports_fields.setColumnCount(len(data[0][0]))

        for r_idx, row in enumerate(data):
            for c_idx, item in enumerate(row[0]):
                self._ui.reports_fields.setHorizontalHeaderItem(c_idx,
                                                                QTableWidgetItem(str(reports_col[c_idx])))
                self._ui.reports_fields.setItem(r_idx, c_idx, QTableWidgetItem(str(item)))
        self._ui.reports_fields.resizeColumnsToContents()

    def show_problematic_courier_report(self):
        self._ui.groupBox_2.setVisible(False)
        self._ui.reports_fields.clear()
        self._ui.reports_fields.setColumnCount(0)
        self._ui.reports_fields.setRowCount(0)
        try:
            with self.connect.cursor() as cur:
                data = cur.execute("SELECT * FROM identifying_problematic_couriers;").fetchall()
        except ps.Error as p:
            logging.exception(f"Произошла ошибка при выполнении запроса: {p}")

        if not data:
            return

        self._ui.reports_fields.setRowCount(len(data))
        self._ui.reports_fields.setColumnCount(len(data[0]))

        for r_idx, row in enumerate(data):
            for c_idx, item in enumerate(row):
                self._ui.reports_fields.setHorizontalHeaderItem(c_idx,
                                                                QTableWidgetItem(
                                                                    str(reports_problematic_couriers_col[c_idx])))
                self._ui.reports_fields.setItem(r_idx, c_idx, QTableWidgetItem(str(item)))
        self._ui.reports_fields.resizeColumnsToContents()
