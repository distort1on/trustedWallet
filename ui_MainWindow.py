# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPlainTextEdit, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.create_transaction_button = QPushButton(self.centralwidget)
        self.create_transaction_button.setObjectName(u"create_transaction_button")
        self.create_transaction_button.setGeometry(QRect(10, 40, 251, 32))
        self.tx_info_edit = QPlainTextEdit(self.centralwidget)
        self.tx_info_edit.setObjectName(u"tx_info_edit")
        self.tx_info_edit.setGeometry(QRect(10, 140, 611, 271))
        self.tx_info_edit.setReadOnly(True)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 61, 21))
        self.label.setStyleSheet(u"border: 1px solid black;")
        self.user_address = QLineEdit(self.centralwidget)
        self.user_address.setObjectName(u"user_address")
        self.user_address.setGeometry(QRect(70, 10, 561, 21))
        self.user_address.setStyleSheet(u"border: 1px solid black;")
        self.user_address.setReadOnly(True)
        self.get_lastBlock_button = QPushButton(self.centralwidget)
        self.get_lastBlock_button.setObjectName(u"get_lastBlock_button")
        self.get_lastBlock_button.setGeometry(QRect(10, 90, 101, 32))
        self.sign_transaction_button = QPushButton(self.centralwidget)
        self.sign_transaction_button.setObjectName(u"sign_transaction_button")
        self.sign_transaction_button.setGeometry(QRect(380, 42, 251, 32))
        self.send_transaction_button = QPushButton(self.centralwidget)
        self.send_transaction_button.setObjectName(u"send_transaction_button")
        self.send_transaction_button.setGeometry(QRect(190, 90, 251, 32))
        self.select_document_button = QPushButton(self.centralwidget)
        self.select_document_button.setObjectName(u"select_document_button")
        self.select_document_button.setGeometry(QRect(510, 90, 121, 32))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Trusted Wallet", None))
        self.create_transaction_button.setText(QCoreApplication.translate("MainWindow", u"Create Transaction", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Address:", None))
        self.get_lastBlock_button.setText(QCoreApplication.translate("MainWindow", u"Get last block", None))
        self.sign_transaction_button.setText(QCoreApplication.translate("MainWindow", u"Sign Transaction", None))
        self.send_transaction_button.setText(QCoreApplication.translate("MainWindow", u"Send Transaction", None))
        self.select_document_button.setText(QCoreApplication.translate("MainWindow", u"Select Document", None))
    # retranslateUi

