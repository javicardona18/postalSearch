import sys
from PySide6.QtWidgets import QApplication
from controladores.controlador_principal import ControladorPrincipal
from modelos.modelo_pasajero import crear_tabla
from modelos.modelo_pasajero import crear_tabla, insertar_datos_prueba

if __name__ == "__main__":
    crear_tabla()
    insertar_datos_prueba()
    app = QApplication(sys.argv)
    ventana = ControladorPrincipal()
    ventana.show()
    sys.exit(app.exec())