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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_reports(object):
    def setupUi(self, reports):
        if not reports.objectName():
            reports.setObjectName(u"reports")
        reports.resize(800, 600)
        self.summary = QAction(reports)
        self.summary.setObjectName(u"summary")
        self.action_2 = QAction(reports)
        self.action_2.setObjectName(u"action_2")
        self.action_4 = QAction(reports)
        self.action_4.setObjectName(u"action_4")
        self.action_5 = QAction(reports)
        self.action_5.setObjectName(u"action_5")
        self.centralwidget = QWidget(reports)
        self.centralwidget.setObjectName(u"centralwidget")
        reports.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(reports)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        reports.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(reports)
        self.statusbar.setObjectName(u"statusbar")
        reports.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.summary)
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_5)
        self.menu.addSeparator()
        self.menu.addAction(self.action_4)

        self.retranslateUi(reports)

        QMetaObject.connectSlotsByName(reports)
    # setupUi

    def retranslateUi(self, reports):
        reports.setWindowTitle(QCoreApplication.translate("reports", u"\u041e\u0442\u0447\u0435\u0442\u044b", None))
        self.summary.setText(QCoreApplication.translate("reports", u"\u0421\u0432\u043e\u0434\u043d\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
#if QT_CONFIG(shortcut)
        self.summary.setShortcut(QCoreApplication.translate("reports", u"Ctrl+1", None))
#endif // QT_CONFIG(shortcut)
        self.action_2.setText(QCoreApplication.translate("reports", u"\u0414\u0430\u043d\u043d\u044b\u0435", None))
#if QT_CONFIG(shortcut)
        self.action_2.setShortcut(QCoreApplication.translate("reports", u"Ctrl+2", None))
#endif // QT_CONFIG(shortcut)
        self.action_4.setText(QCoreApplication.translate("reports", u"\u0412\u044b\u0445\u043e\u0434", None))
#if QT_CONFIG(shortcut)
        self.action_4.setShortcut(QCoreApplication.translate("reports", u"Ctrl+X", None))
#endif // QT_CONFIG(shortcut)
        self.action_5.setText(QCoreApplication.translate("reports", u"\u0416\u0443\u0440\u043d\u0430\u043b \u0443\u0432\u0435\u0434\u043e\u043c\u043b\u0435\u043d\u0438\u0439", None))
#if QT_CONFIG(shortcut)
        self.action_5.setShortcut(QCoreApplication.translate("reports", u"Ctrl+3", None))
#endif // QT_CONFIG(shortcut)
        self.menu.setTitle(QCoreApplication.translate("reports", u"\u041c\u0435\u043d\u044e", None))
    # retranslateUi

