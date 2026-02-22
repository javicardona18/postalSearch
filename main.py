import sys
from PySide6.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)

label = QLabel("Hola mundo")
label.show()

sys.exit(app.exec())