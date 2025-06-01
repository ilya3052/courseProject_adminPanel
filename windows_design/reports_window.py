# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reports.ui'
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
    QHeaderView, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)

class Ui_reports(object):
    def setupUi(self, reports):
        if not reports.objectName():
            reports.setObjectName(u"reports")
        reports.resize(800, 600)
        self.summary = QAction(reports)
        self.summary.setObjectName(u"summary")
        self.data = QAction(reports)
        self.data.setObjectName(u"data")
        self.action_4 = QAction(reports)
        self.action_4.setObjectName(u"action_4")
        self.action_5 = QAction(reports)
        self.action_5.setObjectName(u"action_5")
        self.problematic_couriers = QAction(reports)
        self.problematic_couriers.setObjectName(u"problematic_couriers")
        self.report_by_courier = QAction(reports)
        self.report_by_courier.setObjectName(u"report_by_courier")
        self.full_analytical_report = QAction(reports)
        self.full_analytical_report.setObjectName(u"full_analytical_report")
        self.report_by_category = QAction(reports)
        self.report_by_category.setObjectName(u"report_by_category")
        self.average_cost_report = QAction(reports)
        self.average_cost_report.setObjectName(u"average_cost_report")
        self.centralwidget = QWidget(reports)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setStyleSheet(u"QGroupBox {border: none;}")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.generate_report = QPushButton(self.groupBox_2)
        self.generate_report.setObjectName(u"generate_report")
        self.generate_report.setEnabled(True)

        self.gridLayout_2.addWidget(self.generate_report, 2, 0, 1, 1)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.courier_listbox = QComboBox(self.groupBox_2)
        self.courier_listbox.setObjectName(u"courier_listbox")

        self.gridLayout_2.addWidget(self.courier_listbox, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.reports_fields = QTableWidget(self.centralwidget)
        self.reports_fields.setObjectName(u"reports_fields")

        self.gridLayout.addWidget(self.reports_fields, 0, 0, 1, 3)

        self.save_as_PDF = QPushButton(self.centralwidget)
        self.save_as_PDF.setObjectName(u"save_as_PDF")

        self.gridLayout.addWidget(self.save_as_PDF, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 1, 1, 1)

        reports.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(reports)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        reports.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(reports)
        self.statusbar.setObjectName(u"statusbar")
        reports.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.summary)
        self.menu.addAction(self.data)
        self.menu.addAction(self.action_5)
        self.menu.addSeparator()
        self.menu.addAction(self.action_4)
        self.menu_2.addAction(self.problematic_couriers)
        self.menu_2.addAction(self.report_by_courier)
        self.menu_2.addAction(self.full_analytical_report)
        self.menu_2.addAction(self.report_by_category)

        self.retranslateUi(reports)

        QMetaObject.connectSlotsByName(reports)
    # setupUi

    def retranslateUi(self, reports):
        reports.setWindowTitle(QCoreApplication.translate("reports", u"\u041e\u0442\u0447\u0435\u0442\u044b", None))
        self.summary.setText(QCoreApplication.translate("reports", u"\u0421\u0432\u043e\u0434\u043d\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
#if QT_CONFIG(shortcut)
        self.summary.setShortcut(QCoreApplication.translate("reports", u"Ctrl+1", None))
#endif // QT_CONFIG(shortcut)
        self.data.setText(QCoreApplication.translate("reports", u"\u0414\u0430\u043d\u043d\u044b\u0435", None))
#if QT_CONFIG(shortcut)
        self.data.setShortcut(QCoreApplication.translate("reports", u"Ctrl+2", None))
#endif // QT_CONFIG(shortcut)
        self.action_4.setText(QCoreApplication.translate("reports", u"\u0412\u044b\u0445\u043e\u0434", None))
#if QT_CONFIG(shortcut)
        self.action_4.setShortcut(QCoreApplication.translate("reports", u"Ctrl+X", None))
#endif // QT_CONFIG(shortcut)
        self.action_5.setText(QCoreApplication.translate("reports", u"\u0416\u0443\u0440\u043d\u0430\u043b \u0443\u0432\u0435\u0434\u043e\u043c\u043b\u0435\u043d\u0438\u0439", None))
#if QT_CONFIG(shortcut)
        self.action_5.setShortcut(QCoreApplication.translate("reports", u"Ctrl+3", None))
#endif // QT_CONFIG(shortcut)
        self.problematic_couriers.setText(QCoreApplication.translate("reports", u"\u041f\u0440\u043e\u0431\u043b\u0435\u043c\u043d\u044b\u0435 \u043a\u0443\u0440\u044c\u0435\u0440\u044b", None))
#if QT_CONFIG(shortcut)
        self.problematic_couriers.setShortcut(QCoreApplication.translate("reports", u"Alt+1", None))
#endif // QT_CONFIG(shortcut)
        self.report_by_courier.setText(QCoreApplication.translate("reports", u"\u041e\u0442\u0447\u0435\u0442 \u043f\u043e \u043a\u0443\u0440\u044c\u0435\u0440\u0443", None))
#if QT_CONFIG(shortcut)
        self.report_by_courier.setShortcut(QCoreApplication.translate("reports", u"Alt+2", None))
#endif // QT_CONFIG(shortcut)
        self.full_analytical_report.setText(QCoreApplication.translate("reports", u"\u041e\u0442\u0447\u0435\u0442 \u043f\u043e \u0432\u0441\u0435\u043c \u043a\u0443\u0440\u044c\u0435\u0440\u0430\u043c", None))
#if QT_CONFIG(shortcut)
        self.full_analytical_report.setShortcut(QCoreApplication.translate("reports", u"Alt+3", None))
#endif // QT_CONFIG(shortcut)
        self.report_by_category.setText(QCoreApplication.translate("reports", u"\u041e\u0442\u0447\u0435\u0442 \u043f\u043e \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438", None))
#if QT_CONFIG(shortcut)
        self.report_by_category.setShortcut(QCoreApplication.translate("reports", u"Alt+4", None))
#endif // QT_CONFIG(shortcut)
        self.average_cost_report.setText(QCoreApplication.translate("reports", u"\u041e\u0442\u0447\u0435\u0442 \u043f\u043e \u0441\u0440\u0435\u0434\u043d\u0435\u0439 \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u0438 \u0437\u0430\u043a\u0430\u0437\u0430", None))
#if QT_CONFIG(shortcut)
        self.average_cost_report.setShortcut(QCoreApplication.translate("reports", u"Alt+5", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox_2.setTitle("")
        self.generate_report.setText(QCoreApplication.translate("reports", u"\u0421\u0433\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043e\u0442\u0447\u0435\u0442", None))
        self.label.setText(QCoreApplication.translate("reports", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043a\u0443\u0440\u044c\u0435\u0440\u0430 \u0434\u043b\u044f \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f \u043e\u0442\u0447\u0435\u0442\u0430", None))
        self.save_as_PDF.setText(QCoreApplication.translate("reports", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0432 PDF", None))
        self.menu.setTitle(QCoreApplication.translate("reports", u"\u041c\u0435\u043d\u044e", None))
        self.menu_2.setTitle(QCoreApplication.translate("reports", u"\u041e\u0442\u0447\u0435\u0442\u044b", None))
    # retranslateUi

