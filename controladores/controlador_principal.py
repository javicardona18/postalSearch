import os
from PySide6.QtWidgets import QWidget, QStackedWidget, QVBoxLayout, QApplication
from PySide6.QtGui import QPalette, QColor, QFontDatabase, QFont
from vistas.vista_menu import VistaMenu
from vistas.vista_busqueda import VistaBusqueda
from modelos.modelo_pasajero import obtener_pasajeros
from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtCore import Qt
from servicios.kiu_api import obtener_pasajeros_api
from modelos.modelo_pasajero import insertar_pasajeros_api


class ControladorPrincipal(QWidget):
    def __init__(self):
        super().__init__()

        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("#054A81"))
        self.setPalette(palette)

        ruta_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        # Fuente personalizada
        font_path = os.path.join(ruta_dir, "recursos", "fuentes", "Banita.ttf")
        font_id = QFontDatabase.addApplicationFont(font_path)

        if font_id != -1:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            custom_font = QFont(font_family, 40)
        else:
            custom_font = QFont("Arial", 40)

        QApplication.instance().setFont(custom_font)

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

        self.stack = QStackedWidget()
        layout = QVBoxLayout(self)
        layout.addWidget(self.stack)

        self.pantalla_menu = VistaMenu()
        self.pantalla_busqueda = VistaBusqueda()

        self.stack.addWidget(self.pantalla_menu)
        self.stack.addWidget(self.pantalla_busqueda)

        self.stack.setCurrentWidget(self.pantalla_menu)

        # Conexiones
        self.pantalla_menu.btnbusqueda.clicked.connect(self.ir_a_busqueda)
        self.pantalla_menu.btnsalir.clicked.connect(self.close)
        self.pantalla_busqueda.btn_back.clicked.connect(self.ir_a_menu)

        self.setWindowTitle("PostalSearch")
        self.showMaximized()

        self.cargar_tabla()

    def ir_a_busqueda(self):
        self.stack.setCurrentWidget(self.pantalla_busqueda)

    def ir_a_menu(self):
        self.stack.setCurrentWidget(self.pantalla_menu)

    def cargar_tabla(self):
        datos = obtener_pasajeros()

        tabla = self.pantalla_busqueda.table
        tabla.setRowCount(len(datos))

        for row, fila in enumerate(datos):
            for col, valor in enumerate(fila):
                item = QTableWidgetItem(str(valor))
                item.setFlags(Qt.ItemIsEnabled)
                item.setTextAlignment(Qt.AlignCenter)
                tabla.setItem(row, col, item)

    def actualizar_desde_api(self):

        pasajeros = obtener_pasajeros_api()

        insertar_pasajeros_api(pasajeros)

        self.cargar_tabla()
            