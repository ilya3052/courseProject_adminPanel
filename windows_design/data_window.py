# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'data.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QSizePolicy,
    QSpacerItem, QStatusBar, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_data(object):
    def setupUi(self, data):
        if not data.objectName():
            data.setObjectName(u"data")
        data.resize(800, 600)
        self.summary = QAction(data)
        self.summary.setObjectName(u"summary")
        self.reports = QAction(data)
        self.reports.setObjectName(u"reports")
        self.action_3 = QAction(data)
        self.action_3.setObjectName(u"action_3")
        self.action_5 = QAction(data)
        self.action_5.setObjectName(u"action_5")
        self.centralwidget = QWidget(data)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setStyleSheet(u"QGroupBox {border: none;}")
        self.gridLayout = QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.tables = QComboBox(self.groupBox_3)
        self.tables.addItem("")
        self.tables.addItem("")
        self.tables.addItem("")
        self.tables.addItem("")
        self.tables.addItem("")
        self.tables.addItem("")
        self.tables.setObjectName(u"tables")
        self.tables.setMaximumSize(QSize(171, 22))

        self.gridLayout.addWidget(self.tables, 2, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 0, 0, 1, 1)

        self.gridLayout.setColumnStretch(0, 2)

        self.horizontalLayout.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setStyleSheet(u"QGroupBox {border: none;}")
        self.groupBox_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox_7 = QGroupBox(self.groupBox_4)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.groupBox_7)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_4.addWidget(self.label_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.display_columns = QGroupBox(self.groupBox_7)
        self.display_columns.setObjectName(u"display_columns")

        self.verticalLayout_4.addWidget(self.display_columns)


        self.horizontalLayout_2.addWidget(self.groupBox_7)

        self.groupBox_6 = QGroupBox(self.groupBox_4)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.search_input = QLineEdit(self.groupBox_6)
        self.search_input.setObjectName(u"search_input")

        self.verticalLayout_2.addWidget(self.search_input)


        self.horizontalLayout_2.addWidget(self.groupBox_6)

        self.groupBox_5 = QGroupBox(self.groupBox_4)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_5)

        self.label = QLabel(self.groupBox_5)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.search_field = QComboBox(self.groupBox_5)
        self.search_field.setObjectName(u"search_field")

        self.verticalLayout_3.addWidget(self.search_field)


        self.horizontalLayout_2.addWidget(self.groupBox_5)

        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(2, 2)

        self.horizontalLayout.addWidget(self.groupBox_4)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 6)

        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.data_table = QTableWidget(self.groupBox_2)
        self.data_table.setObjectName(u"data_table")

        self.gridLayout_2.addWidget(self.data_table, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 8)
        data.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(data)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        data.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(data)
        self.statusbar.setObjectName(u"statusbar")
        data.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.summary)
        self.menu.addAction(self.reports)
        self.menu.addAction(self.action_3)
        self.menu.addSeparator()
        self.menu.addAction(self.action_5)

        self.retranslateUi(data)

        QMetaObject.connectSlotsByName(data)
    # setupUi

    def retranslateUi(self, data):
        data.setWindowTitle(QCoreApplication.translate("data", u"\u0414\u0430\u043d\u043d\u044b\u0435", None))
        self.summary.setText(QCoreApplication.translate("data", u"\u0421\u0432\u043e\u0434\u043d\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
#if QT_CONFIG(shortcut)
        self.summary.setShortcut(QCoreApplication.translate("data", u"Ctrl+1", None))
#endif // QT_CONFIG(shortcut)
        self.reports.setText(QCoreApplication.translate("data", u"\u041e\u0442\u0447\u0435\u0442\u044b", None))
#if QT_CONFIG(shortcut)
        self.reports.setShortcut(QCoreApplication.translate("data", u"Ctrl+2", None))
#endif // QT_CONFIG(shortcut)
        self.action_3.setText(QCoreApplication.translate("data", u"\u0416\u0443\u0440\u043d\u0430\u043b \u0443\u0432\u0435\u0434\u043e\u043c\u043b\u0435\u043d\u0438\u0439", None))
#if QT_CONFIG(shortcut)
        self.action_3.setShortcut(QCoreApplication.translate("data", u"Ctrl+3", None))
#endif // QT_CONFIG(shortcut)
        self.action_5.setText(QCoreApplication.translate("data", u"\u0412\u044b\u0445\u043e\u0434", None))
#if QT_CONFIG(shortcut)
        self.action_5.setShortcut(QCoreApplication.translate("data", u"Ctrl+X", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox.setTitle("")
        self.groupBox_3.setTitle("")
        self.label_2.setText(QCoreApplication.translate("data", u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430 \u0434\u043b\u044f \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f", None))
        self.tables.setItemText(0, QCoreApplication.translate("data", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438", None))
        self.tables.setItemText(1, QCoreApplication.translate("data", u"\u041a\u043b\u0438\u0435\u043d\u0442\u044b", None))
        self.tables.setItemText(2, QCoreApplication.translate("data", u"\u041a\u0443\u0440\u044c\u0435\u0440\u044b", None))
        self.tables.setItemText(3, QCoreApplication.translate("data", u"\u0414\u043e\u0441\u0442\u0430\u0432\u043a\u0438", None))
        self.tables.setItemText(4, QCoreApplication.translate("data", u"\u0422\u043e\u0432\u0430\u0440\u044b", None))
        self.tables.setItemText(5, QCoreApplication.translate("data", u"\u0417\u0430\u043a\u0430\u0437\u044b", None))

        self.groupBox_4.setTitle("")
        self.groupBox_7.setTitle("")
        self.label_3.setText(QCoreApplication.translate("data", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043a\u043e\u043b\u043e\u043d\u043a\u0438 \u0434\u043b\u044f \u0441\u043e\u043a\u0440\u044b\u0442\u0438\u044f", None))
        self.display_columns.setTitle("")
        self.groupBox_6.setTitle("")
        self.search_input.setPlaceholderText(QCoreApplication.translate("data", u"\u041f\u043e\u0438\u0441\u043a...", None))
        self.groupBox_5.setTitle("")
        self.label.setText(QCoreApplication.translate("data", u"\u041f\u043e\u043b\u0435 \u0434\u043b\u044f \u043f\u043e\u0438\u0441\u043a\u0430", None))
        self.groupBox_2.setTitle("")
        self.menu.setTitle(QCoreApplication.translate("data", u"\u041c\u0435\u043d\u044e", None))
        self.menu_2.setTitle(QCoreApplication.translate("data", u"\u041f\u043e\u043c\u043e\u0449\u044c", None))
    # retranslateUi

