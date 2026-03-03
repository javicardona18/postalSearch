import os
from PySide6.QtWidgets import (QWidget,QLabel,QStackedWidget,QPushButton,QVBoxLayout,QSizePolicy,QFrame,QApplication)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette, QBrush, QPixmap, QFontDatabase, QFont

# -----------------------------
# Widget personalizado del Logo
# -----------------------------
class LogoWidget(QLabel):
    def __init__(self, pixmap):
        super().__init__()
        self.original_pixmap = pixmap
        self.setAlignment(Qt.AlignCenter)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def resizeEvent(self, event):
        if not self.original_pixmap.isNull():
            max_width = int(self.width() * 0.6)

            scaled = self.original_pixmap.scaled(
                max_width,
                max_width,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )

            self.setPixmap(scaled)

        super().resizeEvent(event)

# -----------------------------
# Paneles
# -----------------------------
class Panel(QFrame):
    def __init__(self, widget_inside):
        super().__init__()

        self.setObjectName("panel")

        # Tamaño fijo uniforme
        self.setFixedSize(180, 80)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(widget_inside, alignment=Qt.AlignCenter)

# -----------------------------
# Pantalla Menú
# -----------------------------
class Menu(QWidget):
    def __init__(self):
        super().__init__()

        ruta_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        logo_path = os.path.join(ruta_dir, "recursos", "imagenes", "logo.png")
        original_logo = QPixmap(logo_path)

        self.logo = LogoWidget(original_logo)

        self.btnbusqueda = QPushButton("Ir a Búsqueda")
        self.btnsalir = QPushButton("Abandonar")
        
        # Se meten los botones en paneles
        panel_busqueda = Panel(self.btnbusqueda)
        panel_salir = Panel(self.btnsalir)

        # Opcional: botones más elegantes
        self.btnbusqueda.setMaximumWidth(300)
        self.btnsalir.setMaximumWidth(300)

        # Layout principal
        layout_principal = QVBoxLayout()
        layout_principal.setContentsMargins(40, 40, 40, 40)
        layout_principal.setSpacing(30)
        layout_principal.addStretch()
        
        layout_principal.addWidget(self.logo)
        layout_principal.addStretch()

        layout_principal.addWidget(panel_busqueda, alignment=Qt.AlignCenter)
        layout_principal.addWidget(panel_salir, alignment=Qt.AlignCenter)
        layout_principal.addStretch()

        self.setLayout(layout_principal)


# -----------------------------
# Pantalla Búsqueda
# -----------------------------
class Busqueda(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.setContentsMargins(40, 40, 40, 40)

        titulo = QLabel("Pantalla de Búsqueda")
        titulo.setAlignment(Qt.AlignCenter)

        self.btn_back = QPushButton("Volver al menú")
        self.btn_back.setMaximumWidth(300)

        layout.addStretch()
        layout.addWidget(titulo)
        layout.addWidget(self.btn_back, alignment=Qt.AlignCenter)
        layout.addStretch()

        self.setLayout(layout)


# -----------------------------
# Ventana Principal
# -----------------------------
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        
        # --- Fuente personalizada ---
        font_path = os.path.join(base_dir, "recursos", "fuentes", "Banita.ttf")
        font_id = QFontDatabase.addApplicationFont(font_path)

        if font_id != -1:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            self.custom_font = QFont(font_family, 40)
        else:
            print("Error cargando la fuente")
            self.custom_font = QFont("Arial", 40)
        
        QApplication.instance().setFont(self.custom_font)
        
        self.setStyleSheet("""
        QFrame#panel {
            background-color: #0A4D8C;
            border-radius: 15px;
        }

        QPushButton {
            background-color: #0A4D8C;
            color: white;
            border: black;
            border-radius: 15px;
            padding: 20px;
            font-size: 23px;
        }

        QPushButton:hover {
            background-color: #1366B3;
        }

        QPushButton:pressed {
            background-color: #083A66;
        }
        """)
        
        background_path = os.path.join(ruta_dir, "recursos", "imagenes", "fondo.png")

        btn_layout.addWidget(btn_reporte)
        dashboard_layout.addLayout(btn_layout)

        # Crear pantallas
        self.pantalla_menu = Menu()
        self.pantalla_busqueda = Busqueda()

        # Añadir al stack
        self.stack.addWidget(self.pantalla_menu)
        self.stack.addWidget(self.pantalla_busqueda)
        self.stack.setCurrentWidget(self.pantalla_menu)

        # Conectar botones
        self.pantalla_menu.btnbusqueda.clicked.connect(self.ir_a_busqueda)
        self.pantalla_menu.btnsalir.clicked.connect(self.close)
        self.pantalla_busqueda.btn_back.clicked.connect(self.ir_a_menu)

        # --- Fondo ---
        background_path = os.path.join(base_dir, "recursos", "imagenes", "fondo.png")
        self.background = QPixmap(background_path)

        self.setWindowTitle("PostalSearch")
        self.showMaximized()

    def ir_a_busqueda(self):
        self.stack.setCurrentWidget(self.pantalla_busqueda)

    def ir_a_menu(self):
        self.stack.setCurrentWidget(self.pantalla_menu)

    def resizeEvent(self, event):
        if not self.background.isNull():
            scaled_bg = self.background.scaled(
                self.size(),
                Qt.IgnoreAspectRatio,
                Qt.SmoothTransformation
            )

            palette = QPalette()
            palette.setBrush(QPalette.Window, QBrush(scaled_bg))
            self.setAutoFillBackground(True)
            self.setPalette(palette)

        super().resizeEvent(event)