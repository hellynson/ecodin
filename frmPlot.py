# -*- coding: utf-8 -*-
"""
Created on Fri May 04 17:16:08 2012

@author: Hellynson
"""
# Python Qt4 bindings for GUI objects
from PyQt4 import QtGui, QtCore
# Numpy functions for image creation
import numpy as np
# Matplotlib Figure object
from matplotlib.figure import Figure
# import the Qt4Agg FigureCanvas object, that binds Figure to
# Qt4Agg backend. It also inherits from QWidget
from matplotlib.backends.backend_qt4agg\
import FigureCanvasQTAgg as FigureCanvas
# import the NavigationToolbar Qt4Agg widget
from matplotlib.backends.backend_qt4agg\
import NavigationToolbar2QTAgg as NavigationToolbar
# configuration module
import config
import csv
from frmModelSetup import ModelSetup



class Qt4MplCanvas(FigureCanvas):
    """Class to represent the FigureCanvas widget"""
    def __init__(self, parent):
        # plot definition
        self.fig = Figure()
        self.axes = self.fig.add_subplot(111)
        # initialization of the canvas
        FigureCanvas.__init__(self, self.fig)
        # set the parent widget
        self.setParent(parent)
        # we define the widget as expandable
        FigureCanvas.setSizePolicy(self,
            QtGui.QSizePolicy.Expanding,
            QtGui.QSizePolicy.Expanding)
        # notify the system of updated policy
        FigureCanvas.updateGeometry(self)
        
class ModelsPlot(QtGui.QMdiSubWindow):
    '''It creates the plot window '''
    def __init__(self, parent=None):
        # call to base class constructor
        QtGui.QMdiSubWindow.__init__(self, parent)
        # setup window's title
        self.setWindowTitle("EcoDin")
        # instantiate a widget, it will be the main one
        self.main_widget = QtGui.QWidget(self)
        self.setWidget(self.main_widget)
        # create a vertical box layout widget
        self.vbl = QtGui.QVBoxLayout(self.main_widget)
        # instantiate our Matplotlib canvas widget
        self.qmc = Qt4MplCanvas(self.main_widget)
        # instantiate the navigation toolbar
        self.ntb = NavigationToolbar(self.qmc, self.main_widget)
        # pack these widget into the vertical box
        self.vbl.addWidget(self.ntb)
        self.vbl.addWidget(self.qmc)
        # set the focus on the main widget
        self.main_widget.setFocus()
        # plot model
        self.plot()
        
        

         #Prerequisite to display the right mouse button
        self.qmc.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
 
        #creates the menu object with the right mouse button 
        self.BtMenu = QtGui.QMenu()
        self.onButtonMenu()
        
        
        #Connect the signal from the right mouse button       
        self.connect(self.qmc,
                     QtCore.SIGNAL('customContextMenuRequested(const QPoint&)'), 
                        self.onClickButtonMenu)
 
  
    def onClickLoadFile(self):
        '''Method that gets CSV files of the user and creates chart with the datas'''
        print "testando o upload do arquivo"
        self.endereco = QtGui.QFileDialog.getOpenFileName()#Open a window for to get files
#        spamReader = csv.reader(endereco, delimiter='', quotechar='|')
             
        if self.endereco != "": 
            
            lista=[]
          
            lista = csv.reader(open(self.endereco), delimiter=';')
            
            self.x = []
            self.y = []
            for linha in lista:
                self.x.append(float(linha[0]))
                self.y.append(float(linha[1]))
           
            print 'x= ', self.x
            print 'y= ', self.y
            
            
            self.legenda = unicode(self.endereco.split("/")[-1])#pega apenas o último nome (o nome do arquivo)
            self.qmc.axes.plot(self.x, self.y, "o", label=self.legenda)
            self.qmc.axes.legend()
            
            self.qmc.draw()
        else:
            QtGui.QMessageBox.information(self, u"Arquivo não selecionado - EcoDin", 
                                      u"Nenhum arquivo foi selecionado")  
                                      
    def onClickHelp(self):
        '''Method that shows a Help Window'''
        #mensagem de ajuda para quando usuário clicar com o botão direito 
        msg1 = u"Você pode carregar novos dados de um arquivo .CSV para gerar outro gráfico dentro desta janela."
        msg2 = u" Ou pode também selecionar outro modelo e gerar novamente outro gráfico."        
        QtGui.QMessageBox.information(self, "Ajuda", msg1+msg2)

    def onClickOtherModel(self):
        '''Method that calls the Model Choice  Window, for manual choice of the model'''
        filha = ModelSetup(self)
        result = filha.exec_()
        if result:
                # if the Model Selection Dialog wasn't cancelled, plot the mode
                self.plot()
        else:
                # Model Selection Dialog was cancelled, do nothing
                return
                
        
    def onButtonMenu(self):        
        #Create each item and associated with slot
        self.BtMenu.addAction("Carregar dados",self.onClickLoadFile)
        self.BtMenu.addAction("Inserir outro modelo", self.onClickOtherModel)
        self.BtMenu.addSeparator() #cria um separador entre as opções do menu
        self.BtMenu.addAction("Ajuda",self.onClickHelp)        
        
        #Enables or disables the menu          
        self.BtMenu.setEnabled(True)
 
       

    def onClickButtonMenu(self, point):
        '''Runs right button menu'''
        self.BtMenu.exec_(self.qmc.mapToGlobal(point))
        
        
    def plot(self):
        ''' Create the chart according with the selected model'''
        if config.modelo.has_key("modeloEscolhido"):
     
             if config.modelo["modeloEscolhido"] == "malthus":
                #Gets Dictionary's data and creates the chart
                self.deltaT = config.modelo["tempo"]
                self.b = config.modelo["natalidade"]
                self.d =  config.modelo["mortalidade"]
                self.N0 = config.modelo["populacaoInicial"]
                self.alfa = self.b - self.d
                self.x = np.arange(0.0, self.deltaT, 1.0)
                self.y = self.N0 * np.exp(self.alfa * self.x)
                self.qmc.axes.set_xlabel("Tempo")
                self.qmc.axes.set_ylabel(u"População")
                self.etiqueta = "Exp b="+str(self.b)+" "+"d="+str(self.d)
                self.qmc.axes.plot(self.x, self.y, label=self.etiqueta)
                self.qmc.axes.legend()
            
             elif config.modelo["modeloEscolhido"] == "logistico":
                #Gets Dictionary's data and creates the chart
                self.deltaT = config.modelo["tempo"]
                self.r = config.modelo["taxaCrescimento"]
                self.k =  config.modelo["capacidadeSuporte"]
                self.N0 = config.modelo["populacaoInicial"]
                self.x = np.arange(0.0, self.deltaT, 1.0)
                self.y = self.k/(1 + ( (self.k / self.N0 - 1) * np.exp( -self.r * self.x) ))
                self.qmc.axes.set_xlabel("Tempo")
                self.qmc.axes.set_ylabel(u"População")
                self.etiqueta = "Log r="+str(self.r)+" "+"K="+str(self.k)
                self.qmc.axes.plot(self.x, self.y, label=self.etiqueta)
                self.qmc.axes.legend()
                
             else:
                QtGui.QMessageBox.critical(self.parent(),
                                    "EcoDin",
                                    u"Erro na seleção do modelo")

        self.qmc.draw()
            
        