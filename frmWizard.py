# -*- coding: utf-8 -*-
"""
Created on Sun Feb 05 01:32:57 2012

@author: Hellynson
"""

from PyQt4 import QtCore, QtGui
from UI.frmWizardUi import Ui_Wizard
import config
#from config import modelo
from wpEspecies import WPEspecies
from wpPopulacoes import WPPopulacoes # certo!
from wpPredacaoCompeticao import WPPredacaoCompeticao
from wpDensidade import WPDensidade_dependente_independente
from wpMetapopulacoes import WPMetapopulacao
from wpEstacionalidade import WPContinuoDiscreto
from wpSemImplementar import WP_sem_implementar
from wpExponencialContinuo import WPExponencial
from wpLogistico import WPLogistico

class Wizard(QtGui.QWizard):
    '''Class that creates a wizard to help users choose the best model'''
    def __init__(self, parent=None):
        
        QtGui.QWidget.__init__(self, parent) 
        self.uiW = Ui_Wizard()#construtor
        self.uiW.setupUi(self)
        self.setWindowTitle("EcoDin")
        
        # crio as páginas
        self.pageNames = {"WPEspecies":1,
                          "WPPopulacoes":2,
                          "WPPredacaoCompeticao":3,
                          "WPDensidade_dependente_independente":4,
                          "WPMetapopulacao":5,
                          "WPContinuoDiscreto":6,
                          "WP_sem_implementar":7,
                          "WPExponencial":8,
                          "WPLogistico":9
                          }
        
        self.WPEspecies = WPEspecies()
        self.WPPopulacoes = WPPopulacoes()
        self.WPPredacaoCompeticao = WPPredacaoCompeticao() 
        self.WPDensidade_dependente_independente = WPDensidade_dependente_independente()
        self.WPMetapopulacao = WPMetapopulacao()
        self.WPContinuoDiscreto = WPContinuoDiscreto()
        self.WP_sem_implementar = WP_sem_implementar()
        self.WPExponencial= WPExponencial()
        self.WPLogistico= WPLogistico()
        ### Assigning numerical indices to the windows of the wizard ###
        self.setPage(config.pageIDs["WPEspecies"], self.WPEspecies)#atribui indices numericos às janelas do wizard para que o nextId possa retorná-los e chamar as demais paginas
        self.setPage(config.pageIDs["WPPopulacoes"], self.WPPopulacoes)
        self.setPage(config.pageIDs["WPPredacaoCompeticao"], self.WPPredacaoCompeticao)
        self.setPage(config.pageIDs["WPDensidade_dependente_independente"], self.WPDensidade_dependente_independente)
        self.setPage(config.pageIDs["WPMetapopulacao"], self.WPMetapopulacao)        
        self.setPage(config.pageIDs["WPContinuoDiscreto"], self.WPContinuoDiscreto)        
        self.setPage(config.pageIDs["wp_sem_implementar"], self.WP_sem_implementar)
        self.setPage(config.pageIDs["WPExponencial"], self.WPExponencial)
        self.setPage(config.pageIDs["WPLogistico"], self.WPLogistico)
        # Connecting the Help button of the Wizard #
        self.connect(self, QtCore.SIGNAL("helpRequested()"), self.ajuda);

    def notImplemented(self):
        ''' Method that displays a dialog box informing informing that isn't there implementation'''   
        # setup an information box
        infoBox = QtGui.QMessageBox(self)
        infoBox.setWindowTitle("EcoDin")
        infoBox.setIcon(infoBox.Information)
        infoBox.setText(u"Funcionalidade ainda não implementada")
        infoBox.setStandardButtons(infoBox.Ok)
        infoBox.setDefaultButton(infoBox.Ok)
        infoBox.exec_()
        
    def ajuda(self):
        '''Method that shows a Help Window for user'''
        if self.currentId() == 0:
            self.notImplemented()
        elif self.currentId() == 1:
            self.notImplemented()
        elif self.currentId() == 2:
            self.notImplemented()
        elif self.currentId() == 3:
            self.notImplemented()
        elif self.currentId() == 4:
            self.notImplemented()
        else:
            self.notImplemented()
