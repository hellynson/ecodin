#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from UI.frmMain_ui import Ui_MainWindow
from frmWizard import Wizard
from frmModelSetup import ModelSetup
from frmPlot import ModelsPlot
import config

class frmMain(QtGui.QMainWindow):
    def __init__(self, parent=None):
        ''' This is the "mother windows" of all windows of the Ecodin.
        Here, the other windows is called '''
        QtGui.QWidget.__init__(self, parent) 
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("EcoDin")

        QtCore.QObject.connect(self.ui.actionModelo,
                               QtCore.SIGNAL("triggered()"),
                               self.wizardOption)
                               
        QtCore.QObject.connect(self.ui.actionSair, 
                               QtCore.SIGNAL("triggered()"),
                               self.close)
                               
        QtCore.QObject.connect(self.ui.actionSobre_o_Software, 
                               QtCore.SIGNAL("triggered()"),
                               self.aboutSoftware)
                               
        QtCore.QObject.connect(self.ui.actionComo_usar, 
                               QtCore.SIGNAL("triggered()"),
                               self.howToUse)
                               
        QtCore.QObject.connect(self.ui.actionDados, 
                               QtCore.SIGNAL("triggered()"),
                               self.loadFile)
    def loadFile(self):
        config.modelo.clear()
        g = ModelsPlot(self.ui.mdiArea)
        g.onClickLoadFile()
        g.show()
                
        
    def notImplemented(self):
        ''' Method that displays a dialog box informing
        that isn't there implementation'''        
        # setup an information box
        infoBox = QtGui.QMessageBox(self)
        infoBox.setWindowTitle("EcoDin")
        infoBox.setIcon(infoBox.Information)
        infoBox.setText(u"Funcionalidade ainda não implementada")
        infoBox.setStandardButtons(infoBox.Ok)
        infoBox.setDefaultButton(infoBox.Ok)
        infoBox.exec_()
        
    def aboutSoftware(self):
               
        # setup an information box
        infoBox = QtGui.QMessageBox(self)
        infoBox.setWindowTitle("EcoDin")
        infoBox.setIcon(infoBox.Information)
        infoBox.setText(u"Ecodin 1.0.0\n" + "Created Scientific Programming Python"+
                        "\n2011 - 2012\n"+
                        u"\n\nDeveloped by Hellynson Cássio\n"+
                        "Undergraduate students in Interdisciplinary Science and Technology\n"+
                        "Federal University of Alfenas - Minas Gerais - Brazil"+
                        "\nhellynson@hotmail.com\nfacebook.com/hellynson\n"+
                        "\n\nProject bench by CNPq\n"+
                        "www.cnpq.br")
        infoBox.setStandardButtons(infoBox.Ok)
        infoBox.setDefaultButton(infoBox.Ok)
        infoBox.exec_()
        
    def howToUse(self):
              
        # setup an information box
        infoBox = QtGui.QMessageBox(self)
        infoBox.setWindowTitle("EcoDin - Como usar o Software?")
        infoBox.setIcon(infoBox.Information)
        infoBox.setText(u"Como usar...")
        infoBox.setStandardButtons(infoBox.Ok)
        infoBox.setDefaultButton(infoBox.Ok)
        infoBox.exec_()

    def runWizard(self):
        ''' Method that runs the wizard to choose a model '''
        wizard = Wizard(self)
        return wizard.exec_()
     
    def runModelSelectionDialog(self):
        '''Method that call the Window "modelSetup" 
        for the user can choose the model '''
        filha = ModelSetup(self)
        return filha.exec_()
        
    def plotModel(self):
        '''Method that creates the chart after the choice of model '''
        g = ModelsPlot(self.ui.mdiArea)
        g.show()

    def wizardOption(self):
        '''Method that allows the user to choose if wants or no to use the Model Choice Wizard  '''
        config.modelo.clear()
        # setup a question box
        questionBox = QtGui.QMessageBox(self)
        questionBox.setWindowTitle("EcoDin")
        questionBox.setIcon(questionBox.Question)
        questionBox.setText("Deseja usar o Assistente para criar um novo modelo?")
        questionBox.setStandardButtons(questionBox.Yes | questionBox.No | questionBox.Cancel)
        questionBox.setDefaultButton(questionBox.No)
        choice = questionBox.exec_()
        if choice == questionBox.Yes:
            result = self.runWizard()
            if result:
                # if the wizard wasn't cancelled, plot the model
                self.plotModel()
            else:
                #wizard was cancelled, do nothing
                return
        elif choice == questionBox.No:
            result = self.runModelSelectionDialog()
            if result:
                # if the Model Selection Dialog wasn't cancelled, plot the model
                self.plotModel()
            else:
                # Model Selection Dialog was cancelled, do nothing
                return
        else:
            # the user gives up from setting up a model, do nothing
            return
             
    
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName("EcoDin")
    MainWindow = frmMain()
    MainWindow.show()
    sys.exit(app.exec_())
        