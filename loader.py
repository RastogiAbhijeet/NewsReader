# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loader.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(0, 186, 401, 16))
        self.progressBar.setStyleSheet("border:None;\n"
"background-color:black;")
        self.progressBar.setProperty("value", 10)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

Obj = Ui_Form()
Obj.setupUi()
