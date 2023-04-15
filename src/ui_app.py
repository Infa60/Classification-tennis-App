# -*- coding: utf-8 -*-
import os

################################################################################
## Form generated from reading UI file 'ui_application.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QLCDNumber,
    QLabel, QListWidget, QListWidgetItem, QPushButton,
    QRadioButton, QSizePolicy, QWidget)
from data import root

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")

        self.id = QFontDatabase.addApplicationFont(os.getcwd() + "/data/SharpSansBold.ttf")

        mainWindow.resize(1200, 581)
        mainWindow.setMinimumSize(QSize(1200, 581))
        mainWindow.setMaximumSize(QSize(1200, 581))
        mainWindow.setAutoFillBackground(False)
        mainWindow.setStyleSheet(u"background-color: rgb(22, 27, 34);")
        self.laterality = QGroupBox(mainWindow)
        self.laterality.setObjectName(u"laterality")
        self.laterality.setGeometry(QRect(20, 120, 271, 91))
        self.laterality.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 16pt \"Sharp Sans\";")
        self.rightHanded = QRadioButton(self.laterality)
        self.rightHanded.setObjectName(u"rightHanded")
        self.rightHanded.setChecked(True)
        self.rightHanded.setGeometry(QRect(150, 30, 101, 51))
        self.rightHanded.setStyleSheet(u"font: 75 11pt \"Sharp Sans\";")
        self.leftHanded = QRadioButton(self.laterality)
        self.leftHanded.setObjectName(u"leftHanded")
        self.leftHanded.setGeometry(QRect(10, 30, 111, 51))
        self.leftHanded.setStyleSheet(u"font: 75 11pt \"Sharp Sans\";")
        self.title = QLabel(mainWindow)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(370, 20, 501, 71))
        self.title.setStyleSheet(u"font: 75 36pt \"Sharp Sans\";\n"
"color: rgb(213, 220, 60);\n"
"text-align:center;")
        self.IMUinformations = QGroupBox(mainWindow)
        self.IMUinformations.setObjectName(u"IMUinformations")
        self.IMUinformations.setGeometry(QRect(310, 120, 861, 371))
        self.IMUinformations.setStyleSheet(u"font: 75 16pt \"Sharp Sans\";\n"
"color: rgb(255, 255, 255);")
        self.message_connexion = QLabel(self.IMUinformations)
        self.message_connexion.setObjectName(u"message_connexion")
        self.message_connexion.setGeometry(QRect(390, 290, 461, 61))
        self.message_connexion.setStyleSheet(u"color: rgb(193, 78, 78);")
        self.adresseMac = QLabel(self.IMUinformations)
        self.adresseMac.setObjectName(u"adresseMac")
        self.adresseMac.setGeometry(QRect(20, 50, 371, 41))
        self.adresseMac.setStyleSheet(u"font: 75 11pt \"Sharp Sans\";")
        self.connexion_statut = QLabel(self.IMUinformations)
        self.connexion_statut.setObjectName(u"connexion_statut")
        self.connexion_statut.setGeometry(QRect(20, 90, 401, 41))
        self.connexion_statut.setStyleSheet(u"font: 75 11pt \"Sharp Sans\";")
        self.sdk_version = QLabel(self.IMUinformations)
        self.sdk_version.setObjectName(u"sdk_version")
        self.sdk_version.setGeometry(QRect(20, 170, 721, 41))
        self.sdk_version.setStyleSheet(u"font: 75 11pt \"Sharp Sans\";")
        self.file_path = QLabel(self.IMUinformations)
        self.file_path.setObjectName(u"file_path")
        self.file_path.setGeometry(QRect(20, 210, 451, 41))
        self.file_path.setStyleSheet(u"font: 75 11pt \"Sharp Sans\";")
        self.mode_record = QLabel(self.IMUinformations)
        self.mode_record.setObjectName(u"mode_record")
        self.mode_record.setGeometry(QRect(20, 130, 431, 41))
        self.mode_record.setStyleSheet(u"font: 75 11pt \"Sharp Sans\";")
        self.startRecord = QPushButton(mainWindow)
        self.startRecord.setObjectName(u"startRecord")
        self.startRecord.setGeometry(QRect(310, 500, 271, 61))
        self.startRecord.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"	font: 75 15pt \"Sharp Sans\";\n"
"	background-color: #DFFF4F;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: #BCEB33;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #BCEB33;\n"
"    border-style: inset;\n"
"}")
        self.resetRecord = QPushButton(mainWindow)
        self.resetRecord.setObjectName(u"resetRecord")
        self.resetRecord.setGeometry(QRect(900, 500, 271, 61))
        self.resetRecord.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"	font: 75 15pt \"Sharp Sans\";\n"
"	background-color: #DFFF4F;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: #BCEB33;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #BCEB33;\n"
"    border-style: inset;\n"
"}")
        self.stopRecord = QPushButton(mainWindow)
        self.stopRecord.setObjectName(u"stopRecord")
        self.stopRecord.setGeometry(QRect(600, 500, 281, 61))
        self.stopRecord.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"	font: 75 15pt \"Sharp Sans\";\n"
