# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RegisterWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_register_window(object):
    def setupUi(self, register_window):
        if not register_window.objectName():
            register_window.setObjectName(u"register_window")
        register_window.resize(530, 326)
        self.logo_label = QLabel(register_window)
        self.logo_label.setObjectName(u"logo_label")
        self.logo_label.setGeometry(QRect(220, 7, 100, 80))
        self.logo_label.setPixmap(QPixmap(u"resources/TrustedWallet_logo.png"))
        self.layoutWidget = QWidget(register_window)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(60, 90, 411, 201))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.create_login_input = QLineEdit(self.layoutWidget)
        self.create_login_input.setObjectName(u"create_login_input")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.create_login_input.sizePolicy().hasHeightForWidth())
        self.create_login_input.setSizePolicy(sizePolicy)
        self.create_login_input.setMinimumSize(QSize(0, 35))
        self.create_login_input.setEchoMode(QLineEdit.Normal)

        self.verticalLayout.addWidget(self.create_login_input)

        self.create_password_input = QLineEdit(self.layoutWidget)
        self.create_password_input.setObjectName(u"create_password_input")
        sizePolicy.setHeightForWidth(self.create_password_input.sizePolicy().hasHeightForWidth())
        self.create_password_input.setSizePolicy(sizePolicy)
        self.create_password_input.setMinimumSize(QSize(0, 35))
        self.create_password_input.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.create_password_input)

        self.create_password_input_2 = QLineEdit(self.layoutWidget)
        self.create_password_input_2.setObjectName(u"create_password_input_2")
        sizePolicy.setHeightForWidth(self.create_password_input_2.sizePolicy().hasHeightForWidth())
        self.create_password_input_2.setSizePolicy(sizePolicy)
        self.create_password_input_2.setMinimumSize(QSize(0, 35))
        self.create_password_input_2.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.create_password_input_2)

        self.register_button = QPushButton(self.layoutWidget)
        self.register_button.setObjectName(u"register_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.register_button.sizePolicy().hasHeightForWidth())
        self.register_button.setSizePolicy(sizePolicy1)
        self.register_button.setMinimumSize(QSize(100, 35))

        self.verticalLayout.addWidget(self.register_button)

        self.verticalSpacer = QSpacerItem(20, 35, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(register_window)

        QMetaObject.connectSlotsByName(register_window)
    # setupUi

    def retranslateUi(self, register_window):
        register_window.setWindowTitle(QCoreApplication.translate("register_window", u"Create Wallet", None))
        self.logo_label.setText("")
        self.create_login_input.setInputMask("")
        self.create_login_input.setText("")
        self.create_login_input.setPlaceholderText(QCoreApplication.translate("register_window", u"Login:", None))
        self.create_password_input.setInputMask("")
        self.create_password_input.setText("")
        self.create_password_input.setPlaceholderText(QCoreApplication.translate("register_window", u"Password:", None))
        self.create_password_input_2.setInputMask("")
        self.create_password_input_2.setText("")
        self.create_password_input_2.setPlaceholderText(QCoreApplication.translate("register_window", u"Repeat password:", None))
        self.register_button.setText(QCoreApplication.translate("register_window", u"Create Wallet", None))
    # retranslateUi

