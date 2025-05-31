import logging
from random import randint
from threading import Timer

import asyncio
import psycopg as ps
import pyperclip
from PySide6.QtCore import Qt, QTimer, QDate
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QCheckBox, QMessageBox, QVBoxLayout, QWidget, QGridLayout, \
    QAbstractItemView, QComboBox, QDateEdit, QLabel, QHBoxLayout, QDialog, QPushButton, QSpacerItem, QGroupBox, \
    QSizePolicy
from icecream import ic
from psycopg import sql

from core import Database
from core import LOCALIZED_TABLES_NAMES, LOCALIZED_COLUMNS_NAME, IDENTIFIERS, FOREIGN_KEYS, NON_EDITABLE_COLUMNS, \
    REDACT_IN_MODAL_WINDOW_MODE
from windows.addProduct import AddProduct
from windows_design import DataWindow


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


def get_chats_id() -> list[str] | ps.Error:
    connect: ps.connect = Database.get_connection()
    try:
        with connect.cursor() as cur:
            data = cur.execute("SELECT user_tgchat_id FROM users").fetchall()
            data = [item[0] for item in data]
        return data
    except ps.Error as p:
        logging.exception(f"При выполнении запроса произошла ошибка\n"
                          f"Класс ошибки: {type(p).__name__}\n"
                          f"SQLSTATE: {p.sqlstate}\n"
                          f"Описание: {p.diag.message_primary}\n"
                          f"Подробности: {p.diag.message_detail}\n"
                          f"Полный текст ошибки: {str(p)}\n"
                          f"---------------------------------------")
        return p


