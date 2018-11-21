# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from time import sleep
from class_spam import Spam
import subprocess

class Ui_Dialog(object):
    def __init__(self):
        self.salida = Spam()
    def mensaje(self, titulo, mensaje):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(titulo)
        msgBox.setText(mensaje)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def boton_aceptar(self):
        texto = self.lineEdit.text()
        N = self.spinBox.value()
        if texto == '':
            self.mensaje('', "Ingrese algún texto")
            return(None)
        
        if self.radioButton_2.isChecked():
            self.salida.cambiar_de_ventana()
        elif self.radioButton.isChecked():
            sleep(2)
        else:
            self.mensaje('', "Selecione algúna opción")
            return(None)
        
        self.salida.enviar_mensajes(texto, N)
        return(None)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(275, 189)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 20, 220, 149))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.radioButton = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 2, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 2)
        self.radioButton_2 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.boton_aceptar)
        self.gridLayout.addWidget(self.pushButton, 3, 1, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(999)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 1, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", ""))
        self.radioButton.setText(_translate("Dialog", "2s"))
        self.radioButton_2.setText(_translate("Dialog", "alt+tab"))
        self.pushButton.setText(_translate("Dialog", "Aceptar"))


