import os
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QStackedWidget,
    QPushButton,
    QVBoxLayout,
    QSizePolicy,
)
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
        self.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )

    def resizeEvent(self, event):
        if not self.original_pixmap.isNull():
            max_width = int(self.width() * 0.8)

            scaled = self.original_pixmap.scaled(
                max_width,
                max_width,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )

            self.setPixmap(scaled)

        super().resizeEvent(event)


# -----------------------------
# Pantalla Menú
# -----------------------------
class Menu(QWidget):
    def __init__(self):
        super().__init__()

        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        logo_path = os.path.join(base_dir, "recursos", "imagenes", "logo.png")
        original_logo = QPixmap(logo_path)

        self.logo = LogoWidget(original_logo)

        self.btnbusqueda = QPushButton("Ir a Búsqueda")
        self.btnsalir = QPushButton("Salir")

        # Opcional: botones más elegantes
        self.btnbusqueda.setMaximumWidth(300)
        self.btnsalir.setMaximumWidth(300)

        # Layout principal
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(40, 40, 40, 40)
        main_layout.setSpacing(20)

        main_layout.addStretch()
        main_layout.addWidget(self.logo)
        main_layout.addStretch()
        main_layout.addWidget(self.btnbusqueda, alignment=Qt.AlignCenter)
        main_layout.addWidget(self.btnsalir, alignment=Qt.AlignCenter)
        main_layout.addStretch()

        self.setLayout(main_layout)


# -----------------------------
# Pantalla Búsqueda
# -----------------------------
class Busqueda(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.setContentsMargins(40, 40, 40, 40)

        title = QLabel("Pantalla de Búsqueda")
        title.setAlignment(Qt.AlignCenter)

        self.btn_back = QPushButton("Volver al menú")
        self.btn_back.setMaximumWidth(300)

        layout.addStretch()
        layout.addWidget(title)
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

        # --- Stack de pantallas ---
        self.stack = QStackedWidget()
        layout = QVBoxLayout(self)
        layout.addWidget(self.stack)

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

        # --- Fuente personalizada ---
        font_path = os.path.join(base_dir, "recursos", "fuentes", "Banita.ttf")
        font_id = QFontDatabase.addApplicationFont(font_path)

        if font_id != -1:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            self.custom_font = QFont(font_family, 40)
        else:
            print("Error cargando la fuente")
            self.custom_font = QFont("Arial", 40)

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