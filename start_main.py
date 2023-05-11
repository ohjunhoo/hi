import sys
import os
from model import model
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
    m=model
    def __init__(self):
        super(MainWindow,self).__init__()
        self.ui = QUiLoader().load(resource_path("UI/pd_ui.ui"))
        self.m.train_model(self.m)
        self.ui.btn_pd.clicked.connect(self.btn_pd_clicked)
    
    def btn_pd_clicked(self):
        length = self.ui.f_length.text()
        weight = self.ui.f_weight.text()
        result =self.m.predict(self.m,length, weight)
        result_str =""
        if result ==[1]:
            result_str="도미"
        else:
            result_str ="빙어"
        self.ui.lb_result.setText(result_str)

if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    window =MainWindow()
    window.ui.show()
    sys.exit(app.exec())