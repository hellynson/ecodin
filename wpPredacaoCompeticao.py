# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 13:29:19 2012

@author: Hellynson
"""

from PyQt4 import QtCore, QtGui
#from config import modelo
import config
from UI.wpPredacaoCompeticaoUi import Ui_WizardPagePredacaoCompeticao

class WPPredacaoCompeticao(QtGui.QWizardPage):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.uiW = Ui_WizardPagePredacaoCompeticao()#construtor
        self.uiW.setupUi(self)
        
        QtCore.QObject.connect(self.uiW.rbPredacao, 
                             QtCore.SIGNAL("toggled(bool)"), 
                             self, QtCore.SIGNAL("completeChanged()"))

        QtCore.QObject.connect(self.uiW.rbCompeticao,
                               QtCore.SIGNAL("toggled(bool)"), 
                                self, QtCore.SIGNAL("completeChanged()")) 

    def nextId(self):
        if self.uiW.rbPredacao.isChecked() == True: #verifica se o radio button foi clicado
         
         #config.modelo["qtd_pop"]="uma"
         
             return config.pageIDs["wp_sem_implementar"]#vai para pagina seguinte
         
        elif self.uiW.rbCompeticao.isChecked() == True: 
        
         #config.modelo["qtd_pop"]="varias"
     
         
             return config.pageIDs["wp_sem_implementar"]
#         from naoImplementado import janelaNaoImplementada
#         bugado = janelaNaoImplementada(self)
#         bugado.show()   
        else:
            return 0