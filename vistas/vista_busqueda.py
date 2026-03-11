from PySide6.QtWidgets import (
    QWidget, QFrame, QHBoxLayout, QVBoxLayout,
    QPushButton, QLabel, QLineEdit,
    QTableWidget, QTableWidgetItem, QHeaderView, QMenu
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette, QColor, QFont, QAction


class VistaBusqueda(QWidget):
    def __init__(self):
        super().__init__()
        
        print("VistaBusqueda cargada")

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
        # CONTENIDO
        # =======================
        content = QFrame()
        content_layout = QVBoxLayout(content)
        content_layout.setContentsMargins(20, 20, 20, 20)
        content_layout.setSpacing(15)

        # HEADER
        header = QFrame()
        header.setStyleSheet("background-color: white; border-radius: 8px;")

        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(15, 10, 15, 10)

        # =========================
        # CREAR WIDGETS
        # =========================

        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Buscar pasajero...")
        self.search_bar.setFixedHeight(35)
        self.search_bar.setFont(QFont(self.font().family(), 14))
        self.search_bar.setStyleSheet("""
            QLineEdit {
                border: 2px solid #90CAF9;
                border-radius: 6px;
                padding-left: 10px;
                background-color: #F5F5F5;
            }
        """)
        
        #Declaracion de boton buscar
        self.btn_buscar = QPushButton("Buscar")
        self.btn_buscar.setFixedSize(110, 35)
        
        #Declaracion de boton Filtros
        self.btn_filtros = QPushButton("Filtros")
        self.btn_filtros.setFixedSize(120, 35)
        
        #Panel que se abre al clickear filtros
        self.menu_filtros = QMenu()
        
        #Estilo del menu de Filtros
        self.menu_filtros.setStyleSheet("""
            QMenu {
                background-color: white;
                border: 1px solid #B0BEC5;
                padding: 5px;
                font-size: 15px;
            }

            QMenu::item {
                padding: 6px 20px;
            }

            QMenu::item:selected {
                background-color: #42A5F5;
                color: white;
            }
            """)
        self.menu_filtros.setFixedWidth(self.btn_filtros.width())
        
        #Opciones de filtro
        self.filtro_nombre = QAction("Nombre", self)
        self.filtro_apellido = QAction("Apellido", self)
        self.filtro_ci = QAction("CI", self)
        self.filtro_correo = QAction("Correo", self)
        self.filtro_telefono = QAction("Teléfono", self)

        self.menu_filtros.addAction(self.filtro_nombre)
        self.menu_filtros.addAction(self.filtro_apellido)
        self.menu_filtros.addAction(self.filtro_ci)
        self.menu_filtros.addAction(self.filtro_correo)
        self.menu_filtros.addAction(self.filtro_telefono)
        
        self.btn_filtros.setMenu(self.menu_filtros)
        self.filtro_activo = "nombre"
        
        self.filtro_nombre.triggered.connect(lambda: self.cambiar_filtro("nombre"))
        self.filtro_apellido.triggered.connect(lambda: self.cambiar_filtro("apellido"))
        self.filtro_ci.triggered.connect(lambda: self.cambiar_filtro("ci"))
        self.filtro_correo.triggered.connect(lambda: self.cambiar_filtro("correo"))
        self.filtro_telefono.triggered.connect(lambda: self.cambiar_filtro("telefono"))

        # BOTÓN BUSCAR DISEÑO
        self.btn_buscar.setStyleSheet("""
        QPushButton {
            background-color: #42A5F5;
            color: white;
            border-radius: 6px;
            font-size: 14px;
            font-weight: bold;
            padding: 5px;
        }
        QPushButton:hover {
            background-color: #1E88E5;
        }
        """)

        # BOTÓN FILTROS DISEÑO
        self.btn_filtros.setStyleSheet("""
        QPushButton {
            background-color: #42A5F5;
            color: white;
            border-radius: 6px;
            font-size: 14px;
            font-weight: bold;
            padding: 5px;
        }
        QPushButton:hover {
            background-color: #64B5F6;
        }
        """)
        user_label = QLabel("Usuario")
        user_label.setStyleSheet("color: #424242;")
        user_label.setFont(QFont(self.font().family(), 14))

        # =========================
        # CREAR LAYOUTS
        # =========================

        search_container = QVBoxLayout()

        fila_busqueda = QHBoxLayout()
        fila_busqueda.addWidget(self.search_bar)
        fila_busqueda.addWidget(self.btn_buscar)

        search_container.addLayout(fila_busqueda)
        search_container.addWidget(self.btn_filtros)

        # =========================
        # AGREGAR AL HEADER
        # =========================

        header_layout.addLayout(search_container)
        header_layout.addStretch()

        header_layout.addWidget(user_label)
        
        # TABLA
        table_container = QFrame()
        table_container.setStyleSheet("background-color: white; border-radius: 8px;")

        table_layout = QVBoxLayout(table_container)
        table_layout.setContentsMargins(20, 20, 20, 20)

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(
            ["Nombre", "Apellido", "CI", "Correo Electrónico", "Teléfono"]
        )

        self.table.setRowCount(0)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setAlternatingRowColors(True)
        self.table.setShowGrid(False)
        self.table.setMinimumHeight(400)
        self.table.setFont(QFont(self.font().family(), 14))
        self.table.horizontalHeader().setFont(QFont(self.font().family(), 15))

        self.table.setStyleSheet("""
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

        self.table.verticalHeader().setVisible(False)
        self.table.setSelectionMode(QTableWidget.NoSelection)

        table_layout.addWidget(self.table)

        # BOTÓN VOLVER
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

        content_layout.addWidget(header)
        content_layout.addWidget(table_container, 1)
        content_layout.addLayout(btn_layout)

        main_layout.addWidget(sidebar)
        main_layout.addWidget(content)
    
    def cargar_pasajeros_en_tabla(self, pasajeros):

        self.table.setRowCount(len(pasajeros))

        for row, pasajero in enumerate(pasajeros):

            self.table.setItem(row, 0, QTableWidgetItem(pasajero["nombre"]))
            self.table.setItem(row, 1, QTableWidgetItem(pasajero["apellido"]))
            self.table.setItem(row, 2, QTableWidgetItem(pasajero["ci"]))
            self.table.setItem(row, 3, QTableWidgetItem(pasajero["correo"]))
            self.table.setItem(row, 4, QTableWidgetItem(pasajero["telefono"]))

# Que cambie el nombre del boton filtros segun lo seleccionado
    def cambiar_filtro(self, filtro):

        self.filtro_activo = filtro
        
        nombres = {
        "nombre": "Por Nombre",
        "apellido": "Por Apellido",
        "ci": "Por CI",
        "correo": "Por Correo",
        "telefono": "Por Teléfono"
        }

        self.btn_filtros.setText(nombres[filtro])