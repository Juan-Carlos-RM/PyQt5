# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 13:31:25 2019

@author: Juan Carlos RM
"""
from PyQt5.QtGui      import QIcon
from PyQt5.QtWidgets  import QApplication
from VentanaPrincipal import VentanaPrincipal
import sys
   

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("../img/buap.png"))
    v = VentanaPrincipal()
    sys.exit(app.exec_())