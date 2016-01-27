# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 13:29:19 2012

@author: Hellynson
"""

from PyQt4 import QtCore, QtGui
#from config import modelo
import config
from UI.wpEspeciesUi import Ui_WizardPageEspecies

class WPEspecies(QtGui.QWizardPage):
    def __init__(self, parent=None):
        '''Wizard page '''
        QtGui.QWidget.__init__(self, parent) 
        self.uiW = Ui_WizardPageEspecies()#construtor
        self.uiW.setupUi(self)
        
        QtCore.QObject.connect(self.uiW.rbUMAespecie, 
                             QtCore.SIGNAL("toggled(bool)"), 
                             self, QtCore.SIGNAL("completeChanged()"))

        QtCore.QObject.connect(self.uiW.rbNespecies,
                               QtCore.SIGNAL("toggled(bool)"), 
                                self, QtCore.SIGNAL("completeChanged()")) 
    def nextId(self):
        '''Method that goes to the next or previous window in the Wizard'''
        if self.uiW.rbUMAespecie.isChecked() == True: #checks if the radio button was clicked
       
             return config.pageIDs["WPPopulacoes"]#go to next page
         
        elif self.uiW.rbNespecies.isChecked() == True: 
        

             print u"Você escolheu N espécies"
         
             return config.pageIDs["WPPredacaoCompeticao"]
 
        else:
            return 0