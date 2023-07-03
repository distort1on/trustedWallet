# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_login_window(object):
    def setupUi(self, login_window):
        if not login_window.objectName():
            login_window.setObjectName(u"login_window")
        login_window.resize(530, 326)
        self.register_button = QPushButton(login_window)
        self.register_button.setObjectName(u"register_button")
        self.register_button.setGeometry(QRect(370, 280, 100, 35))
        self.logo_label = QLabel(login_window)
        self.logo_label.setObjectName(u"logo_label")
        self.logo_label.setGeometry(QRect(220, 7, 100, 80))
        self.logo_label.setPixmap(QPixmap(u"resources/TrustedWallet_logo.png"))
        self.layoutWidget = QWidget(login_window)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(60, 80, 411, 201))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.login_input = QLineEdit(self.layoutWidget)
        self.login_input.setObjectName(u"login_input")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_input.sizePolicy().hasHeightForWidth())
        self.login_input.setSizePolicy(sizePolicy)
        self.login_input.setMinimumSize(QSize(0, 35))
        self.login_input.setEchoMode(QLineEdit.Normal)

        self.verticalLayout.addWidget(self.login_input)

        self.password_input = QLineEdit(self.layoutWidget)
        self.password_input.setObjectName(u"password_input")
        sizePolicy.setHeightForWidth(self.password_input.sizePolicy().hasHeightForWidth())
        self.password_input.setSizePolicy(sizePolicy)
        self.password_input.setMinimumSize(QSize(0, 35))
        self.password_input.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.password_input)

        self.login_button = QPushButton(self.layoutWidget)
        self.login_button.setObjectName(u"login_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.login_button.sizePolicy().hasHeightForWidth())
        self.login_button.setSizePolicy(sizePolicy1)
        self.login_button.setMinimumSize(QSize(100, 35))

        self.verticalLayout.addWidget(self.login_button)

        self.verticalSpacer = QSpacerItem(20, 35, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.restore_wallet_button = QPushButton(login_window)
        self.restore_wallet_button.setObjectName(u"restore_wallet_button")
        self.restore_wallet_button.setGeometry(QRect(60, 280, 100, 35))

        self.retranslateUi(login_window)

        QMetaObject.connectSlotsByName(login_window)
    # setupUi

    def retranslateUi(self, login_window):
        login_window.setWindowTitle(QCoreApplication.translate("login_window", u"Sign in", None))
        self.register_button.setText(QCoreApplication.translate("login_window", u"Create Wallet", None))
        self.logo_label.setText("")
        self.login_input.setInputMask("")
        self.login_input.setText("")
        self.login_input.setPlaceholderText(QCoreApplication.translate("login_window", u"Login:", None))
        self.password_input.setInputMask("")
        self.password_input.setText("")
        self.password_input.setPlaceholderText(QCoreApplication.translate("login_window", u"Password:", None))
        self.login_button.setText(QCoreApplication.translate("login_window", u"Sign in", None))
        self.restore_wallet_button.setText(QCoreApplication.translate("login_window", u"Restore Wallet", None))
    # retranslateUi

