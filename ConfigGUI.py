
from PySide6.QtWidgets import QDialog
from ui.configUI import Ui_Config

class ConfigDiaglog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Config()
        self.ui.setupUi(self)