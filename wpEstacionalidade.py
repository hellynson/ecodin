# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 13:29:19 2012

@author: Hellynson
"""

from PyQt4 import QtCore, QtGui
import config
from UI.wpEstacionalidadeUi import Ui_WizardPageContinuo_discreto

class WPContinuoDiscreto(QtGui.QWizardPage):
    def __init__(self, parent=None):
        '''Wizard Page'''
        QtGui.QWidget.__init__(self, parent) 
        self.uiW = Ui_WizardPageContinuo_discreto()#construtor
        self.uiW.setupUi(self)
        
        QtCore.QObject.connect(self.uiW.rbContinuo, 
                             QtCore.SIGNAL("toggled(bool)"), 
                             self, QtCore.SIGNAL("completeChanged()"))

        QtCore.QObject.connect(self.uiW.rbDiscreto,
                               QtCore.SIGNAL("toggled(bool)"), 
                                self, QtCore.SIGNAL("completeChanged()")) 

    def nextId(self):
        '''Method that goes to the next or previous window in the Wizard'''
        if self.uiW.rbContinuo.isChecked() == True: #checks if the radio button was clicked
         
             config.modelo["modeloEscolhido"]="malthus"
             print "Dicionario: ",config.modelo
            
             return config.pageIDs["wp_sem_implementar"]#go to next page
         
        elif self.uiW.rbDiscreto.isChecked() == True: 
        
  
             return config.pageIDs["wp_sem_implementar"]#go to next page
  
        else:
            return 0