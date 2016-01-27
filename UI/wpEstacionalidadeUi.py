# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wpEstacionalidade.ui'
#
# Created: Mon Jun 18 08:53:10 2012
#      by: PyQt4 UI code generator 4.5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_WizardPageContinuo_discreto(object):
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
        self.rbContinuo = QtGui.QRadioButton(WizardPage)
        self.rbContinuo.setChecked(True)
        self.rbContinuo.setObjectName("rbContinuo")
        self.gridLayout.addWidget(self.rbContinuo, 0, 0, 1, 1)
        self.rbDiscreto = QtGui.QRadioButton(WizardPage)
        self.rbDiscreto.setObjectName("rbDiscreto")
        self.gridLayout.addWidget(self.rbDiscreto, 1, 0, 1, 1)
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
        self.label.setText(QtGui.QApplication.translate("WizardPage", "As variações sazonais tem influência no tamanho da população?", None, QtGui.QApplication.UnicodeUTF8))
        self.rbContinuo.setText(QtGui.QApplication.translate("WizardPage", "Sim", None, QtGui.QApplication.UnicodeUTF8))
        self.rbDiscreto.setText(QtGui.QApplication.translate("WizardPage", "Não", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("WizardPage", "Descrição", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("WizardPage", "...", None, QtGui.QApplication.UnicodeUTF8))

