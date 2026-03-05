from PySide6.QtWidgets import (
    QWidget, QFrame, QHBoxLayout, QVBoxLayout,
    QPushButton, QLabel, QLineEdit,
    QTableWidget, QTableWidgetItem, QHeaderView
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette, QColor, QFont


class VistaBusqueda(QWidget):
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