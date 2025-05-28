import logging

import psycopg as ps
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from icecream import ic
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle

from core import Database
from windows_design import ReportsWindow

reports_col = ['Курьер', 'Номер заказа', 'Получатель', 'Адрес доставки', 'Оценка доставки', 'Отзыв']

reports_problematic_couriers_col = ['Курьер', 'ID курьера', 'Рейтинг', 'Номер заказа', 'Оценка доставки', 'Комментарий']


def get_key_by_index(data: dict, index: int):
    for i, key in enumerate(data.keys()):
        if i == index:
            return key


def generate_empty_template():
    report = SimpleDocTemplate("report.pdf", pagesize=landscape(letter))
    pdfmetrics.registerFont(TTFont('Arial', 'C:/Windows/Fonts/arial.ttf'))
    style = ParagraphStyle(name='RussianStyle', fontName='Arial', fontSize=12)
    return report, style


class Reports(QMainWindow):
    def __init__(self, manager):
        super().__init__()
        self.manager = manager
        self._ui = ReportsWindow()
        self._ui.setupUi(self)
        self.couriers = dict()
        self.connect: ps.connect = Database.get_connection()

        self.current_courier_id = 0
        self.data = None
        self.is_problematic_courier_report = False
        self.setup_actions()
        self._ui.groupBox_2.setVisible(False)
        self.show_full_report()

    def setup_actions(self):
        self._ui.summary.triggered.connect(self.manager.show_summary)
        self._ui.full_analytical_report.triggered.connect(self.show_full_report)
        self._ui.report_by_courier.triggered.connect(self.show_report_by_courier)
        self._ui.courier_listbox.currentIndexChanged.connect(self.change_cur_courier)
        self._ui.generate_report.clicked.connect(self.generate_report_by_courier)
        self._ui.save_as_PDF.clicked.connect(self.generate_pdf_report)
        self._ui.problematic_couriers.triggered.connect(self.show_problematic_courier_report)

    def change_cur_courier(self):
        self.current_courier_id = get_key_by_index(self.couriers, self._ui.courier_listbox.currentIndex())

    def show_full_report(self):
        self._ui.groupBox_2.setVisible(False)
        try:
            with self.connect.cursor() as cur:
                self.data = cur.execute("SELECT * FROM full_analytical_report;").fetchall()
            self.data = [[item for item in data] for data in self.data]
            self._ui.reports_fields.setRowCount(len(self.data))
            self._ui.reports_fields.setColumnCount(len(self.data[0]))

            for r_idx, row in enumerate(self.data):
                for c_idx, item in enumerate(row):
                    self._ui.reports_fields.setHorizontalHeaderItem(c_idx,
                                                                    QTableWidgetItem(str(reports_col[c_idx])))
                    self._ui.reports_fields.setItem(r_idx, c_idx, QTableWidgetItem(str(item)))
            self._ui.reports_fields.resizeColumnsToContents()
            self.is_problematic_courier_report = False
        except ps.Error as p:
            logging.exception(f"Произошла ошибка при выполнении запроса: {p}")

    def get_couriers(self):
        try:
            with self.connect.cursor() as cur:
                self.data = cur.execute("""SELECT c.courier_id, 
                u.user_surname || ' ' || u.user_name || ' ' || u.user_patronymic AS "Курьер" 
                FROM courier c 
                JOIN users u ON c.user_id = u.user_id;""").fetchall()
        except ps.Error as p:
            logging.exception(f"Произошла ошибка при выполнении запроса: {p}")

        self._ui.courier_listbox.clear()
        for item in self.data:
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
                self.data = cur.execute("SELECT full_analytical_report_by_courier(%s);",
                                        (self.current_courier_id,)).fetchall()
                self.data = [[item for item in row[0]] for row in self.data]
        except ps.Error as p:
            logging.exception(f"Произошла ошибка при выполнении запроса: {p}")
        self._ui.reports_fields.setRowCount(len(self.data))
        self._ui.reports_fields.setColumnCount(len(self.data[0]))

        for r_idx, row in enumerate(self.data):
            for c_idx, item in enumerate(row):
                self._ui.reports_fields.setHorizontalHeaderItem(c_idx,
                                                                QTableWidgetItem(str(reports_col[c_idx])))
                self._ui.reports_fields.setItem(r_idx, c_idx, QTableWidgetItem(str(item)))
        self._ui.reports_fields.resizeColumnsToContents()
        self.is_problematic_courier_report = False

    def show_problematic_courier_report(self):
        self._ui.groupBox_2.setVisible(False)
        self._ui.reports_fields.clear()
        self._ui.reports_fields.setColumnCount(0)
        self._ui.reports_fields.setRowCount(0)
        try:
            with self.connect.cursor() as cur:
                self.data = cur.execute("SELECT * FROM identifying_problematic_couriers;").fetchall()
            self.data = [[item for item in data] for data in self.data]
            ic(self.data)
        except ps.Error as p:
            logging.exception(f"Произошла ошибка при выполнении запроса: {p}")

        if not self.data:
            return

        self._ui.reports_fields.setRowCount(len(self.data))
        self._ui.reports_fields.setColumnCount(len(self.data[0]))

        for r_idx, row in enumerate(self.data):
            for c_idx, item in enumerate(row):
                self._ui.reports_fields.setHorizontalHeaderItem(c_idx,
                                                                QTableWidgetItem(
                                                                    str(reports_problematic_couriers_col[c_idx])))
                self._ui.reports_fields.setItem(r_idx, c_idx, QTableWidgetItem(str(item)))
        self._ui.reports_fields.resizeColumnsToContents()
        self.is_problematic_courier_report = True

    def generate_pdf_report(self):
        if not self.data:
            QMessageBox.warning(self, "Предупреждение", "Нет данных для сохранения",
                                buttons=QMessageBox.StandardButton.Ok)
            return

        report, style = generate_empty_template()

        self.data = [[Paragraph(str(item), style) for item in row] for row in self.data]

        if self.is_problematic_courier_report:
            self.data.insert(0, reports_problematic_couriers_col)
        else:
            self.data.insert(0, reports_col)

        table_style = TableStyle([
            ('FONTNAME', (0, 0), (-1, -1), 'Arial'),
            ('FONTSIZE', (0, 0), (-1, -1), 12),
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ])

        report_table = Table(data=self.data, style=table_style, hAlign="LEFT")

        report.build([report_table])
        QMessageBox.information(self, "Успех", "Данные сохранены в файл report.pdf",
                                buttons=QMessageBox.StandardButton.Ok)


