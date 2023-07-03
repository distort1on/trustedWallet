# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RestoreWindow.ui'
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

class Ui_restore_window(object):
    def setupUi(self, restore_window):
        if not restore_window.objectName():
            restore_window.setObjectName(u"restore_window")
        restore_window.resize(530, 326)
        self.logo_label = QLabel(restore_window)
        self.logo_label.setObjectName(u"logo_label")
        self.logo_label.setGeometry(QRect(220, 7, 100, 80))
        self.logo_label.setPixmap(QPixmap(u"resources/TrustedWallet_logo.png"))
        self.layoutWidget = QWidget(restore_window)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(60, 90, 411, 204))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.login_restore_input = QLineEdit(self.layoutWidget)
        self.login_restore_input.setObjectName(u"login_restore_input")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_restore_input.sizePolicy().hasHeightForWidth())
        self.login_restore_input.setSizePolicy(sizePolicy)
        self.login_restore_input.setMinimumSize(QSize(0, 35))
        self.login_restore_input.setEchoMode(QLineEdit.Normal)

        self.verticalLayout.addWidget(self.login_restore_input)

        self.password_restore_input = QLineEdit(self.layoutWidget)
        self.password_restore_input.setObjectName(u"password_restore_input")
        sizePolicy.setHeightForWidth(self.password_restore_input.sizePolicy().hasHeightForWidth())
        self.password_restore_input.setSizePolicy(sizePolicy)
        self.password_restore_input.setMinimumSize(QSize(0, 35))
        self.password_restore_input.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.password_restore_input)

        self.password_restore_input_2 = QLineEdit(self.layoutWidget)
        self.password_restore_input_2.setObjectName(u"password_restore_input_2")
        sizePolicy.setHeightForWidth(self.password_restore_input_2.sizePolicy().hasHeightForWidth())
        self.password_restore_input_2.setSizePolicy(sizePolicy)
        self.password_restore_input_2.setMinimumSize(QSize(0, 35))
        self.password_restore_input_2.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.password_restore_input_2)

        self.seed_phrase_input = QLineEdit(self.layoutWidget)
        self.seed_phrase_input.setObjectName(u"seed_phrase_input")
        sizePolicy.setHeightForWidth(self.seed_phrase_input.sizePolicy().hasHeightForWidth())
        self.seed_phrase_input.setSizePolicy(sizePolicy)
        self.seed_phrase_input.setMinimumSize(QSize(0, 35))
        self.seed_phrase_input.setEchoMode(QLineEdit.Normal)

        self.verticalLayout.addWidget(self.seed_phrase_input)

        self.restore_wallet_button = QPushButton(self.layoutWidget)
        self.restore_wallet_button.setObjectName(u"restore_wallet_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.restore_wallet_button.sizePolicy().hasHeightForWidth())
        self.restore_wallet_button.setSizePolicy(sizePolicy1)
        self.restore_wallet_button.setMinimumSize(QSize(100, 35))

        self.verticalLayout.addWidget(self.restore_wallet_button)

        self.verticalSpacer = QSpacerItem(20, 35, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(restore_window)

        QMetaObject.connectSlotsByName(restore_window)
    # setupUi

    def retranslateUi(self, restore_window):
        restore_window.setWindowTitle(QCoreApplication.translate("restore_window", u"Restore Wallet", None))
        self.logo_label.setText("")
        self.login_restore_input.setInputMask("")
        self.login_restore_input.setText("")
        self.login_restore_input.setPlaceholderText(QCoreApplication.translate("restore_window", u"Login:", None))
        self.password_restore_input.setInputMask("")
        self.password_restore_input.setText("")
        self.password_restore_input.setPlaceholderText(QCoreApplication.translate("restore_window", u"Password:", None))
        self.password_restore_input_2.setInputMask("")
        self.password_restore_input_2.setText("")
        self.password_restore_input_2.setPlaceholderText(QCoreApplication.translate("restore_window", u"Repeat password:", None))
        self.seed_phrase_input.setInputMask("")
        self.seed_phrase_input.setText("")
        self.seed_phrase_input.setPlaceholderText(QCoreApplication.translate("restore_window", u"Seed Phrase:", None))
        self.restore_wallet_button.setText(QCoreApplication.translate("restore_window", u"Restore Wallet", None))
    # retranslateUi

