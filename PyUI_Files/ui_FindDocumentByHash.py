# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FindDocumentByHash.ui'
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

class Ui_find_document_by_hash_window(object):
    def setupUi(self, find_document_by_hash_window):
        if not find_document_by_hash_window.objectName():
            find_document_by_hash_window.setObjectName(u"find_document_by_hash_window")
        find_document_by_hash_window.resize(630, 115)
        self.document_path_line_edit = QLineEdit(find_document_by_hash_window)
        self.document_path_line_edit.setObjectName(u"document_path_line_edit")
        self.document_path_line_edit.setGeometry(QRect(18, 10, 591, 35))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.document_path_line_edit.sizePolicy().hasHeightForWidth())
        self.document_path_line_edit.setSizePolicy(sizePolicy)
        self.document_path_line_edit.setMinimumSize(QSize(0, 35))
        self.document_path_line_edit.setEchoMode(QLineEdit.Normal)
        self.document_path_line_edit.setReadOnly(True)
        self.select_document_button = QPushButton(find_document_by_hash_window)
        self.select_document_button.setObjectName(u"select_document_button")
        self.select_document_button.setGeometry(QRect(20, 50, 240, 35))
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.select_document_button.sizePolicy().hasHeightForWidth())
        self.select_document_button.setSizePolicy(sizePolicy1)
        self.select_document_button.setMinimumSize(QSize(100, 35))
        self.search_document_by_hash_button = QPushButton(find_document_by_hash_window)
        self.search_document_by_hash_button.setObjectName(u"search_document_by_hash_button")
        self.search_document_by_hash_button.setGeometry(QRect(370, 50, 240, 35))
        sizePolicy1.setHeightForWidth(self.search_document_by_hash_button.sizePolicy().hasHeightForWidth())
        self.search_document_by_hash_button.setSizePolicy(sizePolicy1)
        self.search_document_by_hash_button.setMinimumSize(QSize(100, 35))

        self.retranslateUi(find_document_by_hash_window)

        QMetaObject.connectSlotsByName(find_document_by_hash_window)
    # setupUi

    def retranslateUi(self, find_document_by_hash_window):
        find_document_by_hash_window.setWindowTitle(QCoreApplication.translate("find_document_by_hash_window", u"Find document by hash", None))
        self.document_path_line_edit.setInputMask("")
        self.document_path_line_edit.setText("")
        self.document_path_line_edit.setPlaceholderText(QCoreApplication.translate("find_document_by_hash_window", u"Document path:", None))
        self.select_document_button.setText(QCoreApplication.translate("find_document_by_hash_window", u"Select document", None))
        self.search_document_by_hash_button.setText(QCoreApplication.translate("find_document_by_hash_window", u"Search", None))
    # retranslateUi

