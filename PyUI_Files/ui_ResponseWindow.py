# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ResponseWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPlainTextEdit, QSizePolicy,
    QWidget)

class Ui_Response(object):
    def setupUi(self, Response):
        if not Response.objectName():
            Response.setObjectName(u"Response")
        Response.resize(1680, 911)
        self.horizontalLayout = QHBoxLayout(Response)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.text_field = QPlainTextEdit(Response)
        self.text_field.setObjectName(u"text_field")
        self.text_field.setReadOnly(True)

        self.horizontalLayout.addWidget(self.text_field)


        self.retranslateUi(Response)

        QMetaObject.connectSlotsByName(Response)
    # setupUi

    def retranslateUi(self, Response):
        Response.setWindowTitle(QCoreApplication.translate("Response", u"Response", None))
    # retranslateUi

