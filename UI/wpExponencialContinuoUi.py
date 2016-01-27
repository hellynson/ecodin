# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wpExponencialContinuo.ui'
#
# Created: Fri Jul 13 11:53:44 2012
#      by: PyQt4 UI code generator 4.5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_WizardPageExponencial(object):
    def setupUi(self, Ui_WizardPageExponencial):
        Ui_WizardPageExponencial.setObjectName("Ui_WizardPageExponencial")
        Ui_WizardPageExponencial.resize(503, 428)
        self.fmExpContDet = QtGui.QFrame(Ui_WizardPageExponencial)
        self.fmExpContDet.setGeometry(QtCore.QRect(0, 10, 491, 381))
        self.fmExpContDet.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fmExpContDet.setFrameShadow(QtGui.QFrame.Raised)
        self.fmExpContDet.setObjectName("fmExpContDet")
        self.groupBox_3 = QtGui.QGroupBox(self.fmExpContDet)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 0, 301, 331))
        self.groupBox_3.setObjectName("groupBox_3")
        self.layoutWidget = QtGui.QWidget(self.groupBox_3)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 31, 222, 220))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_10 = QtGui.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_10.addWidget(self.label_4, 0, 0, 1, 1)
        self.lineEditPop = QtGui.QLineEdit(self.layoutWidget)
        self.lineEditPop.setObjectName("lineEditPop")
        self.gridLayout_10.addWidget(self.lineEditPop, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_10, 0, 0, 1, 1)
        self.gridLayout_11 = QtGui.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_11.addWidget(self.label_5, 0, 0, 1, 1)
        self.lineEditTempo = QtGui.QLineEdit(self.layoutWidget)
        self.lineEditTempo.setObjectName("lineEditTempo")
        self.gridLayout_11.addWidget(self.lineEditTempo, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_11.addItem(spacerItem, 1, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_11.addItem(spacerItem1, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_11, 1, 0, 1, 1)
        self.gridLayout_12 = QtGui.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.groupBox_5 = QtGui.QGroupBox(self.layoutWidget)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_13 = QtGui.QGridLayout(self.groupBox_5)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.lineEditNat = QtGui.QLineEdit(self.groupBox_5)
        self.lineEditNat.setObjectName("lineEditNat")
        self.gridLayout_13.addWidget(self.lineEditNat, 0, 0, 1, 1)
        self.gridLayout_12.addWidget(self.groupBox_5, 0, 0, 1, 1)
        self.groupBox_6 = QtGui.QGroupBox(self.layoutWidget)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_15 = QtGui.QGridLayout(self.groupBox_6)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.lineEditMort = QtGui.QLineEdit(self.groupBox_6)
        self.lineEditMort.setObjectName("lineEditMort")
        self.gridLayout_15.addWidget(self.lineEditMort, 0, 0, 1, 1)
        self.gridLayout_12.addWidget(self.groupBox_6, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_12, 2, 0, 1, 1)

        self.retranslateUi(Ui_WizardPageExponencial)
        QtCore.QMetaObject.connectSlotsByName(Ui_WizardPageExponencial)

    def retranslateUi(self, Ui_WizardPageExponencial):
        Ui_WizardPageExponencial.setWindowTitle(QtGui.QApplication.translate("Ui_WizardPageExponencial", "WizardPage", None, QtGui.QApplication.UnicodeUTF8))
        self.fmExpContDet.setToolTip(QtGui.QApplication.translate("Ui_WizardPageExponencial", "Quantidade de indivíduos\n"
" no começo da análise", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("Ui_WizardPageExponencial", "Modelo Exponencial Contínuo Determinístico", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Ui_WizardPageExponencial", "População Inicial", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditPop.setText(QtGui.QApplication.translate("Ui_WizardPageExponencial", "100", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Ui_WizardPageExponencial", "Duração/Tempo", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditTempo.setText(QtGui.QApplication.translate("Ui_WizardPageExponencial", "12", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setTitle(QtGui.QApplication.translate("Ui_WizardPageExponencial", "Taxa de Natalidade", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditNat.setText(QtGui.QApplication.translate("Ui_WizardPageExponencial", "0.9", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_6.setTitle(QtGui.QApplication.translate("Ui_WizardPageExponencial", "Taxa de Mortalidade", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditMort.setText(QtGui.QApplication.translate("Ui_WizardPageExponencial", "0.1", None, QtGui.QApplication.UnicodeUTF8))

