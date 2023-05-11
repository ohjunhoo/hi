import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QIcon
class MyAPP(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("Icon")
        self.setWindowIcon(QIcon('web.png'))
        self.setGeometry(300,300,300,200)
        self.show()

if __name__ == '__main__':
    app =QApplication(sys.argv)
    ex = MyAPP()
    sys.exit(app.exec_())