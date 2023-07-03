# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPlainTextEdit,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 480)
        self.actionRequest_blocksHistory = QAction(MainWindow)
        self.actionRequest_blocksHistory.setObjectName(u"actionRequest_blocksHistory")
        self.actionRequest_txHistory = QAction(MainWindow)
        self.actionRequest_txHistory.setObjectName(u"actionRequest_txHistory")
        self.actionAdd_KeyPair = QAction(MainWindow)
        self.actionAdd_KeyPair.setObjectName(u"actionAdd_KeyPair")
        self.actionShow_my_seed_phrase = QAction(MainWindow)
        self.actionShow_my_seed_phrase.setObjectName(u"actionShow_my_seed_phrase")
        self.action_show_Find_tx_by_hash_window = QAction(MainWindow)
        self.action_show_Find_tx_by_hash_window.setObjectName(u"action_show_Find_tx_by_hash_window")
        self.actionFind_document = QAction(MainWindow)
        self.actionFind_document.setObjectName(u"actionFind_document")
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
        self.user_address.setGeometry(QRect(70, 10, 491, 21))
        self.user_address.setStyleSheet(u"border: 1px solid black;")
        self.user_address.setReadOnly(True)
        self.sign_transaction_button = QPushButton(self.centralwidget)
        self.sign_transaction_button.setObjectName(u"sign_transaction_button")
        self.sign_transaction_button.setGeometry(QRect(380, 42, 251, 32))
        self.send_transaction_button = QPushButton(self.centralwidget)
        self.send_transaction_button.setObjectName(u"send_transaction_button")
        self.send_transaction_button.setGeometry(QRect(190, 90, 251, 32))
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(560, 1, 81, 41))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 24))
        self.menuGet_Information = QMenu(self.menubar)
        self.menuGet_Information.setObjectName(u"menuGet_Information")
        self.menuAction = QMenu(self.menubar)
        self.menuAction.setObjectName(u"menuAction")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuGet_Information.menuAction())
        self.menubar.addAction(self.menuAction.menuAction())
        self.menuGet_Information.addAction(self.actionRequest_blocksHistory)
        self.menuGet_Information.addAction(self.actionRequest_txHistory)
        self.menuGet_Information.addAction(self.action_show_Find_tx_by_hash_window)
        self.menuGet_Information.addAction(self.actionFind_document)
        self.menuGet_Information.addAction(self.actionShow_my_seed_phrase)
        self.menuAction.addAction(self.actionAdd_KeyPair)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Trusted Wallet", None))
        self.actionRequest_blocksHistory.setText(QCoreApplication.translate("MainWindow", u"Request blocks history", None))
        self.actionRequest_txHistory.setText(QCoreApplication.translate("MainWindow", u"Request my TX history", None))
        self.actionAdd_KeyPair.setText(QCoreApplication.translate("MainWindow", u"Add KeyPair", None))
        self.actionShow_my_seed_phrase.setText(QCoreApplication.translate("MainWindow", u"Show my seed phrase", None))
        self.action_show_Find_tx_by_hash_window.setText(QCoreApplication.translate("MainWindow", u"Find TX by hash", None))
        self.actionFind_document.setText(QCoreApplication.translate("MainWindow", u"Find document", None))
        self.create_transaction_button.setText(QCoreApplication.translate("MainWindow", u"Create Transaction", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Address:", None))
        self.sign_transaction_button.setText(QCoreApplication.translate("MainWindow", u"Sign Transaction", None))
        self.send_transaction_button.setText(QCoreApplication.translate("MainWindow", u"Send Transaction", None))
        self.menuGet_Information.setTitle(QCoreApplication.translate("MainWindow", u"Get Information", None))
        self.menuAction.setTitle(QCoreApplication.translate("MainWindow", u"Action", None))
    # retranslateUi

