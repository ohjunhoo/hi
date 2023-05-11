import sys
from PySide6.QtWidgets import QApplication, QMainWindow

class MyAPP(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.statusBar().showMessage('Ready')
        self.setWindowTitle("Statusbar")
        self.setGeometry(300,300,300,200)
        self.show()


if __name__ == "__main__":
    app =QApplication(sys.argv)
    ex=MyAPP()
    sys.exit(app.exec_())
