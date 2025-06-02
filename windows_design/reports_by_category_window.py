# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'report_by_category.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGraphicsView,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_RepByCat(object):
    def setupUi(self, RepByCat):
        if not RepByCat.objectName():
            RepByCat.setObjectName(u"RepByCat")
        RepByCat.resize(740, 768)
        self.verticalLayout = QVBoxLayout(RepByCat)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(RepByCat)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"QGroupBox {border: none;}")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.report_img = QGraphicsView(self.groupBox)
        self.report_img.setObjectName(u"report_img")

        self.gridLayout.addWidget(self.report_img, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(RepByCat)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setStyleSheet(u"QGroupBox {border: none;}")
        self.horizontalLayout = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_3 = QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.categories = QComboBox(self.groupBox_3)
        self.categories.setObjectName(u"categories")

        self.verticalLayout_2.addWidget(self.categories)

        self.create_report = QPushButton(self.groupBox_3)
        self.create_report.setObjectName(u"create_report")

        self.verticalLayout_2.addWidget(self.create_report)


        self.horizontalLayout.addWidget(self.groupBox_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.groupBox_4 = QGroupBox(self.groupBox_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.save_report = QPushButton(self.groupBox_4)
        self.save_report.setObjectName(u"save_report")

        self.verticalLayout_3.addWidget(self.save_report)

        self.close = QPushButton(self.groupBox_4)
        self.close.setObjectName(u"close")

        self.verticalLayout_3.addWidget(self.close)


        self.horizontalLayout.addWidget(self.groupBox_4)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 4)

        self.verticalLayout.addWidget(self.groupBox_2)

        self.verticalLayout.setStretch(0, 5)
        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(RepByCat)

        QMetaObject.connectSlotsByName(RepByCat)
    # setupUi

    def retranslateUi(self, RepByCat):
        RepByCat.setWindowTitle(QCoreApplication.translate("RepByCat", u"\u041e\u0442\u0447\u0435\u0442 \u043f\u043e \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438", None))
        self.groupBox.setTitle("")
        self.groupBox_2.setTitle("")
        self.groupBox_3.setTitle("")
        self.label.setText(QCoreApplication.translate("RepByCat", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e", None))
        self.create_report.setText(QCoreApplication.translate("RepByCat", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043e\u0442\u0447\u0435\u0442", None))
        self.groupBox_4.setTitle("")
        self.save_report.setText(QCoreApplication.translate("RepByCat", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.close.setText(QCoreApplication.translate("RepByCat", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi

