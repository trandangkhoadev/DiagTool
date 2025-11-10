import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui.mainUI import Ui_MainWindow
from Controller.DiagToolController import DiagToolController

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.controller = DiagToolController(self.ui, self)

def start():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    start()