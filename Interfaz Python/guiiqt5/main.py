#hecho por gato
#dios ayudame

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5.QtGui import QColor
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
import time
import datetime
#from cuenta_regresiva_ui import Ui_MainWindow


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        loadUi('design.ui', self)
        
        self.bt_menu_1.clicked.connect(self.mover_menu)
        self.bt_menu_2.clicked.connect(self.mover_menu)
        
        #ocultar botones
        self.bt_restaurar.hide()
        self.bt_menu_2.hide()
        
        
        #sombra de los widgets
        self.sombra_frame(self.stackedWidget)
        self.sombra_frame(self.frame_superior)
        self.sombra_frame(self.bt_1)
        self.sombra_frame(self.bt_2)
        self.sombra_frame(self.bt_3)
        self.sombra_frame(self.bt_4)

        
        #control barra titulos
        self.bt_minimizar.clicked.connect(self.control_bt_minimizar)
        self.bt_restaurar.clicked.connect(self.control_bt_normal)
        self.bt_maximizar.clicked.connect(self.control_bt_maximizar)
        self.bt_cerrar.clicked.connect(lambda: self.close())
        
        #eliminar opcacidad titulo
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        
        #tamañogrip
        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)
        
        #mover ventana
        self.frame_superior.mouseMoveEvent = self.mover_ventana
        
        
        #acceder a las paginas
        self.bt_1.clicked.connect(self.pagina1)
        self.bt_2.clicked.connect(self.pagina2)
        self.bt_3.clicked.connect(self.pagina3)
        self.bt_4.clicked.connect(self.pagina4)
        self.bt_rutina1.clicked.connect(self.pagina_rutina1)
        self.bt_rutina2.clicked.connect(self.pagina_rutina2)
        self.bt_rutina3.clicked.connect(self.pagina_rutina3)
        self.bt_rutina4.clicked.connect(self.pagina_rutina4)
        self.bt_rutina5.clicked.connect(self.pagina_rutina5)
        
        #botones rutinas
        self.bt_aceptar_R1.clicked.connect(self.rutina1)
        self.bt_detener_R1.clicked.connect(self.detener_cuenta_regresiva_R1)
        self.bt_tiempo0.clicked.connect(self.detener_cuenta_regresiva_R1)
        self.bt_aceptar_R3.clicked.connect(self.rutina3)
        #copiar y pegar en el bueno
        self.bt_aceptar_r2.clicked.connect(self.rutina1)
        self.bt_aceptar_r4.clicked.connect(self.rutina1)
        self.bt_aceptar_r5.clicked.connect(self.rutina1)
        self.bt_aceptar_manual.clicked.connect(self.manual)
        #self.bt_detener_R3.clicked.connect(self.detener_cuenta_regresiva_R1)
        
        
        
        #timer
        self.tiempo_restante = 0
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.actualizar_cuenta_regresiva)
        
        
    def control_bt_minimizar(self):
        self.showMinimized()
    
    def control_bt_normal(self):
        self.showNormal()
        self.bt_restaurar.hide()
        self.bt_maximizar.show()
        
    def control_bt_maximizar(self):
        self.showMaximized()
        self.bt_maximizar.hide()
        self.bt_restaurar.show()
        
    #metodo sombra
    def sombra_frame(self, frame):
        sombra = QGraphicsDropShadowEffect(self)
        sombra.setBlurRadius(30)
        sombra.setXOffset(8)
        sombra.setYOffset(8)
        sombra.setColor(QColor(20, 200, 220, 255))
        frame.setGraphicsEffect(sombra)
        
    #sizegrip
    def resizeEvent(self, event):
        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)
        
    #mover ventana
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
        
    def mover_ventana (self, event):
        if self.isMaximized() == False:
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()
        if event.globalPos().y() <=10:
            self.showMaximized()
            self.bt_maximizar.hide()
            self.bt_restaurar.show()
        else:
            self.showNormal()
            self.bt_restaurar.hide()
            self.bt_maximizar.show()
            
    #menu lateral izquierdo mover
    def mover_menu(self):
        if True:
            width = self.menu_lateral.width()
            normal = 0
            if width == 0:
                extender = 300
                self.bt_menu_2.hide()
                self.bt_menu_1.show()
            else:
                self.bt_menu_1.hide()
                self.bt_menu_2.show()
                extender = normal
            self.animacion = QPropertyAnimation(self.menu_lateral, b"maximumWidth")
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setDuration(500)
            self.animacion.setEasingCurve(QEasingCurve.OutInBack)
            self.animacion.start()
            
    #animacion paginas
    def pagina1(self):
        self.stackedWidget_2.setCurrentWidget(self.page_uno)
        self.animacion_paginas()
    def pagina2(self):
        self.stackedWidget_2.setCurrentWidget(self.page_dos)
        self.animacion_paginas()
    def pagina3(self):
        self.stackedWidget_2.setCurrentWidget(self.page_tres)
        self.animacion_paginas()
    def pagina4(self):
        self.stackedWidget_2.setCurrentWidget(self.page_cuatro)
        self.animacion_paginas()
    #paginas rutinas
    def pagina_rutina1(self):
        self.stackedWidget.setCurrentWidget(self.page_rutina1)
        self.animacion_paginasru()
    def pagina_rutina2(self):
        self.stackedWidget.setCurrentWidget(self.page_rutina2)
        self.animacion_paginasru()
    def pagina_rutina3(self):
        self.stackedWidget.setCurrentWidget(self.page_rutina3)
        self.animacion_paginasru()
    def pagina_rutina4(self):
        self.stackedWidget.setCurrentWidget(self.page_rutina4)
        self.animacion_paginasru()
    def pagina_rutina5(self):
        self.stackedWidget.setCurrentWidget(self.page_rutina5)
        self.animacion_paginasru()
        
    #metodo animacion opaginas
    def animacion_paginas(self):
        if True:
            width = self.stackedWidget_2.width()
            x1 = self.frame_7.rect().right()
            normal = 100
            if width == 100:
                extender = x1
            else:
                extender = normal
            self.animacion1 = QPropertyAnimation(self.menu_lateral, b"maximumWidth")
            self.animacion1.setStartValue(width)
            self.animacion1.setEndValue(extender)
            self.animacion1.setDuration(500)
            self.animacion1.setEasingCurve(QEasingCurve.OutInQuad)
            self.animacion1.start()
            
    #metodo animacion opaginas rutinas
    def animacion_paginasru(self):
        if True:
            width = self.stackedWidget.width()
            x1 = self.frame_paginas.rect().right()
            normal = 100
            if width == 100:
                extender = x1
            else:
                extender = normal
            
            #self.animacion1 = QPropertyAnimation(self.menu_lateral, b"maximumWidth")
            #self.animacion1.setStartValue(width)
            #self.animacion1.setEndValue(extender)
            #self.animacion1.setDuration(500)
            #self.animacion1.setEasingCurve(QEasingCurve.OutInQuad)
            #self.animacion1.start()
    
    
    def rutina1(self):

        
        # Obtenemos el tiempo introducido por el usuario
        tiempo = self.txt_tiempo.text()
        if tiempo == "":
            QtWidgets.QMessageBox.warning(self, "Error", "Introduce un tiempo en minutos")
            return

        # Convertimos el tiempo a segundos
        # Convertimos el tiempo a segundos
        try:
            minutos, segundos = map(int, tiempo.split(":"))
            tiempo_total = minutos * 60 + segundos
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Error", "Introduce un tiempo válido (minutos:segundos)")
            return

        
        #colocar la funcion de movimiento aqui 
        #self.ejecutar_funcion(tiempo_total)
        
        

        # Iniciamos el temporizador
        self.tiempo_restante = tiempo_total
        self.timer.start(1000) # Actualizamos cada 1 segundo
        
        
    def rutina3(self):

        
        # Obtenemos el tiempo introducido por el usuario
        tiempo = self.chevront1.text()
        tiempo2 = self.chevront2.text()
        tiempo3 = self.chevront3.text()
        tiempo4 = self.chevront4.text()
        if tiempo == "":
            QtWidgets.QMessageBox.warning(self, "Error", "Introduce un tiempo en minutos")
            return

        # Convertimos el tiempo a segundos
        # Convertimos el tiempo a segundos
        try:
            minutos, segundos = map(int, tiempo.split(":"))
            tiempo_total = minutos * 60 + segundos
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Error", "Introduce un tiempo válido (minutos:segundos)")
            return

        
        #colocar la funcion de movimiento aqui 
        #self.ejecutar_funcion(tiempo_total)
        
        
        # Iniciamos el temporizador
        self.tiempo_restante = tiempo_total
        self.timer.start(1000) # Actualizamos cada 1 segundo
        
    def actualizar_cuenta_regresiva(self):
        # Actualizamos el tiempo restante
        self.tiempo_restante -= 1

        # Comprobamos si se ha terminado la cuenta regresiva
        if self.tiempo_restante <= 0:
            self.timer.stop()
            self.label_cuenta_regresiva.setText("¡Tiempo terminado!")
            QtWidgets.QMessageBox.information(self, "Tiempo completo", "El tiempo ha terminado")
            return

        # Convertimos el tiempo restante a formato minutos:segundos
        minutos = self.tiempo_restante // 60
        segundos = self.tiempo_restante % 60
        tiempo_formateado = f"{minutos:02d}:{segundos:02d}"
        
        # Actualizamos el label
        self.label_cuenta_regresiva.setText(tiempo_formateado)
        
        

            
    def detener_cuenta_regresiva_R1(self):
        self.timer.stop()
        self.tiempo_restante = 0
        self.label_cuenta_regresiva.setText("00:00")
        QtWidgets.QMessageBox.information(self, "Tiempo completo", "El tiempo ha terminado")
    #aqui seria lña funcoion de mover motor
    #def mover_motor(self)
        #codigo para mover el metor ciertos grados con su determinado tiempo
        #y en este colocar un sleep el cual sea lo que se demore la funcion del motor para asegurarse del movimiento del motor
        
    
    
    
    
    def manual(self):
        datos= self.datos_manual.text()
        tempmanual = self.tempmanual.text()
        ang = self.angulomanual.text()
        rpm_manual = self.rpm.text()
        tiempo_manual= self.tiempomanual.text()
        
        hora_actual = datetime.datetime.now()
        with open("datos.txt", "a") as archivo:
            # Escribir las variables en el archivo
            archivo.write(f"{hora_actual.strftime('%Y-%m-%d %H:%M:%S')}\n")
            archivo.write(f"datos: {datos}\n")
            archivo.write(f"Temperatura: {tempmanual}\n")
            archivo.write(f"Tiempo: {tiempo_manual}\n")
            archivo.write("-" * 20 + "\n")
        print("Datos guardados correctamente.")
        
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_app = VentanaPrincipal()
    mi_app.show()
    sys.exit(app.exec_())
    
    
        