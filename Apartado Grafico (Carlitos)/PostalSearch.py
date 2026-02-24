import sys
import os
from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette, QBrush, QPixmap, QFontDatabase, QFont


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        #Ruta base del proyecto
        base_dir = os.path.dirname(os.path.abspath(__file__))

        #Se carga la fuente
        font_path = os.path.join(base_dir, "Resources", "Fuentes", "Banita.ttf")
        font_id = QFontDatabase.addApplicationFont(font_path)
        
        #Si se encuentra la fuente, font_id es un id si no devuelve -1 y no se cumple el if.
        if font_id != -1:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            self.custom_font = QFont(font_family, 40)
        else:
            print("Error cargando la fuente")
            self.custom_font = QFont("Arial", 40)

        #Se carga el logo.
        logo_path = os.path.join(base_dir, "Resources", "imagenes", "logo.png")
    
        self.original_logo = QPixmap(logo_path)
        self.logo_label = QLabel(self)
        self.logo_label.setPixmap(self.original_logo)
        self.logo_label.setFixedSize(750, 120)

        #Se carga el fondo.
        background_path = os.path.join(base_dir, "Resources", "imagenes", "fondo.png")
        self.background = QPixmap(background_path)
        
        #Detalles de la ventana.
        self.setWindowTitle("PostalSearch")
        self.showMaximized()    

    def resizeEvent(self, event):
        #Escalando el fondo al tamaño de la ventana.
        scaled = self.background.scaled(
            self.size(),
            Qt.IgnoreAspectRatio,
            Qt.SmoothTransformation
        )
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(scaled))
        self.setPalette(palette)
        
        #Escalando el logo al tamaño de la ventana.
        nueva_escala = int(self.width() * 0.45)  # 10% del ancho ventana
        logo_escalado = self.original_logo.scaled(nueva_escala,nueva_escala,Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.logo_label.setPixmap(logo_escalado)
        
        super().resizeEvent(event)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()