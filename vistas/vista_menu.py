import os
from PySide6.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout,
    QSizePolicy, QFrame
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette, QBrush, QPixmap


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


class Panel(QFrame):
    def __init__(self, widget_inside):
        super().__init__()
        self.setObjectName("panel")
        self.setFixedSize(180, 80)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(widget_inside, alignment=Qt.AlignCenter)


class VistaMenu(QWidget):
    def __init__(self):
        super().__init__()

        ruta_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        logo_path = os.path.join(ruta_dir, "recursos", "imagenes", "logo.png")

        original_logo = QPixmap(logo_path)
        self.background = QPixmap(logo_path.replace("logo.png", "fondo.png"))

        self.logo = LogoWidget(original_logo)

        self.btnbusqueda = QPushButton("Ir a Búsqueda")
        self.btnsalir = QPushButton("Abandonar")

        panel_busqueda = Panel(self.btnbusqueda)
        panel_salir = Panel(self.btnsalir)

        self.btnbusqueda.setMaximumWidth(300)
        self.btnsalir.setMaximumWidth(300)

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
