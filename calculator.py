import sys
from PyQt5 import QtWidgets, uic


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("calculator.ui", self)

        self.expression = ""

        self.number0 = self.findChild(QtWidgets.QPushButton, 'number0')
        self.number1 = self.findChild(QtWidgets.QPushButton, 'number1')
        self.number2 = self.findChild(QtWidgets.QPushButton, 'number2')
        self.number3 = self.findChild(QtWidgets.QPushButton, 'number3')
        self.number4 = self.findChild(QtWidgets.QPushButton, 'number4')
        self.number5 = self.findChild(QtWidgets.QPushButton, 'number5')
        self.number6 = self.findChild(QtWidgets.QPushButton, 'number6')
        self.number7 = self.findChild(QtWidgets.QPushButton, 'number7')
        self.number8 = self.findChild(QtWidgets.QPushButton, 'number8')
        self.number9 = self.findChild(QtWidgets.QPushButton, 'number9')
        self.arti = self.findChild(QtWidgets.QPushButton, 'arti')
        self.eksi = self.findChild(QtWidgets.QPushButton, 'eksi')
        self.carpi = self.findChild(QtWidgets.QPushButton, 'carpi')
        self.bolu = self.findChild(QtWidgets.QPushButton, 'bolu')
        self.esittir = self.findChild(QtWidgets.QPushButton, 'esittir')
        self.temizle = self.findChild(QtWidgets.QPushButton, 'temizle')
        self.nokta = self.findChild(QtWidgets.QPushButton, 'nokta')
        self.parantez1 = self.findChild(QtWidgets.QPushButton, 'parantez1')
        self.parantez2 = self.findChild(QtWidgets.QPushButton, 'parantez2')
        self.ekran = self.findChild(QtWidgets.QLineEdit, 'ekran')

        self.number0.clicked.connect(self.buttonClick)
        self.number1.clicked.connect(self.buttonClick)
        self.number2.clicked.connect(self.buttonClick)
        self.number3.clicked.connect(self.buttonClick)
        self.number4.clicked.connect(self.buttonClick)
        self.number5.clicked.connect(self.buttonClick)
        self.number6.clicked.connect(self.buttonClick)
        self.number7.clicked.connect(self.buttonClick)
        self.number8.clicked.connect(self.buttonClick)
        self.number9.clicked.connect(self.buttonClick)
        self.arti.clicked.connect(self.buttonClick)
        self.eksi.clicked.connect(self.buttonClick)
        self.carpi.clicked.connect(self.buttonClick)
        self.bolu.clicked.connect(self.buttonClick)
        self.esittir.clicked.connect(self.buttonClick)
        self.temizle.clicked.connect(self.buttonClick)
        self.nokta.clicked.connect(self.buttonClick)
        self.parantez1.clicked.connect(self.buttonClick)
        self.parantez2.clicked.connect(self.buttonClick)

    def keyPressEvent(self, event):
        if str(event.key()) == "48":
            self.expression += "0"
        if str(event.key()) == "49":
            self.expression += "1"
        if str(event.key()) == "50":
            self.expression += "2"
        if str(event.key()) == "51":
            self.expression += "3"
        if str(event.key()) == "52":
            self.expression += "4"
        if str(event.key()) == "53":
            self.expression += "5"
        if str(event.key()) == "54":
            self.expression += "6"
        if str(event.key()) == "55":
            self.expression += "7"
        if str(event.key()) == "56":
            self.expression += "8"
        if str(event.key()) == "57":
            self.expression += "9"
        if str(event.key()) == "47":
            self.expression += "/"
        if str(event.key()) == "42":
            self.expression += "*"
        if str(event.key()) == "45":
            self.expression += "-"
        if str(event.key()) == "43":
            self.expression += "+"
        if str(event.key()) == "46":
            self.expression += "."
        if str(event.key()) == "40":
            self.expression += "("
        if str(event.key()) == "41":
            self.expression += ")"
        if str(event.key()) == "16777219":
            self.expression = ""
        if str(event.key()) == "16777220" or str(event.key()) == "16777221":
            self.expression = str(eval(self.expression))
        if str(event.key()) == "16777216":
            self.close()
        if str(event.key()) == "44":
            self.expression += "."

        self.ekran.setText(self.expression)

    def buttonClick(self):
        senderButton = self.sender()
        if str(senderButton.objectName()) != "esittir" and str(senderButton.objectName()) != "temizle":
            self.expression += str(senderButton.text())

        if str(senderButton.objectName()) == "temizle":
            self.expression = ""

        if str(senderButton.objectName()) == "esittir":
            self.expression = str(eval(self.expression))

        self.ekran.setText(self.expression)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.update()
    app.exec_()
