import os
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette, QBrush, QPixmap, QFontDatabase, QFont


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # --- Configuración de rutas ---
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        # Fuente personalizada
        font_path = os.path.join(base_dir, "recursos", "fuentes", "Banita.ttf")
        font_id = QFontDatabase.addApplicationFont(font_path)
        if font_id != -1:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            self.custom_font = QFont(font_family, 40)
        else:
            print("Error cargando la fuente")
            self.custom_font = QFont("Arial", 40)

        # Logo
        logo_path = os.path.join(base_dir, "recursos", "imagenes", "logo.png")
        self.original_logo = QPixmap(logo_path)
        self.logo_label = QLabel()
        self.logo_label.setPixmap(self.original_logo)
        self.logo_label.setAlignment(Qt.AlignCenter)

        # Fondo
        background_path = os.path.join(base_dir, "recursos", "imagenes", "fondo.png")
        self.background = QPixmap(background_path)

        # --- Layout principal ---
        layout = QVBoxLayout()
        layout.addWidget(self.logo_label)
        layout.setAlignment(self.logo_label, Qt.AlignTop | Qt.AlignHCenter)
        layout.setContentsMargins(0, 0, 0, 0)  # Opcional: sin márgenes
        self.setLayout(layout)

        self.setWindowTitle("PostalSearch")
        self.showMaximized()

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

        # Escalar logo proporcionalmente al ancho de la ventana
        nueva_escala = int(self.width() * 0.4)
        logo_escalado = self.original_logo.scaled(
            nueva_escala,
            nueva_escala,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.logo_label.setPixmap(logo_escalado)

        super().resizeEvent(event)