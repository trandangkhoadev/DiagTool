# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainUI.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QMainWindow,
    QMenu, QMenuBar, QProgressBar, QPushButton,
    QSizePolicy, QStatusBar, QTabWidget, QTableView,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(809, 729)
        self.actionConfig = QAction(MainWindow)
        self.actionConfig.setObjectName(u"actionConfig")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 801, 671))
        self.tabMain = QTabWidget(self.widget)
        self.tabMain.setObjectName(u"tabMain")
        self.tabMain.setGeometry(QRect(10, 10, 781, 511))
        self.tabFlash = QWidget()
        self.tabFlash.setObjectName(u"tabFlash")
        self.btnRun = QPushButton(self.tabFlash)
        self.btnRun.setObjectName(u"btnRun")
        self.btnRun.setGeometry(QRect(20, 20, 91, 51))
        self.progressBar = QProgressBar(self.tabFlash)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(140, 20, 621, 23))
        self.progressBar.setValue(24)
        self.tableView = QTableView(self.tabFlash)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(20, 100, 361, 371))
        self.tableView_2 = QTableView(self.tabFlash)
        self.tableView_2.setObjectName(u"tableView_2")
        self.tableView_2.setGeometry(QRect(400, 100, 361, 371))
        self.label = QLabel(self.tabFlash)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 80, 111, 16))
        self.label_2 = QLabel(self.tabFlash)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(400, 80, 61, 16))
        self.label_3 = QLabel(self.tabFlash)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(140, 50, 591, 16))
        self.tabMain.addTab(self.tabFlash, "")
        self.tabConfig = QWidget()
        self.tabConfig.setObjectName(u"tabConfig")
        self.tabMain.addTab(self.tabConfig, "")
        self.tabWidget = QTabWidget(self.widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 520, 781, 141))
        self.tabInfo = QWidget()
        self.tabInfo.setObjectName(u"tabInfo")
        self.tabWidget.addTab(self.tabInfo, "")
        self.tabTrace = QWidget()
        self.tabTrace.setObjectName(u"tabTrace")
        self.tabWidget.addTab(self.tabTrace, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 809, 33))
        self.menuSetup = QMenu(self.menubar)
        self.menuSetup.setObjectName(u"menuSetup")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuSetup.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuSetup.addAction(self.actionConfig)

        self.retranslateUi(MainWindow)

        self.tabMain.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DiagTool", None))
        self.actionConfig.setText(QCoreApplication.translate("MainWindow", u"Config", None))
        self.btnRun.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Performance steps:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Segments:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"0.4 seconds remaining - 242 bytes of 1023 bytes", None))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tabFlash), QCoreApplication.translate("MainWindow", u"Flash", None))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tabConfig), QCoreApplication.translate("MainWindow", u"Configure", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabInfo), QCoreApplication.translate("MainWindow", u"Information", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTrace), QCoreApplication.translate("MainWindow", u"Trace", None))
        self.menuSetup.setTitle(QCoreApplication.translate("MainWindow", u"Setup", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

