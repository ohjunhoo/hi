import sys
import os

from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6 import QtCore
from PySide6.QtCore import QFile, QIODevice

# 파일 경로
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."),relative_path)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()

        self.ui = QUiLoader().load(resource_path("UI/gui_test.ui"))
        # 시그널 등록
        self.ui.btn_push.clicked.connect(self.say_hello)
    
    # 슬롯
    def say_hello(self):
        button = QMessageBox.question(self, "Hello", "Push")
        if button == QMessageBox.Yes:
            QMessageBox.information(self, "Yes","예스")
        else:
            QMessageBox.information(self, "No","노")

if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    window =MainWindow()
    window.ui.show()
    sys.exit(app.exec())