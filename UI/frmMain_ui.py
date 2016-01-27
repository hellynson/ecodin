# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmMain.ui'
#
# Created: Fri Jul 13 16:04:17 2012
#      by: PyQt4 UI code generator 4.5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(778, 587)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mdiArea = QtGui.QMdiArea(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mdiArea.sizePolicy().hasHeightForWidth())
        self.mdiArea.setSizePolicy(sizePolicy)
        self.mdiArea.setAutoFillBackground(True)
        self.mdiArea.setObjectName("mdiArea")
        self.horizontalLayout.addWidget(self.mdiArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 778, 22))
        self.menubar.setObjectName("menubar")
        self.menuModelo = QtGui.QMenu(self.menubar)
        self.menuModelo.setObjectName("menuModelo")
        self.menuAjuda = QtGui.QMenu(self.menubar)
        self.menuAjuda.setObjectName("menuAjuda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionModelo = QtGui.QAction(MainWindow)
        self.actionModelo.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionModelo.setObjectName("actionModelo")
        self.actionSobre_o_Software = QtGui.QAction(MainWindow)
        self.actionSobre_o_Software.setObjectName("actionSobre_o_Software")
        self.actionSair = QtGui.QAction(MainWindow)
        self.actionSair.setObjectName("actionSair")
        self.actionComo_usar = QtGui.QAction(MainWindow)
        self.actionComo_usar.setObjectName("actionComo_usar")
        self.actionDados = QtGui.QAction(MainWindow)
        self.actionDados.setObjectName("actionDados")
        self.menuModelo.addAction(self.actionModelo)
        self.menuModelo.addAction(self.actionDados)
        self.menuModelo.addSeparator()
        self.menuModelo.addAction(self.actionSair)
        self.menuAjuda.addAction(self.actionSobre_o_Software)
        self.menuAjuda.addAction(self.actionComo_usar)
        self.menubar.addAction(self.menuModelo.menuAction())
        self.menubar.addAction(self.menuAjuda.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.menuModelo.setTitle(QtGui.QApplication.translate("MainWindow", "Novo", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAjuda.setTitle(QtGui.QApplication.translate("MainWindow", "Ajuda", None, QtGui.QApplication.UnicodeUTF8))
        self.actionModelo.setText(QtGui.QApplication.translate("MainWindow", "Gráfico de modelo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionModelo.setToolTip(QtGui.QApplication.translate("MainWindow", "m", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSobre_o_Software.setText(QtGui.QApplication.translate("MainWindow", "Sobre o Software", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSair.setText(QtGui.QApplication.translate("MainWindow", "Sair", None, QtGui.QApplication.UnicodeUTF8))
        self.actionComo_usar.setText(QtGui.QApplication.translate("MainWindow", "Como usar?", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDados.setText(QtGui.QApplication.translate("MainWindow", "Gráfico de dados", None, QtGui.QApplication.UnicodeUTF8))

