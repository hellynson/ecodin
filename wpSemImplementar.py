# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 20:08:21 2012

@author: eaguilar
"""

from PyQt4 import QtGui
from UI.wpSemImplementarUi import Ui_wpSemImplementar

class WP_sem_implementar(QtGui.QWizardPage):
    '''Class that creates a Information Window'''
    def __init__(self, parent=None):
        # crio a ui da página
        QtGui.QWidget.__init__(self, parent) 
        self.ui = Ui_wpSemImplementar()
        self.ui.setupUi(self)

    def isComplete(self):
        '''Method that rehabilitates or no the button Ok'''
        return False