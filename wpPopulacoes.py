# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 13:29:19 2012

@author: Hellynson
"""

from PyQt4 import QtCore, QtGui
#from config import modelo
import config
from UI.wpPopulacoesUi import Ui_WizardPagePopulacoes

class WPPopulacoes(QtGui.QWizardPage):
    def __init__(self, parent=None):
        '''Wizard Page'''
        
        QtGui.QWidget.__init__(self, parent) 
        self.uiW = Ui_WizardPagePopulacoes()#construtor
        self.uiW.setupUi(self)
        
        QtCore.QObject.connect(self.uiW.rbUMApop, 
                             QtCore.SIGNAL("toggled(bool)"), 
                             self, QtCore.SIGNAL("completeChanged()"))

        QtCore.QObject.connect(self.uiW.rbNpop,
                               QtCore.SIGNAL("toggled(bool)"), 
                                self, QtCore.SIGNAL("completeChanged()")) 

    def nextId(self):
        '''Method that goes to the next or previous window in the Wizard'''
        if self.uiW.rbUMApop.isChecked() == True:#checks if the radio button was clicked
         

         
             return config.pageIDs["WPDensidade_dependente_independente"]#go to next page
         
        elif self.uiW.rbNpop.isChecked() == True: 
        

             print u"Você escolheu Várias Populações"
         
             return config.pageIDs["WPMetapopulacao"]
  
        else:
            return 0