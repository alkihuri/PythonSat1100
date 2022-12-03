from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.counter = 0
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("counter")
        self.CreateLabel("random", 50, 75)
        self.CreateButton("button", 50, 50)

    def CreateLabel(self, text, x=50, y=50):
        self.newLabel = QtWidgets.QLabel()
        self.newLabel.setText(text)
        self.newLabel.move(x, y)

    def counterFunc(self):
        self.counter += 1
        self.newLabel.setText(str(self.counter))

    def CreateButton(self, text, x, y):
        self.newButton = QtWidgets.QPushButton(self)
        self.newButton.setText(text)
        self.newButton.move(x, y)
        self.newButton.clicked.connect(self.counterFunc)


app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())
