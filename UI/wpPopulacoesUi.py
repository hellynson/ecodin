# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wpPopulacoes.ui'
#
# Created: Mon Jun 18 08:55:40 2012
#      by: PyQt4 UI code generator 4.5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_WizardPagePopulacoes(object):
    def setupUi(self, WizardPage):
        WizardPage.setObjectName("WizardPage")
        WizardPage.resize(507, 430)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(WizardPage)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtGui.QLabel(WizardPage)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_5 = QtGui.QLabel(WizardPage)
        self.label_5.setPixmap(QtGui.QPixmap("../Imagens/Imagens programa/ALiger.jpg"))
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.rbNpop = QtGui.QRadioButton(WizardPage)
        self.rbNpop.setObjectName("rbNpop")
        self.gridLayout.addWidget(self.rbNpop, 1, 0, 1, 1)
        self.rbUMApop = QtGui.QRadioButton(WizardPage)
        self.rbUMApop.setChecked(True)
        self.rbUMApop.setObjectName("rbUMApop")
        self.gridLayout.addWidget(self.rbUMApop, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.groupBox = QtGui.QGroupBox(WizardPage)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setItalic(True)
        font.setBold(False)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.retranslateUi(WizardPage)
        QtCore.QMetaObject.connectSlotsByName(WizardPage)

    def retranslateUi(self, WizardPage):
        WizardPage.setWindowTitle(QtGui.QApplication.translate("WizardPage", "WizardPage", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("WizardPage", "Quantas POPULAÇÕES da espécie existem?", None, QtGui.QApplication.UnicodeUTF8))
        self.rbNpop.setText(QtGui.QApplication.translate("WizardPage", "Várias populações", None, QtGui.QApplication.UnicodeUTF8))
        self.rbUMApop.setText(QtGui.QApplication.translate("WizardPage", "Uma população", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("WizardPage", "Descrição", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("WizardPage", "No conceito de população, salienta-se que a escala espacial (área) e temporal (tempo) são importantes componentes. Assim, uma população é definida pelo conjunto de individuos de uma mesma espécie distribuída na mesma área e ao mesmo tempo", None, QtGui.QApplication.UnicodeUTF8))

