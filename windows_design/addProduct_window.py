# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_product.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDialog,
    QDoubleSpinBox, QGraphicsView, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"RepByCat")
        Dialog.resize(1101, 692)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_3 = QGroupBox(Dialog)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setStyleSheet(u"QGroupBox {border: none;}")
        self.horizontalLayout_8 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.groupBox = QGroupBox(self.groupBox_3)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"QGroupBox {border: 1px solid ;\n"
"border-color: rgb(220, 220, 220);}")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.article = QGroupBox(self.groupBox)
        self.article.setObjectName(u"article")
        self.article.setStyleSheet(u"QGroupBox {border: 1px solid ;\n"
"border-color: rgb(220, 220, 220);}")
        self.horizontalLayout_3 = QHBoxLayout(self.article)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.article)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.article_input = QLineEdit(self.article)
        self.article_input.setObjectName(u"article_input")
        self.article_input.setEnabled(True)
        self.article_input.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.article_input)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)
        self.horizontalLayout_3.setStretch(2, 6)

        self.verticalLayout_6.addWidget(self.article)

        self.name = QGroupBox(self.groupBox)
        self.name.setObjectName(u"name")
        self.name.setStyleSheet(u"QGroupBox {border: 1px solid ;\n"
"border-color: rgb(220, 220, 220);}")
        self.horizontalLayout_4 = QHBoxLayout(self.name)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.name)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.name_input = QLineEdit(self.name)
        self.name_input.setObjectName(u"name_input")

        self.horizontalLayout_4.addWidget(self.name_input)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 2)
        self.horizontalLayout_4.setStretch(2, 6)

        self.verticalLayout_6.addWidget(self.name)

        self.category = QGroupBox(self.groupBox)
        self.category.setObjectName(u"category")
        self.category.setStyleSheet(u"QGroupBox {border: 1px solid ;\n"
"border-color: rgb(220, 220, 220);}")
        self.horizontalLayout = QHBoxLayout(self.category)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.category)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.groupBox_7 = QGroupBox(self.category)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setStyleSheet(u"QGroupBox {border: none;}")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox_9 = QGroupBox(self.groupBox_7)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.category_combobox = QComboBox(self.groupBox_9)
        self.category_combobox.setObjectName(u"category_combobox")

        self.verticalLayout_2.addWidget(self.category_combobox)

        self.category_input = QLineEdit(self.groupBox_9)
        self.category_input.setObjectName(u"category_input")

        self.verticalLayout_2.addWidget(self.category_input)


        self.horizontalLayout_2.addWidget(self.groupBox_9)

        self.groupBox_8 = QGroupBox(self.groupBox_7)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.existsing_category = QRadioButton(self.groupBox_8)
        self.existsing_category.setObjectName(u"existsing_category")
        self.existsing_category.setChecked(True)

        self.verticalLayout_3.addWidget(self.existsing_category)

        self.new_category = QRadioButton(self.groupBox_8)
        self.new_category.setObjectName(u"new_category")

        self.verticalLayout_3.addWidget(self.new_category)


        self.horizontalLayout_2.addWidget(self.groupBox_8)

        self.horizontalLayout_2.setStretch(0, 7)
        self.horizontalLayout_2.setStretch(1, 5)

        self.horizontalLayout.addWidget(self.groupBox_7)

        self.horizontalLayout.setStretch(1, 5)

        self.verticalLayout_6.addWidget(self.category)

        self.price = QGroupBox(self.groupBox)
        self.price.setObjectName(u"price")
        self.price.setStyleSheet(u"QGroupBox {border: 1px solid ;\n"
"border-color: rgb(220, 220, 220);}")
        self.horizontalLayout_5 = QHBoxLayout(self.price)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.price)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.price_input = QDoubleSpinBox(self.price)
        self.price_input.setObjectName(u"price_input")
        self.price_input.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.price_input.setMaximum(50000.000000000000000)
        self.price_input.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.price_input.setValue(1.000000000000000)

        self.horizontalLayout_5.addWidget(self.price_input)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_5.setStretch(0, 2)
        self.horizontalLayout_5.setStretch(1, 4)
        self.horizontalLayout_5.setStretch(2, 6)

        self.verticalLayout_6.addWidget(self.price)

        self.description = QGroupBox(self.groupBox)
        self.description.setObjectName(u"description")
        self.description.setStyleSheet(u"QGroupBox {border: 1px solid ;\n"
"border-color: rgb(220, 220, 220);}")
        self.verticalLayout_4 = QVBoxLayout(self.description)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.description)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_5)

        self.description_input = QTextEdit(self.description)
        self.description_input.setObjectName(u"description_input")

        self.verticalLayout_4.addWidget(self.description_input)


        self.verticalLayout_6.addWidget(self.description)


        self.horizontalLayout_8.addWidget(self.groupBox)

        self.image = QGroupBox(self.groupBox_3)
        self.image.setObjectName(u"image")
        self.image.setStyleSheet(u"QGroupBox {border: 1px solid ;\n"
"border-color: rgb(220, 220, 220);}")
        self.verticalLayout_5 = QVBoxLayout(self.image)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_6 = QLabel(self.image)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_6)

        self.product_img = QGraphicsView(self.image)
        self.product_img.setObjectName(u"product_img")

        self.verticalLayout_5.addWidget(self.product_img)

        self.groupBox_2 = QGroupBox(self.image)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setStyleSheet(u"QGroupBox {border: none;}")
        self.horizontalLayout_7 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)

        self.load_img = QPushButton(self.groupBox_2)
        self.load_img.setObjectName(u"load_img")

        self.horizontalLayout_7.addWidget(self.load_img)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)


        self.verticalLayout_5.addWidget(self.groupBox_2)


        self.horizontalLayout_8.addWidget(self.image)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(Dialog)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setStyleSheet(u"QGroupBox {border: none;}")
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)

        self.groupBox_5 = QGroupBox(self.groupBox_4)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.horizontalLayout_9 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.save = QPushButton(self.groupBox_5)
        self.save.setObjectName(u"save")

        self.horizontalLayout_9.addWidget(self.save)

        self.cancel = QPushButton(self.groupBox_5)
        self.cancel.setObjectName(u"cancel")

        self.horizontalLayout_9.addWidget(self.cancel)


        self.horizontalLayout_6.addWidget(self.groupBox_5)


        self.verticalLayout.addWidget(self.groupBox_4)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("RepByCat", u"RepByCat", None))
        self.groupBox_3.setTitle("")
        self.groupBox.setTitle("")
        self.article.setTitle("")
        self.label.setText(QCoreApplication.translate("RepByCat", u"\u0410\u0440\u0442\u0438\u043a\u0443\u043b", None))
        self.name.setTitle("")
        self.label_2.setText(QCoreApplication.translate("RepByCat", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.category.setTitle("")
        self.label_3.setText(QCoreApplication.translate("RepByCat", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e", None))
        self.groupBox_7.setTitle("")
        self.groupBox_9.setTitle("")
        self.groupBox_8.setTitle("")
        self.existsing_category.setText(QCoreApplication.translate("RepByCat", u"\u0421\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u044e\u0449\u0430\u044f", None))
        self.new_category.setText(QCoreApplication.translate("RepByCat", u"\u041d\u043e\u0432\u0430\u044f", None))
        self.price.setTitle("")
        self.label_4.setText(QCoreApplication.translate("RepByCat", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u20bd", None))
        self.price_input.setSpecialValueText("")
        self.description.setTitle("")
        self.label_5.setText(QCoreApplication.translate("RepByCat", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 (\u0434\u043e 512 \u0441\u0438\u043c\u0432\u043e\u043b\u043e\u0432)", None))
        self.image.setTitle("")
        self.label_6.setText(QCoreApplication.translate("RepByCat", u"\u0412\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0435 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.groupBox_2.setTitle("")
        self.load_img.setText(QCoreApplication.translate("RepByCat", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
        self.groupBox_4.setTitle("")
        self.groupBox_5.setTitle("")
        self.save.setText(QCoreApplication.translate("RepByCat", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.cancel.setText(QCoreApplication.translate("RepByCat", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
    # retranslateUi

