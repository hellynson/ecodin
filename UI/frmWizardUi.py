# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Hellynson\UNIFAL\IC\teste10\frmWizard.ui'
#
# Created: Fri Mar 16 16:01:06 2012
#      by: PyQt4 UI code generator 4.5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Wizard(object):
    def setupUi(self, Wizard):
        Wizard.setObjectName("EcoDin")
        Wizard.setWindowModality(QtCore.Qt.WindowModal)
        Wizard.resize(591, 500)
        Wizard.setMinimumSize(QtCore.QSize(500, 450))
        Wizard.setMaximumSize(QtCore.QSize(591, 500))
        Wizard.setOptions(QtGui.QWizard.HaveHelpButton|QtGui.QWizard.IndependentPages)
        self.wizardPage0 = QtGui.QWizardPage()
        self.wizardPage0.setObjectName("wizardPage0")
        self.layoutWidget = QtGui.QWidget(self.wizardPage0)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 70, 551, 221))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        Wizard.addPage(self.wizardPage0)

        self.retranslateUi(Wizard)
        QtCore.QMetaObject.connectSlotsByName(Wizard)

    def retranslateUi(self, Wizard):
        Wizard.setWindowTitle(QtGui.QApplication.translate("EcoDin", "Wizard", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("EcoDin", "Bem-vindo ao Assistente de Escolha de Modelo", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("EcoDin", "Com este Assistente, você poderá escolher melhor os parâmetros com os quais pretente trabalhar e o software indicará qual o melhor modelo a ser aplicado.", None, QtGui.QApplication.UnicodeUTF8))

