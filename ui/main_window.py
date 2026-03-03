import os
from PySide6.QtWidgets import (QWidget,QLabel,QStackedWidget,QPushButton,QVBoxLayout,QSizePolicy,QFrame,QApplication,QHBoxLayout,QLineEdit,QTableWidget, QTableWidgetItem, QHeaderView)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette, QBrush, QPixmap, QFontDatabase, QFont, QColor

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
        
        self.background = QPixmap(logo_path.replace("logo.png", "fondo.png"))

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
        
        super(Menu, self).resizeEvent(event)


# -----------------------------
# Pantalla Búsqueda
# -----------------------------
class Busqueda(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setStyleSheet("background-color: #E3F2FD;")
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("#084169"))
        self.setPalette(palette)

        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # =======================
        # SIDEBAR
        # =======================
        sidebar = QFrame()
        sidebar.setFixedWidth(220)
        sidebar.setStyleSheet("""
            QFrame {
                background-color: #42A5F5;
            }
            QPushButton {
                color: white;
                background-color: transparent;
                border: none;
                padding: 15px;
                text-align: left;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #BBDEFB;
                color: #1E3A5F;
            }
        """)

        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setContentsMargins(0, 20, 0, 0)
        sidebar_layout.setSpacing(10)

        botones = ["Dashboard", "Clientes", "Reportes", "Configuración"]
        for texto in botones:
            btn = QPushButton(texto)
            sidebar_layout.addWidget(btn)

        sidebar_layout.addStretch()

        # =======================
        # CONTENIDO PRINCIPAL
        # =======================
        content = QFrame()
        content_layout = QVBoxLayout(content)
        content_layout.setContentsMargins(20, 20, 20, 20)
        content_layout.setSpacing(15)

        # =======================
        # HEADER
        # =======================
        header = QFrame()
        header.setStyleSheet("background-color: white; border-radius: 8px;")
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(15, 10, 15, 10)  

        search_bar = QLineEdit()
        search_bar.setPlaceholderText("Buscar pasajero...")
        search_bar.setFixedHeight(35)
        search_bar.setFont(QFont(self.font().family(), 14))
        search_bar.setStyleSheet("""
            QLineEdit {
                border: 2px solid #90CAF9;
                border-radius: 6px;
                padding-left: 10px;
                background-color: #F5F5F5;
            }
        """)

        user_label = QLabel("Usuario")
        user_label.setStyleSheet("color: #424242;")
        user_label.setFont(QFont(self.font().family(), 14))

        header_layout.addWidget(search_bar)
        header_layout.addStretch()
        header_layout.addWidget(user_label)
        

        # =======================
        # TABLA
        # =======================
        table_container = QFrame()
        table_container.setStyleSheet("background-color: white; border-radius: 8px;")
        table_layout = QVBoxLayout(table_container)
        table_layout.setContentsMargins(20, 20, 20, 20)

        table = QTableWidget()
        table.setColumnCount(4)
        table.setHorizontalHeaderLabels(["ID", "Nombre", "Apellido", "CI"])
        table.setRowCount(6)
        table.horizontalHeader().setStretchLastSection(True)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.setAlternatingRowColors(True)
        table.setShowGrid(False)
        table.setMinimumHeight(400)
        table.setFont(QFont(self.font().family(), 14))
        table.horizontalHeader().setFont(QFont(self.font().family(), 15))

        table.setStyleSheet("""
            QTableWidget {
                border: none;
                background-color: white;
                gridline-color: #E0E0E0;
            }
            QHeaderView::section {
                background-color: #64B5F6;
                color: white;
                padding: 8px;
                border: none;
            }
        """)

        table.verticalHeader().setVisible(False)
        table.setSelectionMode(QTableWidget.NoSelection)

        datos = [
            (1, "Juan", "Pérez", "12345678"),
            (2, "María", "Gómez", "87654321"),
            (3, "Carlos", "Rodríguez", "45678912"),
            (4, "Ana", "Martínez", "74125896"),
            (5, "Luis", "Fernández", "85236974"),
            (6, "Sofía", "López", "96385274"),
        ]

        for row, data in enumerate(datos):
            for col, value in enumerate(data):
                item = QTableWidgetItem(str(value))
                item.setFlags(Qt.ItemIsEnabled)
                table.setItem(row, col, item)

        table_layout.addWidget(table)

        # =======================
        # BOTÓN VOLVER
        # =======================
        self.btn_back = QPushButton("Volver al menú")
        self.btn_back.setFixedHeight(45)
        self.btn_back.setStyleSheet("""
            QPushButton {
                background-color: #42A5F5;
                color: white;
                border-radius: 8px;
                padding: 10px 20px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #1E88E5;
            }
        """)

        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        btn_layout.addWidget(self.btn_back)
        btn_layout.addStretch()

        # =======================
        # ENSAMBLADO FINAL
        # =======================
        content_layout.addWidget(header)
        content_layout.addWidget(table_container, 1)
        content_layout.addLayout(btn_layout)

        main_layout.addWidget(sidebar)
        main_layout.addWidget(content)


# -----------------------------
# Ventana Principal
# -----------------------------
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        # COLOR DE FONDO PRINCIPAL
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("#054A81"))
        self.setPalette(palette)

        ruta_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        
        # --- Fuente personalizada ---
        font_path = os.path.join(ruta_dir, "recursos", "fuentes", "Banita.ttf")
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

        self.setWindowTitle("PostalSearch")
        self.showMaximized()

    def ir_a_busqueda(self):
        self.stack.setCurrentWidget(self.pantalla_busqueda)

    def ir_a_menu(self):
        self.stack.setCurrentWidget(self.pantalla_menu)

