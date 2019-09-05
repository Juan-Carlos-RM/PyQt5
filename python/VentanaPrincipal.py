# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 13:48:27 2019

@author: Juan Carlos RM
"""
from PyQt5         import QtCore
from PyQt5.QtCore  import pyqtSlot, pyqtSignal, QUrl
from PyQt5.QtQuick import QQuickView
import serial, time

class VentanaPrincipal(QQuickView):
    
    rpm = pyqtSignal(int)
    temperatura = pyqtSignal(int)
    presion = pyqtSignal(int)
    
    def __init__(self):
        super().__init__()
        self.setSource(QUrl("../qml/gui_fepro.qml"))
        self.rootContext().setContextProperty("VentanaPrincipal", self)
        self.setGeometry(150, 100, 1024, 480)
        self.setTitle("Sled-CAN v1.0")
        self.show()
        
        vista = self.rootObject()
        self.rpm.connect(vista.actualizarRpm)
        self.temperatura.connect(vista.actualizarTemperatura)
        self.presion.connect(vista.actualizarPresion)
        self.iniciarComunicacion('COM11')
        self.iniciaTemporizador()
        
        
    def __del__(self):
        pass
    
    
    def iniciarComunicacion(self, puerto):
        baudrate = 9600
        try:
            self.ser = serial.Serial(puerto, 
                                     baudrate, 
                                     timeout = 0, 
                                     parity = serial.PARITY_NONE, 
                                     stopbits = serial.STOPBITS_TWO, 
                                     bytesize = serial.EIGHTBITS)
            self.uart = 1
            
        except serial.SerialException:
            print("El puerto %s no está conectado" % puerto)
            self.uart = 0
                
    
    def iniciaTemporizador(self):
        self.temporizador = QtCore.QTimer()
        self.temporizador.timeout.connect(self.ciclo)
        self.temporizador.start(52)
    
        
    def ciclo(self):
        if self.uart == 1 :
            self.ser.write('p'.encode())
            datos = self.ser.read(15)
            print(datos)
            datossplit = datos.split(b'#')
            time.sleep(0.01)
            try:
                #
                datoRpm = datossplit[0]
                datoTmp = datossplit[1]
                datoPsn = datossplit[2]
                #print(datos)
                if datoRpm.strip():
                    self.rpm.emit(int(datoRpm))
                    self.temperatura.emit(int(datoTmp))
                    self.presion.emit(int(datoPsn))
                
            except:
                print("¡Error con el paso de datos!")
                
    
    @pyqtSlot('QString')
    def prenderLed(self, valor):
        if valor == 'L':
            self.ser.write('13L'.encode())
        if valor == 'H':
            self.ser.write('13H'.encode())
                  