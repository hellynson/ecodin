# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Hellynson\UNIFAL\IC\teste12\wizard_page_predacao_competicao.ui'
#
# Created: Fri Apr 13 15:00:39 2012
#      by: PyQt4 UI code generator 4.5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_WizardPagePredacaoCompeticao(object):
    def setupUi(self, WizardPage):
        WizardPage.setObjectName("WizardPage")
        WizardPage.resize(507, 428)
        self.layoutWidget = QtGui.QWidget(WizardPage)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 180, 101, 44))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.rbPredacao = QtGui.QRadioButton(self.layoutWidget)
        self.rbPredacao.setChecked(True)
        self.rbPredacao.setObjectName("rbPredacao")
        self.gridLayout.addWidget(self.rbPredacao, 0, 0, 1, 1)
        self.rbCompeticao = QtGui.QRadioButton(self.layoutWidget)
        self.rbCompeticao.setObjectName("rbCompeticao")
        self.gridLayout.addWidget(self.rbCompeticao, 1, 0, 1, 1)
        self.label = QtGui.QLabel(WizardPage)
        self.label.setGeometry(QtCore.QRect(60, 30, 251, 41))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(WizardPage)
        self.label_2.setGeometry(QtCore.QRect(60, 90, 301, 71))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(WizardPage)
        QtCore.QMetaObject.connectSlotsByName(WizardPage)

    def retranslateUi(self, WizardPage):
        WizardPage.setWindowTitle(QtGui.QApplication.translate("WizardPage", "WizardPage", None, QtGui.QApplication.UnicodeUTF8))
        self.rbPredacao.setText(QtGui.QApplication.translate("WizardPage", "Predação", None, QtGui.QApplication.UnicodeUTF8))
        self.rbCompeticao.setText(QtGui.QApplication.translate("WizardPage", "Competição", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("WizardPage", "Qual o tipo de concorrência?", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("WizardPage", "Texto texto texto texto texto texto texto ", None, QtGui.QApplication.UnicodeUTF8))

