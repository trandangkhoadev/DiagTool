# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configUI.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Config(object):
    def setupUi(self, Config):
        if not Config.objectName():
            Config.setObjectName(u"Config")
        Config.resize(292, 212)
        self.widget = QWidget(Config)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 10, 261, 181))
        self.comboBox_4 = QComboBox(self.widget)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setGeometry(QRect(70, 30, 121, 24))
        self.comboBox_3 = QComboBox(self.widget)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(70, 0, 121, 24))
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 30, 49, 21))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 49, 21))
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 60, 49, 21))
        self.comboBox_5 = QComboBox(self.widget)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setGeometry(QRect(70, 60, 121, 24))
        self.btnConnect = QPushButton(self.widget)
        self.btnConnect.setObjectName(u"btnConnect")
        self.btnConnect.setGeometry(QRect(170, 150, 75, 24))

        self.retranslateUi(Config)

        QMetaObject.connectSlotsByName(Config)
    # setupUi

    def retranslateUi(self, Config):
        Config.setWindowTitle(QCoreApplication.translate("Config", u"Form", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("Config", u"Vector", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("Config", u"PCAN", None))

        self.comboBox_3.setItemText(0, QCoreApplication.translate("Config", u"CAN", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("Config", u"Ethernet", None))

        self.label_2.setText(QCoreApplication.translate("Config", u"Device:", None))
        self.label.setText(QCoreApplication.translate("Config", u"Mode:", None))
        self.label_3.setText(QCoreApplication.translate("Config", u"Channel:", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("Config", u"Vector", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("Config", u"PCAN", None))

        self.btnConnect.setText(QCoreApplication.translate("Config", u"Connect", None))
    # retranslateUi

