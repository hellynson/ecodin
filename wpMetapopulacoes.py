# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 13:29:19 2012

@author: Hellynson
"""

from PyQt4 import QtCore, QtGui
#from config import modelo
import config
from UI.wpMetapopulacoesUi import Ui_WizardPageMetapopulacao

class WPMetapopulacao(QtGui.QWizardPage):
    def __init__(self, parent=None):
        
        QtGui.QWidget.__init__(self, parent) 
        self.uiW = Ui_WizardPageMetapopulacao()#construtor
        self.uiW.setupUi(self)
        
        QtCore.QObject.connect(self.uiW.rbMetapopulacao, 
                             QtCore.SIGNAL("toggled(bool)"), 
                             self, QtCore.SIGNAL("completeChanged()"))

    def nextId(self):
        if self.uiW.rbMetapopulacao.isChecked() == True: #verifica se o radio button foi clicado
         
         #config.modelo["qtd_pop"]="uma"
         
             return config.pageIDs["wp_sem_implementar"]#vai para pagina seguinte
        else:
            return 0