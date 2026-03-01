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

            # El logo será máximo el 40% del ancho de su contenedor
            max_width = int(self.parent().width() * 0.4)

            scaled = self.original_pixmap.scaled(
                max_width,
                max_width,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )

            self.setPixmap(scaled)

        super().resizeEvent(event)

class Menu(QWidget):
    def __init__(self):
        super().__init__()
        
         # --- Configuración de rutas ---
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        # Logo
        logo_path = os.path.join(base_dir, "recursos", "imagenes", "logo.png")
        self.original_logo = QPixmap(logo_path)
        self.logo_label = QLabel()
        self.logo_label.setPixmap(self.original_logo)
        self.logo_label.setAlignment(Qt.AlignHCenter)

        # --- Layout principal ---
        layout = QVBoxLayout()
        layout.addWidget(self.logo_label)
        layout.setAlignment(self.logo_label, Qt.AlignTop | Qt.AlignLeft)
        layout.setContentsMargins(50, 50, 0, 0)  # Opcional: sin márgenes
        self.setLayout(layout)
        
        title = QLabel("")
        title.setAlignment(Qt.AlignCenter)

        self.btnbusqueda = QPushButton("Ir a Búsqueda")
        self.btnsalir = QPushButton("Salir")

        layout.addWidget(title)
        layout.addWidget(self.btnbusqueda)
        layout.addWidget(self.btnsalir)
        

class Busqueda(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        title = QLabel("")
        title.setAlignment(Qt.AlignHCenter)

        self.btn_back = QPushButton("Volver al menú")

        layout.addWidget(title)
        layout.addWidget(self.btn_back)
        
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # --- Configuración de rutas ---
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
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

        # Fuente personalizada
        font_path = os.path.join(base_dir, "recursos", "fuentes", "Banita.ttf")
        font_id = QFontDatabase.addApplicationFont(font_path)
        if font_id != -1:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            self.custom_font = QFont(font_family, 40)
        else:
            print("Error cargando la fuente")
            self.custom_font = QFont("Arial", 40)

        # Fondo
        background_path = os.path.join(base_dir, "recursos", "imagenes", "fondo.png")
        self.background = QPixmap(background_path)

        self.setWindowTitle("PostalSearch")
        self.showMaximized()
    
    def ir_a_busqueda(self):
        self.stack.setCurrentWidget(self.pantalla_busqueda)

    def ir_a_menu(self):
        self.stack.setCurrentWidget(self.pantalla_menu)

    def resizeEvent(self, event):
        # Escalar fondo
        scaled_bg = self.background.scaled(
            self.size(),
            Qt.IgnoreAspectRatio,
            Qt.SmoothTransformation
        )
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(scaled_bg))
        self.setPalette(palette)

        super().resizeEvent(event)