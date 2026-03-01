import sys
import os
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QStackedWidget, QPushButton, QVBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette, QBrush, QPixmap, QFontDatabase, QFont

class LogoWidget(QLabel):
    def __init__(self, pixmap):
        super().__init__()
        self.original_pixmap = pixmap
        self.setAlignment(Qt.AlignCenter)

    def resizeEvent(self, event):
        if not self.original_pixmap.isNull():

            # 👇 El logo será máximo el 40% del ancho de su contenedor
            max_width = int(self.parent().width() * 0.4)

            scaled = self.original_pixmap.scaled(
                max_width,
                max_width,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )

            self.setPixmap(scaled)

        super().resizeEvent(event)

#Se crea la ventana del Menu
class Menu(QWidget):
    def __init__(self):
        super().__init__()
        
        #Ruta del programa
        base_dir = os.path.dirname(os.path.abspath(__file__))

        #Se carga el logo.
        logo_path = os.path.join(base_dir, "Resources", "imagenes", "logo.png")
        
        logo_pixmap = QPixmap(logo_path)
        
        layout = QVBoxLayout(self)
        
        self.logo_label = LogoWidget(logo_pixmap)

        title = QLabel("")
        title.setAlignment(Qt.AlignCenter)

        self.btnbusqueda = QPushButton("Ir a Búsqueda")
        self.btnsalir = QPushButton("Salir")

        layout.addWidget(title)
        layout.addWidget(self.logo_label, stretch=3)
        layout.addWidget(self.btnbusqueda, stretch=1)
        layout.addWidget(self.btnsalir, stretch=1)

#Se crea la ventana de busqueda
class Busqueda(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("")
        title.setAlignment(Qt.AlignCenter)

        self.btn_back = QPushButton("Volver al menú")

        layout.addWidget(title)
        layout.addWidget(self.btn_back)

#Ventana principal del programa, es el controlador de las demas ventanas.
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        #Ruta base del proyecto
        base_dir = os.path.dirname(os.path.abspath(__file__))
        
        #Se define el stack que sera el gestor de las pantallas, si es 0 Menu, si es 1 Busqueda, por ejemplo.
        self.stack = QStackedWidget(self)
        layout = QVBoxLayout(self)
        layout.addWidget(self.stack)
        
        #Se crean las instancias de las pantallas
        self.pantalla_menu = Menu()
        self.pantalla_busqueda = Busqueda()
        
        #Se guardan las pantallas en el stack
        self.stack.addWidget(self.pantalla_menu)    #índice 0
        self.stack.addWidget(self.pantalla_busqueda)  #índice 1
        self.stack.setCurrentWidget(self.pantalla_menu) #Establece el menu como pantalla actual
        
        #Conectar botones declarados en las pantallas
        self.pantalla_menu.btnbusqueda.clicked.connect(self.ir_a_busqueda)
        self.pantalla_menu.btnsalir.clicked.connect(self.close)
        self.pantalla_busqueda.btn_back.clicked.connect(self.ir_a_menu)

        #Se carga la fuente
        font_path = os.path.join(base_dir, "Resources", "Fuentes", "Banita.ttf")
        font_id = QFontDatabase.addApplicationFont(font_path)
        
        #Si se encuentra la fuente, font_id es un id si no devuelve -1 y no se cumple el if.
        if font_id != -1:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            self.custom_font = QFont(font_family, 40)
        else:
            print("Error cargando la fuente")
            self.custom_font = QFont("Arial", 40)

        #Se carga el fondo.
        background_path = os.path.join(base_dir, "Resources", "imagenes", "fondo.png")
        self.background = QPixmap(background_path)
        
        #Detalles de la ventana.
        self.setWindowTitle("PostalSearch")
        self.showMaximized()    

    def resizeEvent(self, event):
        #Escalando el fondo al tamaño de la ventana.
        scaled = self.background.scaled( self.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(scaled))
        self.setPalette(palette)
        
        super().resizeEvent(event)
    
    def ir_a_busqueda(self):
        self.stack.setCurrentWidget(self.pantalla_busqueda)

    def ir_a_menu(self):
        self.stack.setCurrentWidget(self.pantalla_menu)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()