from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit
import sys


class Mywindow(QMainWindow):
    def __init__(self):
        super(Mywindow, self).__init__()
        self.setGeometry(200, 200, 300, 300) # pay attettion for coordinates :) 
        self.setWindowTitle("Calculator")
        # input fields
        self.firstField = self.CreateInputField("a", 100, 25)
        self.secondField = self.CreateInputField("b", 100, 50)
        self.resultField = self.CreateLabel("Result", 50, 100)
        # Math Operation Input
        self.plusButton = self.CreateButton("+", 100, 150, self.Plus)
        self.minusButton = self.CreateButton("-", 100, 175, self.Minus)
        self.multiplyButton = self.CreateButton("*", 100, 200, self.Multiply)
        self.divideButton = self.CreateButton("/", 100, 225, self.Divide)
        # Resetting Start Values
        self.a = 0
        self.b = 0
        self.result = 0

    def CreateButton(self, text, x, y, fun):
        newButton = QtWidgets.QPushButton(self)
        newButton.setText(text)
        newButton.move(x, y)
        newButton.clicked.connect(fun)
        return newButton

    def CreateInputField(self, label, x, y):
        self.CreateLabel(label, x - 50, y)
        line = QLineEdit(self)
        line.move(x, y)
        line.resize(200, 32)

    def CreateLabel(self, text, x, y):
        newLabel = QtWidgets.QLabel(self)
        newLabel.setText(text)
        newLabel.move(x, y)
        return newLabel

    def UpdateInput(self): # isdigit doenst work for none types thats why we have errors :) 
        try:
            self.a = float(self.firstField.text())
        except:
            print("Program cant handle a data...")
            self.a = 0
        
        try:
            self.b = float(self.secondField.text())
        except:
            print("Program cant handle a data...")
            self.b = 0

    def UpdateOutput(self):
        self.resultField.setText("Result: " + str(self.result)) # onlu 1 argument

    def Plus(self):
        self.UpdateInput()
        self.result = self.a + self.b
        self.UpdateOutput()

    def Minus(self):
        self.UpdateInput()
        self.result = self.a - self.b
        self.UpdateOutput()

    def Multiply(self):
        self.UpdateInput()
        self.result = self.a * self.b
        self.UpdateOutput()

    def Divide(self):
        self.UpdateInput()
        self.result = self.a / self.b
        self.UpdateOutput()


app = QApplication(sys.argv)
window = Mywindow()
window.show()
sys.exit(app.exec_())
