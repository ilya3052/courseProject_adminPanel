import logging

import psycopg as ps
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QCheckBox, QMessageBox, QVBoxLayout, QWidget, QGridLayout, \
    QAbstractItemView
from icecream import ic
from psycopg import sql

from core import Database
from windows_design import DataWindow

from core import *


def construct_query_by_table(table_name: str) -> sql.SQL:
    query = None
    match table_name:
        case 'users':
            query = sql.SQL("SELECT * FROM users;")
        case 'client':
            query = (sql.SQL(
                """SELECT c.client_id, u.user_surname || ' ' || u.user_name as fullname, c.client_registerdate, c.client_nickname, c.user_id
FROM client c JOIN users u ON u.user_id = c.user_id;"""
            ))
        case 'courier':
            query = (sql.SQL(
                """SELECT c.courier_id, u.user_surname || ' ' || u.user_name as fullname, c.courier_rating, c.courier_is_busy_with_order, c.user_id
FROM courier c JOIN users u ON u.user_id = c.user_id;"""
            ))
        case 'delivery':
            query = (sql.SQL(
                """SELECT d.delivery_id, u.user_surname || ' ' || u.user_name AS courier, d.order_id, d.delivery_rating, d.courier_id
FROM delivery d JOIN courier c ON d.courier_id = c.courier_id JOIN users u ON u.user_id = c.user_id;"""
            ))
        case 'product':
            query = sql.SQL("SELECT * FROM product;")
        case 'order':
            query = (sql.SQL(
                """SELECT o.order_id, u.user_surname || ' ' || u.user_name AS client,
CASE 
	WHEN o.order_status = 0 THEN 'Не принят'
	WHEN o.order_status = 1 THEN 'Принят курьером'
	WHEN o.order_status = 2 THEN 'Доставлен клиенту'
END,
o.order_address, o.order_review, c.client_id
FROM "order" o 
	JOIN client c ON c.client_id = o.client_id
	JOIN users u on c.user_id = u.user_id;"""
            ))
    return query


def get_key_by_value(data: dict, value: str):
    for item in data.items():
        if item[1] == value:
            return item[0]