class Data(QMainWindow):
    def __init__(self, manager):
        super().__init__()
        self.registration_link = None
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

        self.timer = None

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

        self._ui.add_courier.clicked.connect(self.add_courier)
        self._ui.add_product.clicked.connect(self.add_product)

    def current_table_changed(self):
        self.current_table = get_key_by_value(LOCALIZED_TABLES_NAMES, self._ui.tables.currentText())
        self._ui.data_table.cellChanged.disconnect(self.cell_value_changed)
        self.fill_search_field()
        self.fill_display_columns()
        self.show_all_column()

        if self.current_table == 'courier':
            self._ui.add_courier.show()
            self._ui.add_product.hide()
        elif self.current_table == 'product':
            self._ui.add_courier.hide()
            self._ui.add_product.show()
        else:
            self._ui.add_courier.hide()
            self._ui.add_product.hide()

        query = construct_query_by_table(self.current_table)

        try:
            with self.connect.cursor() as cur:
                data = cur.execute(query).fetchall()
            self.data = [[item if isinstance(item, bool) or item is not None else 'Не установлено' for item in row] for
                         row in data]

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
                        checkbox.stateChanged.connect(
                            lambda state, row=r_idx, column=c_idx: self.checkbox_value_changed(state, row, column))
                        self._ui.data_table.setCellWidget(r_idx, c_idx, checkbox)
                        continue

                    self._ui.data_table.setItem(r_idx, c_idx, _item)

            self._ui.data_table.resizeColumnsToContents()
            self._ui.data_table.cellChanged.connect(self.cell_value_changed)

        except ps.Error as p:
            logging.exception(f"При выполнении запроса произошла ошибка\n"
                              f"Класс ошибки: {type(p).__name__}\n"
                              f"SQLSTATE: {p.sqlstate}\n"
                              f"Описание: {p.diag.message_primary}\n"
                              f"Подробности: {p.diag.message_detail}\n"
                              f"Полный текст ошибки: {str(p)}\n"
                              f"---------------------------------------")
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
            logging.exception(f"При выполнении запроса произошла ошибка\n"
                              f"Класс ошибки: {type(p).__name__}\n"
                              f"SQLSTATE: {p.sqlstate}\n"
                              f"Описание: {p.diag.message_primary}\n"
                              f"Подробности: {p.diag.message_detail}\n"
                              f"Полный текст ошибки: {str(p)}\n"
                              f"---------------------------------------")
            self.connect.rollback()

            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Ошибка")
            msg.setText("Произошла ошибка при попытке удаления записи")
            msg.setStandardButtons(QMessageBox.Ok)

            msg.setDetailedText("Дополнительную информацию об ошибке смотрите в логах")
            msg.exec()

    def cell_value_changed(self, row, column):
        table = self._ui.data_table
        new_value = table.item(row, column).text() if table.item(row, column).text() else None

        header_data = table.horizontalHeader().model().headerData(column, Qt.Horizontal)
        header_data = get_key_by_value(LOCALIZED_COLUMNS_NAME.get(self.current_table), header_data)

        try:
            if header_data == 'user_phonenumber':
                if not new_value.isdigit() or len(new_value) != 11:
                    raise BaseException("Новое значение не соответствует шаблону")
        except BaseException as BE:
            logging.exception(f"Произошла ошибка при обновлении значения: {BE}")
            table.item(row, column).setText(self.old_cell_value)
            return

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

            if not new_value:
                self._ui.data_table.cellChanged.disconnect(self.cell_value_changed)

                table.item(row, column).setText('Не установлено')
                table.resizeColumnsToContents()

                self._ui.data_table.cellChanged.connect(self.cell_value_changed)
            if header_data == 'courier_rating':
                asyncio.create_task(Database.notify_channel("rating_changed", ''))
        except ps.Error as p:
            logging.exception(f"При выполнении запроса произошла ошибка\n"
                              f"Класс ошибки: {type(p).__name__}\n"
                              f"SQLSTATE: {p.sqlstate}\n"
                              f"Описание: {p.diag.message_primary}\n"
                              f"Подробности: {p.diag.message_detail}\n"
                              f"Полный текст ошибки: {str(p)}\n"
                              f"---------------------------------------")
            table.item(row, column).setText(self.old_cell_value)
            self.connect.rollback()

    def cell_double_clicked(self, row, column):
        header_data = self._ui.data_table.horizontalHeader().model().headerData(column, Qt.Horizontal)
        header_data = get_key_by_value(LOCALIZED_COLUMNS_NAME.get(self.current_table), header_data)

        if header_data in REDACT_IN_MODAL_WINDOW_MODE.get(self.current_table):
            self._ui.data_table.cellChanged.disconnect(self.cell_value_changed)

            self.old_cell_value = self._ui.data_table.item(row, column).text()
            self.show_modal_window(header_data, row, column)

            self._ui.data_table.cellChanged.connect(self.cell_value_changed)
        else:
            item = self._ui.data_table.item(row, column)
            if item:
                self.old_cell_value = item.text()
                self._ui.data_table.editItem(item)

    def checkbox_value_changed(self, state, row, column):
        new_value = state == Qt.Checked

        header_data = self._ui.data_table.horizontalHeader().model().headerData(column, Qt.Horizontal)
        header_data = get_key_by_value(LOCALIZED_COLUMNS_NAME.get(self.current_table), header_data)
        identifier = IDENTIFIERS.get(self.current_table)
        identifier_value = self._ui.data_table.item(row, 0).text()

        try:
            with self.connect.cursor() as cur:
                query = sql.SQL(
                    "UPDATE {table} SET {column} = %s WHERE {identifier} = %s"
                ).format(
                    table=sql.Identifier(self.current_table),
                    column=sql.Identifier(header_data),
                    identifier=sql.Identifier(identifier)
                )
                cur.execute(query, (new_value, identifier_value))
                self.connect.commit()
        except ps.Error as p:
            logging.exception(f"Ошибка при обновлении checkbox значения в БД\n"
                              f"Класс ошибки: {type(p).__name__}\n"
                              f"SQLSTATE: {p.sqlstate}\n"
                              f"Описание: {p.diag.message_primary}\n"
                              f"Подробности: {p.diag.message_detail}\n"
                              f"Полный текст ошибки: {str(p)}\n"
                              f"---------------------------------------")
            self.connect.rollback()

    def show_modal_window(self, header_data, row, column):
        window = Dialog()
        if window.exec() == 1:
            status = window.save_status()
            self.update_data(row, column, status)

    def update_data(self, row, column, status):
        try:
            table = self._ui.data_table
            identifier = IDENTIFIERS.get(self.current_table)
            identifier_value = table.item(row, 0).text()

            if status[0] == self.old_cell_value:
                return

            with self.connect.cursor() as cur:
                catch = sql.SQL("SELECT 1 FROM \"order\" WHERE order_id = %s FOR UPDATE NOWAIT;")
                cur.execute(catch, (identifier_value,))
                update = sql.SQL("UPDATE \"order\" SET order_status = %s WHERE order_id = %s;")
                cur.execute(update, (status[1], identifier_value,))
            self.connect.commit()

            table.item(row, column).setText(status[0])
            table.resizeColumnsToContents()

        except ps.Error as p:
            logging.exception(f"При выполнении запроса произошла ошибка\n"
                              f"Класс ошибки: {type(p).__name__}\n"
                              f"SQLSTATE: {p.sqlstate}\n"
                              f"Описание: {p.diag.message_primary}\n"
                              f"Подробности: {p.diag.message_detail}\n"
                              f"Полный текст ошибки: {str(p)}\n"
                              f"---------------------------------------")
            self.connect.rollback()

    def add_courier(self):
        chats_id = get_chats_id()

        if not isinstance(chats_id, list):
            e = chats_id
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Ошибка")
            msg.setText("Произошла ошибка при попытке получения данных")
            msg.setStandardButtons(QMessageBox.Ok)

            msg.setDetailedText("Подробную информацию смотрите в логах")
            msg.exec()

        stub_of_chat_id = randint(-2 ** 63, 2 ** 63 - 1)

        while stub_of_chat_id in chats_id:
            stub_of_chat_id = randint(-2 ** 63, 2 ** 63 - 1)

        self.create_courier(stub_of_chat_id)

        pyperclip.copy(self.registration_link)

        QMessageBox.information(self, "Уведомление", "Ссылка для приглашения курьера скопирована в буфер обмена.\n"
                                                     "Отправьте ее курьеру, он должен пройти регистрацию в течение 15 минут!",
                                buttons=QMessageBox.StandardButton.Ok)

    def create_courier(self, chat_id_stub):
        try:
            with self.connect.cursor() as cur:
                query = (sql.SQL(
                    """INSERT INTO users (user_tgchat_id, user_role, user_name, user_surname, user_phonenumber, user_tg_username) 
                values (%s, 'courier', 'stub', 'stub', 11111111111, 'stub') RETURNING user_id;"""
                ))
                user_id = cur.execute(query, (chat_id_stub,)).fetchone()[0]
                self.connect.commit()
            self.registration_link = f"https://t.me/Courier_CourierExpressBot?start={chat_id_stub}"
            self.timer = Timer(900, self.delete_user, [user_id])
            self.timer.start()

        except ps.Error as p:
            logging.exception(f"При выполнении запроса произошла ошибка\n"
                              f"Класс ошибки: {type(p).__name__}\n"
                              f"SQLSTATE: {p.sqlstate}\n"
                              f"Описание: {p.diag.message_primary}\n"
                              f"Подробности: {p.diag.message_detail}\n"
                              f"Полный текст ошибки: {str(p)}\n"
                              f"---------------------------------------")
            self.connect.rollback()

    def delete_user(self, user_id):
        try:
            with self.connect.cursor() as cur:
                query = (sql.SQL(
                    """DELETE FROM users WHERE user_id = %s """
                ))
                cur.execute(query, (user_id,))
                self.connect.commit()
        except ps.Error as p:
            logging.exception(f"При выполнении запроса произошла ошибка\n"
                              f"Класс ошибки: {type(p).__name__}\n"
                              f"SQLSTATE: {p.sqlstate}\n"
                              f"Описание: {p.diag.message_primary}\n"
                              f"Подробности: {p.diag.message_detail}\n"
                              f"Полный текст ошибки: {str(p)}\n"
                              f"---------------------------------------")
            self.connect.rollback()

    def stop_timer(self, conn, pid, channel, payload):
        self.current_table_changed()
        self.timer.cancel()

    def add_product(self):
        window = AddProduct()
        window.exec()


