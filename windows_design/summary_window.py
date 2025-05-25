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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QTextBrowser, QWidget)

class Ui_summary(object):
    def setupUi(self, summary):
        if not summary.objectName():
            summary.setObjectName(u"summary")
        summary.resize(800, 600)
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
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(20, 10, 671, 171))
        summary.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(summary)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
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
        self.textBrowser.setHtml(QCoreApplication.translate("summary", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0417\u0430\u043f\u0438\u0445\u043d\u0443\u0442\u044c \u0441\u044e\u0434\u0430 \u043a\u0430\u043a\u0443\u044e-\u043d\u0438\u0431\u0443\u0434\u044c \u0441\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0443 \u043f\u043e \u0442\u0438\u043f\u0443 </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u041e\u0431\u0449\u0435"
                        "\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0437\u0430\u043a\u0430\u0437\u043e\u0432, \u043e\u0431\u0449\u0430\u044f \u0441\u0443\u043c\u043c\u0430 \u043a\u0443\u043f\u043b\u0435\u043d\u043d\u044b\u0445 \u0442\u043e\u0432\u0430\u0440\u043e\u0432, \u0441\u0430\u043c\u0430\u044f \u043f\u043e\u043f\u0443\u043b\u044f\u0440\u043d\u0430\u044f \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0437\u0430\u043a\u0430\u0437\u043e\u0432 \u0441 \u043e\u0446\u0435\u043d\u043a\u043e\u0439 5 \u0437\u0432\u0435\u0437\u0434 (+ \u043f\u0440\u043e\u0446\u0435\u043d\u0442\u043d\u043e\u0435 \u0441\u043e\u043e\u0442\u043d\u043e\u0448\u0435\u043d\u0438\u0435)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    4 \u0437\u0432\u0435"
                        "\u0437\u0434\u044b</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    3 \u0437\u0432\u0435\u0437\u0434\u044b \u0438 \u0442\u0434</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u0422\u0440\u0435\u0431\u0443\u044e\u0449\u0438\u0435 \u0432\u043d\u0438\u043c\u0430\u043d\u0438\u044f \u043a\u0443\u0440\u044c\u0435\u0440\u044b (\u0443 \u043a\u043e\u0442\u043e\u0440\u044b\u0445 \u0437\u0430\u0431\u043b\u043e\u043a\u0438\u0440\u043e\u0432\u0430\u043d\u0430 \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u044c \u043f\u0440\u0438\u043d\u0438\u043c\u0430\u0442\u044c \u0437\u0430\u043a\u0430\u0437\u044b)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0418\u043d\u0444\u0430 \u043e\u0431\u043d\u043e\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u0434\u0438\u043d\u0430"
                        "\u043c\u0438\u0447\u0435\u0441\u043a\u0438 \u043f\u043e\u0441\u0440\u0435\u0434\u0441\u0442\u0432\u043e\u043c \u0443\u0432\u0435\u0434\u043e\u043c\u043b\u0435\u043d\u0438\u0439 \u043e\u0442 \u0431\u0430\u0437\u044b, \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e \u0447\u0430\u0441\u0442\u0438\u0447\u043d\u043e\u0435 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u0435 \u0442\u043e\u043b\u044c\u043a\u043e \u0438\u0437\u043c\u0435\u043d\u0438\u0432\u0448\u0435\u0439\u0441\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438 (\u043d\u0430\u043f\u0440\u0438\u043c\u0435\u0440 \u043d\u0435\u0442 \u043d\u0443\u0436\u0434\u044b \u0438\u0441\u043a\u0430\u0442\u044c \u0437\u0430\u043d\u043e\u0432\u043e \u043f\u0440\u043e\u0431\u043b\u0435\u043c\u043d\u044b\u0445 \u043a\u0443\u0440\u044c\u0435\u0440\u043e\u0432 \u0435\u0441\u043b\u0438 \u0441\u0438\u0433\u043d\u0430\u043b \u043e\u0442 \u0431\u0430\u0437\u044b \u043d\u0435 \u043f\u043e\u0441\u0442\u0443\u043f\u0438\u043b)</p></body></html>", None))
        self.menu.setTitle(QCoreApplication.translate("summary", u"\u041c\u0435\u043d\u044e", None))
        self.menu_2.setTitle(QCoreApplication.translate("summary", u"\u041f\u043e\u043c\u043e\u0449\u044c", None))
    # retranslateUi

