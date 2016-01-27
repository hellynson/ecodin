# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Hellynson\UNIFAL\IC\teste10\wp_sem_implementar.ui'
#
# Created: Fri Mar 16 13:41:32 2012
#      by: PyQt4 UI code generator 4.5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_wpSemImplementar(object):
    def setupUi(self, WizardPage):
        WizardPage.setObjectName("WizardPage")
        WizardPage.resize(640, 480)
        self.label = QtGui.QLabel(WizardPage)
        self.label.setGeometry(QtCore.QRect(190, 110, 411, 181))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(WizardPage)
        QtCore.QMetaObject.connectSlotsByName(WizardPage)

    def retranslateUi(self, WizardPage):
        WizardPage.setWindowTitle(QtGui.QApplication.translate("WizardPage", "WizardPage", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("WizardPage", "NÃO IMPLEMENTADO!", None, QtGui.QApplication.UnicodeUTF8))

