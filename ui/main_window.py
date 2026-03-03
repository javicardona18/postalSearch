import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QLineEdit, QTableWidget, QTableWidgetItem,
    QFrame, QSizePolicy
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PostalSearch")
        self.resize(1200, 700)

        # Widget principal
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        central_widget.setLayout(main_layout)

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
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #BBDEFB;
                color: #1E3A5F;
            }
        """)

        sidebar_layout = QVBoxLayout()
        sidebar_layout.setContentsMargins(0, 20, 0, 0)
        sidebar_layout.setSpacing(10)

        botones = ["Dashboard", "Clientes", "Reportes", "Configuración"]
        for texto in botones:
            btn = QPushButton(texto)
            sidebar_layout.addWidget(btn)

        sidebar_layout.addStretch()
        sidebar.setLayout(sidebar_layout)

        # =======================
        # ÁREA PRINCIPAL
        # =======================
        content = QFrame()
        content.setStyleSheet("background-color: #E3F2FD;")
        content_layout = QVBoxLayout()
        content_layout.setContentsMargins(20, 20, 20, 20)
        content_layout.setSpacing(15)
        content.setLayout(content_layout)

        # =======================
        # HEADER
        # =======================
        header = QFrame()
        header.setStyleSheet("background-color: white; border-radius: 8px;")
        header_layout = QHBoxLayout()
        header_layout.setContentsMargins(15, 10, 15, 10)

        search_bar = QLineEdit()
        search_bar.setPlaceholderText("Buscar...")
        search_bar.setFixedHeight(35)
        search_bar.setStyleSheet("""
            QLineEdit {
                border: 2px solid #90CAF9;
                border-radius: 6px;
                padding-left: 10px;
                background-color: #F5F5F5;
            }
        """)

        user_label = QLabel("Usuario")
        user_label.setFont(QFont("Arial", 12))
        user_label.setStyleSheet("color: #424242;")

        header_layout.addWidget(search_bar)
        header_layout.addStretch()
        header_layout.addWidget(user_label)

        header.setLayout(header_layout)

        # =======================
        # DASHBOARD
        # =======================
        dashboard = QFrame()
        dashboard.setStyleSheet("background-color: white; border-radius: 8px;")
        dashboard_layout = QVBoxLayout()
        dashboard_layout.setContentsMargins(20, 20, 20, 20)
        dashboard_layout.setSpacing(15)
        dashboard.setLayout(dashboard_layout)

        # Tabla
        table = QTableWidget()
        table.setColumnCount(4)
        table.setHorizontalHeaderLabels(["ID", "Nombre", "Apellido", "CI"])
        table.setRowCount(6)

        # Estilo tabla (solo líneas horizontales)
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

        table.setShowGrid(True)
        table.setGridStyle(Qt.SolidLine)
        table.verticalHeader().setVisible(False)
        table.setSelectionMode(QTableWidget.NoSelection)

        # Datos ejemplo
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

        # Destacar primera fila con cuarto color (#BBDEFB)
        for col in range(4):
            table.item(0, col).setBackground(Qt.GlobalColor.transparent)
            table.item(0, col).setBackground(Qt.GlobalColor.white)
            table.item(0, col).setBackground(Qt.GlobalColor.transparent)
            table.item(0, col).setBackground(Qt.GlobalColor.white)

        table.setRowHeight(0, 35)
        table.setStyleSheet(table.styleSheet() + """
            QTableWidget::item:first {
                background-color: #BBDEFB;
            }
        """)

        dashboard_layout.addWidget(table)

        # Botón generar reporte
        btn_layout = QHBoxLayout()
        btn_layout.addStretch()

        btn_reporte = QPushButton("Generar Reporte")
        btn_reporte.setFixedSize(180, 40)
        btn_reporte.setStyleSheet("""
            QPushButton {
                background-color: #42A5F5;
                color: white;
                border-radius: 6px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #1E88E5;
            }
        """)

        btn_layout.addWidget(btn_reporte)
        dashboard_layout.addLayout(btn_layout)

        # =======================
        # AGREGAR COMPONENTES
        # =======================
        content_layout.addWidget(header)
        content_layout.addWidget(dashboard)

        main_layout.addWidget(sidebar)
        main_layout.addWidget(content)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())