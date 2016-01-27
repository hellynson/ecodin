# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 13:29:19 2012

@author: Hellynson
"""

from PyQt4 import QtCore, QtGui
#from config import modelo
import config
from UI.wpDensidadeUi import Ui_WizardPageDensidade_dependente_independente

class WPDensidade_dependente_independente(QtGui.QWizardPage):
    def __init__(self, parent=None):
        '''Wizard Page'''
        QtGui.QWidget.__init__(self, parent) 
        self.uiW = Ui_WizardPageDensidade_dependente_independente()#construtor
        self.uiW.setupUi(self)
        
        QtCore.QObject.connect(self.uiW.rbDensidadeIndependente, 
                             QtCore.SIGNAL("toggled(bool)"), 
                             self, QtCore.SIGNAL("completeChanged()"))

        QtCore.QObject.connect(self.uiW.rbDensidadeDependente,
                               QtCore.SIGNAL("toggled(bool)"), 
                                self, QtCore.SIGNAL("completeChanged()")) 

    def nextId(self):
        '''Method that goes to the next or previous window in the Wizard'''
        if self.uiW.rbDensidadeIndependente.isChecked() == True: #checks if the radio button was clicked
         
             return config.pageIDs["WPLogistico"]#go to next page
         
        elif self.uiW.rbDensidadeDependente.isChecked() == True: 
 
             return config.pageIDs["WPExponencial"]
  
        else:
            return 0