class Data(QMainWindow):
    def __init__(self, manager):
        super().__init__()
        self.manager = manager
        self._ui = DataWindow()
        self._ui.setupUi(self)

        self.current_table = get_key_by_value(LOCALIZED_TABLES_NAMES, self._ui.tables.currentText())
        self.current_column = ()
        self.connect: ps.connect = Database.get_connection()
        self.data = []
        self.old_cell_value = None

        self.search_timer = QTimer()
        self.search_timer.setInterval(500)
        self.search_timer.setSingleShot(True)

        self.setup_actions()
        self.current_table_changed()

    def setup_actions(self):
        self._ui.summary.triggered.connect(self.manager.show_summary)
        self._ui.reports.triggered.connect(self.manager.show_reports)
        self._ui.tables.currentTextChanged.connect(self.current_table_changed)
        self._ui.search_field.currentTextChanged.connect(self.current_column_changed)

        self.search_timer.timeout.connect(self.search_by_column)
        self._ui.search_input.textChanged.connect(self.search_timer.start)

        self._ui.data_table.cellChanged.connect(self.cell_value_changed)
        self._ui.data_table.cellDoubleClicked.connect(self.cell_double_clicked)

        self._ui.data_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self._ui.data_table.verticalHeader().sectionDoubleClicked.connect(lambda x: self.vertical_header_click(x))

    def current_table_changed(self):
        self.current_table = get_key_by_value(LOCALIZED_TABLES_NAMES, self._ui.tables.currentText())
        self._ui.data_table.cellChanged.disconnect(self.cell_value_changed)
        self.fill_search_field()
        self.fill_display_columns()
        self.show_all_column()

        query = construct_query_by_table(self.current_table)
        try:
            with self.connect.cursor() as cur:
                data = cur.execute(query).fetchall()

            self.data = [[item or 'Не установлено' for item in row] for row in data]

            self.clear_table()
            if not self.data:
                self._ui.data_table.setRowCount(1)
                self._ui.data_table.setColumnCount(len(LOCALIZED_COLUMNS_NAME.get(self.current_table).values()))
                self._ui.data_table.setHorizontalHeaderLabels(LOCALIZED_COLUMNS_NAME.get(self.current_table).values())
                return

            self._ui.data_table.setRowCount(len(self.data))
            self._ui.data_table.setColumnCount(len(self.data[0]))
            self._ui.data_table.setHorizontalHeaderLabels(LOCALIZED_COLUMNS_NAME.get(self.current_table).values())

            for r_idx, row in enumerate(self.data):
                for c_idx, item in enumerate(row):
                    _item = QTableWidgetItem(str(item))

                    header_text = self._ui.data_table.horizontalHeader().model().headerData(c_idx, Qt.Horizontal)
                    original_header_text = get_key_by_value(LOCALIZED_COLUMNS_NAME.get(self.current_table), header_text)

                    if header_text not in LOCALIZED_COLUMNS_NAME.get(self.current_table).values():
                        self._ui.data_table.setColumnHidden(c_idx, True)

                    if original_header_text in NON_EDITABLE_COLUMNS.get(
                            self.current_table) or original_header_text in IDENTIFIERS.values():
                        _item.setFlags(~Qt.ItemIsEnabled)

                    if isinstance(item, bool):
                        checkbox = QCheckBox()
                        checkbox.setChecked(item)
                        self._ui.data_table.setCellWidget(r_idx, c_idx, QCheckBox())
                        continue

                    self._ui.data_table.setItem(r_idx, c_idx, _item)

            self._ui.data_table.resizeColumnsToContents()
            self._ui.data_table.cellChanged.connect(self.cell_value_changed)

        except ps.Error as p:
            logging.exception(f"Произошла ошибка при выполеннии запроса: {p}")
        except IndexError:
            pass

    def fill_search_field(self):
        columns = LOCALIZED_COLUMNS_NAME.get(self.current_table).values()
        self._ui.search_field.clear()
        for column in columns:
            self._ui.search_field.addItem(column)

    def fill_display_columns(self):
        group_box = self._ui.display_columns

        for child in group_box.findChildren(QWidget):
            child.setParent(None)

        old_layout = group_box.layout()
        if old_layout is not None:
            QWidget().setLayout(old_layout)

        layout = QGridLayout()

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setHorizontalSpacing(0)
        layout.setVerticalSpacing(0)

        columns = LOCALIZED_COLUMNS_NAME.get(self.current_table).values()
        ic(columns)
        cols_per_row = 2

        for idx, column in enumerate(columns):
            row = idx // cols_per_row
            col = idx % cols_per_row
            checkbox = QCheckBox(column)
            checkbox.checkStateChanged.connect(lambda state, col=column: self.hide_column(col, state))
            layout.addWidget(checkbox, row, col)

        group_box.setLayout(layout)

    def hide_column(self, col, state):
        table = self._ui.data_table
        for c_idx in range(table.columnCount()):
            header_text = self._ui.data_table.horizontalHeader().model().headerData(c_idx, Qt.Horizontal)
            if header_text != col:
                continue
            if state == Qt.Checked:
                self._ui.data_table.setColumnHidden(c_idx, True)
            else:
                self._ui.data_table.setColumnHidden(c_idx, False)

    def show_all_column(self):
        for c_idx in range(self._ui.data_table.columnCount()):
            self._ui.data_table.setColumnHidden(c_idx, False)

    def search_by_column(self):
        text = self._ui.search_input.text()
        if not text:
            self.show_all_rows()

        table = self._ui.data_table
        c_idx = self.current_column[0]
        for row in range(table.rowCount()):
            if text.lower() not in table.item(row, c_idx).text().lower():
                table.setRowHidden(row, True)

    def show_all_rows(self):
        table = self._ui.data_table
        for row in range(table.rowCount()):
            table.setRowHidden(row, False)

    def current_column_changed(self):
        self._ui.search_input.setText("")
        self.show_all_rows()
        self.current_column = (self._ui.search_field.currentIndex(), self._ui.search_field.currentText())

    def clear_table(self):
        for row in range(self._ui.data_table.rowCount()):
            for col in range(self._ui.data_table.columnCount()):
                widget = self._ui.data_table.cellWidget(row, col)
                if widget:
                    self._ui.data_table.removeCellWidget(row, col)

        self._ui.data_table.clear()
        self._ui.data_table.setRowCount(0)
        self._ui.data_table.setColumnCount(0)

    def vertical_header_click(self, x):
        try:
            table = self._ui.data_table
            header = self._ui.data_table.horizontalHeader().model()
            for c in range(table.columnCount()):
                item = table.item(x, c)
                header_text = header.headerData(c, Qt.Horizontal)
                header_text = get_key_by_value(LOCALIZED_COLUMNS_NAME.get(self.current_table), header_text)
                if header_text in IDENTIFIERS.values():
                    self.delete_record(item.text(), header_text, x)
                    return
        except AttributeError:
            pass

    def delete_record(self, record_id, identifier, row_nmb):
        msg = QMessageBox()
        msg.setWindowTitle("Удаление")
        msg.setIcon(QMessageBox.Warning)
        msg.setText(f"Вы уверены что хотите удалить запись с номером {record_id}")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        msg.button(QMessageBox.Yes).setText("Да")
        msg.button(QMessageBox.No).setText("Нет")

        msg.exec()
        if msg.result() == QMessageBox.No:
            return

        try:
            with self.connect.cursor() as cur:
                query = sql.SQL("DELETE FROM {table} WHERE {id_col} = %s").format(
                    table=sql.Identifier(self.current_table),
                    id_col=sql.Identifier(identifier)
                )
                cur.execute(query, (record_id,))
                self.connect.commit()

            row = self._ui.data_table.rowAt(row_nmb)
            self._ui.data_table.removeRow(row)
        except ps.Error as p:
            logging.exception(f"Произошла ошибка при выполнении запроса: {p}")
            self.connect.rollback()

            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Ошибка")
            msg.setText("Произошла ошибка при попытке удаления записи")
            msg.setStandardButtons(QMessageBox.Ok)

            msg.setDetailedText("Дополнительная информация:\n"
                                f"{str(p).split('DETAIL:')[1].strip()}\n"
                                f"Необходимо удалить связанные записи перед удалением!")
            msg.exec()

    def cell_value_changed(self, row, column):
        table = self._ui.data_table
        new_value = table.item(row, column).text()

        header_data = table.horizontalHeader().model().headerData(column, Qt.Horizontal)
        header_data = get_key_by_value(LOCALIZED_COLUMNS_NAME.get(self.current_table), header_data)
        identifier = IDENTIFIERS.get(self.current_table)

        identifier_value = table.item(row, 0).text()

        try:
            with self.connect.cursor() as cur:
                query = (sql.SQL(
                    "UPDATE {table} SET {column} = %s WHERE {identifier} = %s"
                )).format(
                    table=sql.Identifier(self.current_table),
                    column=sql.Identifier(header_data),
                    identifier=sql.Identifier(identifier)
                )
                cur.execute(query, (new_value, identifier_value,))
                self.connect.commit()
        except ps.Error as p:
            logging.exception(f"Произошла ошибка при выполнении запроса: {p}")
            table.item(row, column).setText(self.old_cell_value)
            self.connect.rollback()
