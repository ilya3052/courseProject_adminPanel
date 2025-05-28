# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'summary.ui'
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
from PySide6.QtWidgets import (QApplication, QGraphicsView, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QSpacerItem,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_summary(object):
    def setupUi(self, summary):
        if not summary.objectName():
            summary.setObjectName(u"summary")
        summary.resize(874, 648)
        self.action_1 = QAction(summary)
        self.action_1.setObjectName(u"action_1")
        self.action_2 = QAction(summary)
        self.action_2.setObjectName(u"action_2")
        self.action_3 = QAction(summary)
        self.action_3.setObjectName(u"action_3")
        self.action_3.setAutoRepeat(False)
        self.action_4 = QAction(summary)
        self.action_4.setObjectName(u"action_4")
        self.action_6 = QAction(summary)
        self.action_6.setObjectName(u"action_6")
        self.reports = QAction(summary)
        self.reports.setObjectName(u"reports")
        self.centralwidget = QWidget(summary)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(self.groupBox_3)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"QGroupBox {border: none;}")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.couriers_summary = QLabel(self.groupBox)
        self.couriers_summary.setObjectName(u"couriers_summary")
        font = QFont()
        font.setPointSize(11)
        self.couriers_summary.setFont(font)

        self.gridLayout.addWidget(self.couriers_summary, 2, 0, 1, 1)

        self.delivery_summary = QLabel(self.groupBox)
        self.delivery_summary.setObjectName(u"delivery_summary")
        self.delivery_summary.setFont(font)

        self.gridLayout.addWidget(self.delivery_summary, 1, 0, 1, 1)

        self.orders_summary = QLabel(self.groupBox)
        self.orders_summary.setObjectName(u"orders_summary")
        self.orders_summary.setFont(font)

        self.gridLayout.addWidget(self.orders_summary, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox)


        self.gridLayout_2.addWidget(self.groupBox_3, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setStyleSheet(u"QGroupBox {border: none;}")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox_4 = QGroupBox(self.groupBox_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout = QVBoxLayout(self.groupBox_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.problematic_courier_label = QLabel(self.groupBox_4)
        self.problematic_courier_label.setObjectName(u"problematic_courier_label")

        self.verticalLayout.addWidget(self.problematic_courier_label)

        self.problematic_couriers_summary = QTableWidget(self.groupBox_4)
        self.problematic_couriers_summary.setObjectName(u"problematic_couriers_summary")
        self.problematic_couriers_summary.setFont(font)

        self.verticalLayout.addWidget(self.problematic_couriers_summary)


        self.horizontalLayout_2.addWidget(self.groupBox_4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 1)

        self.gridLayout_2.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.groupBox_5 = QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.categories_diagram = QGraphicsView(self.groupBox_5)
        self.categories_diagram.setObjectName(u"categories_diagram")

        self.verticalLayout_2.addWidget(self.categories_diagram)

        self.orders_rating_diagram = QGraphicsView(self.groupBox_5)
        self.orders_rating_diagram.setObjectName(u"orders_rating_diagram")

        self.verticalLayout_2.addWidget(self.orders_rating_diagram)


        self.gridLayout_2.addWidget(self.groupBox_5, 0, 1, 2, 1)

        summary.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(summary)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 874, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        summary.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(summary)
        self.statusbar.setObjectName(u"statusbar")
        summary.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.reports)
        self.menu.addAction(self.action_3)
        self.menu.addAction(self.action_4)
        self.menu.addSeparator()
        self.menu.addAction(self.action_6)

        self.retranslateUi(summary)

        QMetaObject.connectSlotsByName(summary)
    # setupUi

    def retranslateUi(self, summary):
        summary.setWindowTitle(QCoreApplication.translate("summary", u"\u0421\u0432\u043e\u0434\u043d\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
        self.action_1.setText(QCoreApplication.translate("summary", u"\u042d\u043b\u0435\u043c\u0435\u043d\u0442 1", None))
        self.action_2.setText(QCoreApplication.translate("summary", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.action_3.setText(QCoreApplication.translate("summary", u"\u0414\u0430\u043d\u043d\u044b\u0435", None))
#if QT_CONFIG(shortcut)
        self.action_3.setShortcut(QCoreApplication.translate("summary", u"Ctrl+2", None))
#endif // QT_CONFIG(shortcut)
        self.action_4.setText(QCoreApplication.translate("summary", u"\u0416\u0443\u0440\u043d\u0430\u043b \u0443\u0432\u0435\u0434\u043e\u043c\u043b\u0435\u043d\u0438\u0439", None))
#if QT_CONFIG(shortcut)
        self.action_4.setShortcut(QCoreApplication.translate("summary", u"Ctrl+3", None))
#endif // QT_CONFIG(shortcut)
        self.action_6.setText(QCoreApplication.translate("summary", u"\u0412\u044b\u0445\u043e\u0434", None))
#if QT_CONFIG(shortcut)
        self.action_6.setShortcut(QCoreApplication.translate("summary", u"Ctrl+X", None))
#endif // QT_CONFIG(shortcut)
        self.reports.setText(QCoreApplication.translate("summary", u"\u041e\u0442\u0447\u0435\u0442\u044b", None))
#if QT_CONFIG(shortcut)
        self.reports.setShortcut(QCoreApplication.translate("summary", u"Ctrl+1", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox_3.setTitle("")
        self.groupBox.setTitle("")
        self.couriers_summary.setText("")
        self.delivery_summary.setText("")
        self.orders_summary.setText("")
        self.groupBox_2.setTitle("")
        self.groupBox_4.setTitle("")
        self.problematic_courier_label.setText(QCoreApplication.translate("summary", u"\u041a\u0443\u0440\u044c\u0435\u0440\u044b, \u043d\u0430 \u043a\u043e\u0442\u043e\u0440\u044b\u0445 \u0442\u0440\u0435\u0431\u0443\u0435\u0442\u0441\u044f \u043e\u0431\u0440\u0430\u0442\u0438\u0442\u044c \u0432\u043d\u0438\u043c\u0430\u043d\u0438\u0435", None))
        self.groupBox_5.setTitle("")
        self.menu.setTitle(QCoreApplication.translate("summary", u"\u041c\u0435\u043d\u044e", None))
        self.menu_2.setTitle(QCoreApplication.translate("summary", u"\u041f\u043e\u043c\u043e\u0449\u044c", None))
    # retranslateUi

