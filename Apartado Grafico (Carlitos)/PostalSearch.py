import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QPushButton, QFrame
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette, QBrush, QPixmap

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PostalSearch")
        self.background = QPixmap("fondo.png")
        self.init_ui()
        self.showMaximized()

    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignCenter)

        panel = QFrame()
        panel.setFixedWidth(400)
        panel.setObjectName("mainPanel")
        panel.setStyleSheet("""
            #mainPanel {
                background-color: rgba(255, 255, 255, 230);
                border-radius: 15px;
                border: 2px solid black;
            }
        """)

        panel_layout = QVBoxLayout()
        panel_layout.setSpacing(25)
        panel_layout.setContentsMargins(40, 60, 40, 60)

        logo = QLabel("PostalSearch")
        logo.setAlignment(Qt.AlignCenter)
        logo.setStyleSheet("""
            font-size: 40px;
            font-weight: bold;
            color: #2c3e50;
        """)

        btn_busqueda = QPushButton("Búsqueda")
        btn_busqueda.setFixedHeight(50)

        btn_salir = QPushButton("Salir")
        btn_salir.setFixedHeight(50)
        btn_salir.clicked.connect(QApplication.quit)

        panel_layout.addWidget(logo)
        panel_layout.addSpacing(20)
        panel_layout.addWidget(btn_busqueda)
        panel_layout.addWidget(btn_salir)

        panel.setLayout(panel_layout)

        main_layout.addWidget(panel)
        self.setLayout(main_layout)

    def resizeEvent(self, event):
        scaled = self.background.scaled(
            self.size(),
            Qt.IgnoreAspectRatio,
            Qt.SmoothTransformation
        )
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(scaled))
        self.setPalette(palette)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()