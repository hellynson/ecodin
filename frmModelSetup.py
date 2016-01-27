# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 15:16:47 2012

@author: Hellynson
"""

from PyQt4 import QtCore, QtGui
from UI.frmModelSetupUi import Ui_JanelaModelo
#from UI.testeModelo_ui import testeUi_Dialog
import config

class ModelSetup(QtGui.QDialog):
    def __init__(self, parent=None):
        '''If the user to prefer to choose the model manually, this window will be called'''
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_JanelaModelo()

        self.ui.setupUi(self)
        #hiding the frames with the parameters Exp. and Logistic
        self.ui.fmExpContDet.setVisible(False)
        self.ui.fmLogistico.setVisible(False)
        # connect the selection of the model with the visibility of the frame
        self.connect(self.ui.cbModelList,
                     QtCore.SIGNAL("currentIndexChanged (int)"),
                        self.model_selected)
                        
                        #connect the buttons "Ok" and "Cancel"
        QtCore.QObject.connect(self.ui.pbOk,
                               QtCore.SIGNAL("clicked()"),
                                self.accept)
                                
        QtCore.QObject.connect(self.ui.pbCancel,
                               QtCore.SIGNAL("clicked()"),
                                self.reject)
                        
        
    def model_selected(self, index):
        '''This method analyzes the model selected by the user '''
        if index == 1:
            # Exponential model was selected, I do the frame visible
            self.ui.fmLogistico.setVisible(False)
            self.ui.fmExpContDet.setVisible(True)
            config.modelo["modeloEscolhido"] = "malthus"
        elif index == 2:
            # Logistic model was selected, I do the frame visible
            self.ui.fmExpContDet.setVisible(False)            
            self.ui.fmLogistico.setVisible(True)
            config.modelo["modeloEscolhido"] = "logistico"    
        elif index == 0:
            #None model was selected: I show the information window
            self.ui.fmExpContDet.setVisible(False)
            config.modelo["modeloEscolhido"] = None
            QtGui.QMessageBox.information(self,"Selecione o Modelo",
                                u"Por favor, selecione um modelo.")
        else:
            #hiding the frames with the parameters Exponential and Logistic
            self.ui.fmExpContDet.setVisible(False)
            self.ui.fmLogistico.setVisible(False)
            config.modelo["modeloEscolhido"] = None
            QtGui.QMessageBox.information(self,"Selecione o Modelo",
                                u"O modelo selecionado ainda não foi implementado")
    
         #analisando para ver se todos os campos estão preenchidos
    def accept(self):
        '''After the user clicked in "Ok", this method will analyze if all paraments are ok'''
        #if selected model is Exponential, grave in dictionary
        if config.modelo["modeloEscolhido"] == "malthus":
            try:
                config.modelo["populacaoInicial"]= float(self.ui.lineEditPopExp.text())
            except:
                QtGui.QMessageBox.information(self,"EcoDin",
                                u"Erro no valor da população inicial")
                self.ui.lineEdit_PopInicial.setFocus()
                return
            try:
                config.modelo["natalidade"]= float(self.ui.lineEditNatalidade.text())
            except:
                QtGui.QMessageBox.information(self,"EcoDin",
                                u"Erro no valor da natalidade")
                self.ui.lineEditNatalidade.setFocus()
                return
            try:
                config.modelo["mortalidade"]= float(self.ui.lineEditMortalidade.text())
            except:
                QtGui.QMessageBox.information(self,"EcoDin",
                u"Erro no valor da mortalidade")
                self.ui.lineEditMortalidade.setFocus()
                return
            try:
                config.modelo["tempo"]= float(self.ui.lineEditTempoExp.text())
            except:
                QtGui.QMessageBox.information(self,"EcoDin",
                u"Erro no valor do tempo")
                self.ui.lineEdit_Tempo.setFocus()
                return
            self.done(self.Accepted)
            
#          else if selected model is Logistic, grave in dictionary
        elif config.modelo["modeloEscolhido"] == "logistico":
            try:
                config.modelo["populacaoInicial"]= float(self.ui.lineEditPopLog.text())
            except:
                QtGui.QMessageBox.information(self,"EcoDin",
                                u"Erro no valor da população inicial")
                self.ui.lineEdit_PopInicial.setFocus()
                return
            try:
                config.modelo["taxaCrescimento"]= float(self.ui.lineEditCresc.text())
            except:
                QtGui.QMessageBox.information(self,"EcoDin",
                                u"Error no valor da taxa de crescimento (r)")
                self.ui.lineEditNatalidade.setFocus()
                return
            try:
                config.modelo["capacidadeSuporte"]= float(self.ui.lineEditCapSup.text())
            except:
                QtGui.QMessageBox.information(self,"EcoDin",
                u"Erro no valor da capacidade de Suporte (K)")
                self.ui.lineEditMortalidade.setFocus()
                return
            try:
                config.modelo["tempo"]= float(self.ui.lineEditTempoLog.text())
            except:
                QtGui.QMessageBox.information(self,"EcoDin",
                u"Erro no valor do tempo")
                self.ui.lineEdit_Tempo.setFocus()
                return
            self.done(self.Accepted)
                
               
        
     