"	background-color: #DFFF4F;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: #BCEB33;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #BCEB33;\n"
"    border-style: inset;\n"
"}")
        self.timer_container = QFrame(mainWindow)
        self.timer_container.setObjectName(u"timer_container")
        self.timer_container.setGeometry(QRect(20, 420, 271, 141))
        self.timer_container.setStyleSheet(u"border: 1px solid rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.timer_container.setFrameShape(QFrame.StyledPanel)
        self.timer_container.setFrameShadow(QFrame.Raised)
        self.timer_ldc = QLCDNumber(self.timer_container)
        self.timer_ldc.setObjectName(u"timer_ldc")
        self.timer_ldc.setGeometry(QRect(10, 60, 251, 71))
        self.timer_ldc.setStyleSheet(u"color: rgb(213, 220, 60);\n"
"border-radius: 5px;\n"
"")
        self.timer_ldc.setProperty("value", 0.000000000000000)
        self.timer_label = QLabel(self.timer_container)
        self.timer_label.setObjectName(u"timer_label")
        self.timer_label.setGeometry(QRect(10, 10, 251, 41))
        self.timer_label.setStyleSheet(u"font: 75 16pt \"Sharp Sans\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.connetionBtn_2 = QPushButton(mainWindow)
        self.connetionBtn_2.setObjectName(u"connetionBtn_2")
        self.connetionBtn_2.setGeometry(QRect(20, 310, 271, 41))
        self.connetionBtn_2.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"	font: 75 13pt \"Sharp Sans\";\n"
"	background-color: #DFFF4F;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: #BCEB33;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #BCEB33;\n"
"    border-style: inset;\n"
"}")
        self.listWidget = QListWidget(mainWindow)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(20, 220, 271, 71))
        self.listWidget.setStyleSheet(u"font: 75 13pt \"Sharp Sans\";\n"
"color: rgb(255, 255, 255);")
        self.connetionBtn_3 = QPushButton(mainWindow)
        self.connetionBtn_3.setObjectName(u"connetionBtn_3")
        self.connetionBtn_3.setGeometry(QRect(20, 360, 271, 41))
        self.connetionBtn_3.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"	font: 75 13pt \"Sharp Sans\";\n"
"	background-color: #DFFF4F;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: #BCEB33;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #BCEB33;\n"
"    border-style: inset;\n"
"}")
        self.message_connexion_2 = QLabel(mainWindow)
        self.message_connexion_2.setObjectName(u"message_connexion_2")
        self.message_connexion_2.setGeometry(QRect(10, 10, 231, 21))
        self.message_connexion_2.setStyleSheet(u"color: rgb(193, 78, 78);\n"
"font: 75 11pt \"Sharp Sans\";")
        self.logo = QLabel(mainWindow)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(1050, 0, 131, 121))
        self.logo.setPixmap(QPixmap(u":/Logo/logo_app.png"))
        self.logo.setScaledContents(True)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"Form", None))
        self.laterality.setTitle(QCoreApplication.translate("mainWindow", u"Lat\u00e9ralit\u00e9", None))
        self.rightHanded.setText(QCoreApplication.translate("mainWindow", u"Droitier", None))
        self.leftHanded.setText(QCoreApplication.translate("mainWindow", u"Gaucher", None))
        self.title.setText(QCoreApplication.translate("mainWindow", u"TennisPrediction", None))
#if QT_CONFIG(tooltip)
        self.IMUinformations.setToolTip(QCoreApplication.translate("mainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sharp Sans Display No2'; font-size:14pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#aa0000;\">Informations g\u00e9n\u00e9rale sur l'IMU connect\u00e9</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.IMUinformations.setTitle(QCoreApplication.translate("mainWindow", u"Informations IMU", None))
        self.message_connexion.setText(QCoreApplication.translate("mainWindow", u"Aucun IMU connect\u00e9 ...", None))
        self.adresseMac.setText(QCoreApplication.translate("mainWindow", u"Adresse MAC :", None))
        self.connexion_statut.setText(QCoreApplication.translate("mainWindow", u"Statut de connexion :", None))
        self.sdk_version.setText(QCoreApplication.translate("mainWindow", u"Version SDK :", None))
        self.file_path.setText(QCoreApplication.translate("mainWindow", u"Emplacement fichiers : ", None))
        self.mode_record.setText(QCoreApplication.translate("mainWindow", u"Mode d'enregistrement :", None))
        self.startRecord.setText(QCoreApplication.translate("mainWindow", u"START", None))
        self.resetRecord.setText(QCoreApplication.translate("mainWindow", u"R\u00e9sultats", None))
        self.stopRecord.setText(QCoreApplication.translate("mainWindow", u"STOP", None))
        self.timer_label.setText(QCoreApplication.translate("mainWindow", u"Timer ", None))
        self.connetionBtn_2.setText(QCoreApplication.translate("mainWindow", u"Connexion IMU", None))
        self.connetionBtn_3.setText(QCoreApplication.translate("mainWindow", u"D\u00e9connexion IMU", None))
        self.message_connexion_2.setText(QCoreApplication.translate("mainWindow", u"Chargement du model ...", None))
        self.logo.setText("")
    # retranslateUi