class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Изменение статуса заказа")

        self.status = None
        self.ok_btn = QPushButton("ОК")
        self.cancel_btn = QPushButton("Отмена")

        self.ok_btn.clicked.connect(self.accept)
        self.cancel_btn.clicked.connect(self.reject)

        self.combo = QComboBox()
        self.combo.currentTextChanged.connect(self.status_changed)

        self.setup_layout()

    def setup_layout(self):
        layout = QVBoxLayout()

        cmb_groupbox = QGroupBox()

        v_layout = QVBoxLayout()
        label = QLabel("Выберите новый статус для заказа")

        self.combo.addItem("Доставлен клиенту", userData=2)
        self.combo.addItem("Принят курьером", userData=1)

        self.combo.currentTextChanged.connect(self.status_changed)

        v_layout.addWidget(label)
        v_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        v_layout.addWidget(self.combo)

        cmb_groupbox.setLayout(v_layout)

        btn_groupbox = QGroupBox()

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.ok_btn)

        # горизонтальный спейсер
        h_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

        h_layout.addWidget(self.cancel_btn)

        btn_groupbox.setLayout(h_layout)

        layout.addWidget(cmb_groupbox)
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        layout.addWidget(btn_groupbox)

        self.setLayout(layout)

    def status_changed(self):
        self.status = (self.combo.currentText(), self.combo.currentData())

    def save_status(self):
        return self.status
