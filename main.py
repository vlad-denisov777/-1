from PyQt5.QtWidgets import QLabel, QWidget, QApplication, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit 
from PyQt5.QtCore import Qt

class MainWin(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.set_appear()
        self.unitUT()
        self.connects()
        self.show()

    def set_appear(self):
        self.resize(500, 300)
        self.setWindowTitle('Инструкция')
        self.move(250, 250)

    def unitUT(self):
        hello = QLabel('Здесь инструкция')
        instr = QLabel('Здесь инструкция')
        button = QPushButton('Начать')
        line_1 = QVBoxLayout()

    def connects(self):
        pass

if __name__ == '__main__':
    app = QApplication([])
    main = MainWin()
    app.exec_()
