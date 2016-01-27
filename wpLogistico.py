# -*- coding: utf-8 -*-
"""
Created on Thu May 03 23:33:32 2012

@author: Hellynson
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 13:29:19 2012

@author: Hellynson
"""

from PyQt4 import QtCore, QtGui
#from config import modelo
import config
from UI.wpLogisticoUi import Ui_WizardPageLogistico
import csv

class WPLogistico(QtGui.QWizardPage):
    def __init__(self, parent=None):
        '''Wizard page: Selected Model Logistic'''
        
        QtGui.QWidget.__init__(self, parent) 
        self.ui = Ui_WizardPageLogistico()#construtor
        self.ui.setupUi(self)
        self.connect(self.ui.lineEditPop, 
                    QtCore.SIGNAL("editingFinished()"),
                    QtCore.SIGNAL("completeChanged()"))
        self.connect(self.ui.lineEditCresc, 
                    QtCore.SIGNAL("editingFinished()"),
                    QtCore.SIGNAL("completeChanged()"))
        self.connect(self.ui.lineEditCapSup, 
                    QtCore.SIGNAL("editingFinished()"),
                    QtCore.SIGNAL("completeChanged()"))
        self.connect(self.ui.lineEditTempo, 
                    QtCore.SIGNAL("editingFinished()"),
                    QtCore.SIGNAL("completeChanged()"))
        
    def nextId(self):
        '''Method that goes to the next or previous window in the Wizard'''
        return -1#Wizard finished
    
    def isComplete(self):
        '''Method that rehabilitates the button Ok if the user filled all lines edits correctly'''
        print "isComplete()"

        if self.ui.lineEditCapSup.text() != "" and\
           self.ui.lineEditCresc.text() != "" and\
           self.ui.lineEditPop.text() != "" and\
           self.ui.lineEditTempo.text() != "":
            config.modelo["populacaoInicial"]= float(self.ui.lineEditPop.text())
            config.modelo["capacidadeSuporte"] = float(self.ui.lineEditCapSup.text())
            config.modelo["taxaCrescimento"] = float(self.ui.lineEditCresc.text())
            config.modelo["tempo"]= float(self.ui.lineEditTempo.text())
            config.modelo["modeloEscolhido"] = "logistico"
            return True
        else:
            return False
