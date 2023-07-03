# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FindTxByHashWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_tx_hash_input_window(object):
    def setupUi(self, tx_hash_input_window):
        if not tx_hash_input_window.objectName():
            tx_hash_input_window.setObjectName(u"tx_hash_input_window")
        tx_hash_input_window.resize(540, 115)
        self.tx_hash_input = QLineEdit(tx_hash_input_window)
        self.tx_hash_input.setObjectName(u"tx_hash_input")
        self.tx_hash_input.setGeometry(QRect(18, 10, 501, 35))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tx_hash_input.sizePolicy().hasHeightForWidth())
        self.tx_hash_input.setSizePolicy(sizePolicy)
        self.tx_hash_input.setMinimumSize(QSize(0, 35))
        self.tx_hash_input.setEchoMode(QLineEdit.Normal)
        self.get_tx_by_hash_button = QPushButton(tx_hash_input_window)
        self.get_tx_by_hash_button.setObjectName(u"get_tx_by_hash_button")
        self.get_tx_by_hash_button.setGeometry(QRect(20, 50, 501, 35))
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.get_tx_by_hash_button.sizePolicy().hasHeightForWidth())
        self.get_tx_by_hash_button.setSizePolicy(sizePolicy1)
        self.get_tx_by_hash_button.setMinimumSize(QSize(100, 35))

        self.retranslateUi(tx_hash_input_window)

        QMetaObject.connectSlotsByName(tx_hash_input_window)
    # setupUi

    def retranslateUi(self, tx_hash_input_window):
        tx_hash_input_window.setWindowTitle(QCoreApplication.translate("tx_hash_input_window", u"Find TX by hash", None))
        self.tx_hash_input.setInputMask("")
        self.tx_hash_input.setText("")
        self.tx_hash_input.setPlaceholderText(QCoreApplication.translate("tx_hash_input_window", u"Tx hash:", None))
        self.get_tx_by_hash_button.setText(QCoreApplication.translate("tx_hash_input_window", u"Search", None))
    # retranslateUi

