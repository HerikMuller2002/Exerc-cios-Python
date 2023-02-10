import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QGridLayout, QLineEdit, QSizePolicy

class Sistema (QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("Calculadora")
        self.setFixedSize(400,400)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 5)
        self.display.setDisabled(True)
        self.display.setStyleSheet("* {background: white; color: black; font-size: 30px;}")
        self.display.setSizePolicy(QSizePolicy.Preferred,QSizePolicy.Expanding)

        self.add_btn(QPushButton("7"),1,0,1,1)
        self.add_btn(QPushButton("8"),1,1,1,1)
        self.add_btn(QPushButton("9"),1,2,1,1)
        self.add_btn(QPushButton("/"),1,3,1,1)
        self.add_btn(QPushButton("C"),1,4,1,1, lambda: self.display.setText(''),'background: #B22222; color: white; font-size: 20px;' )

        self.add_btn(QPushButton("4"),2,0,1,1)
        self.add_btn(QPushButton("5"),2,1,1,1)
        self.add_btn(QPushButton("6"),2,2,1,1)
        self.add_btn(QPushButton("*"),2,3,1,1)
        self.add_btn(QPushButton("<-"),2,4,1,1, lambda: self.display.setText(
            self.display.text()[:-1]
        ),'background: #FF8C00; color: white; font-size: 20px;')

        self.add_btn(QPushButton("1"),3,0,1,1)
        self.add_btn(QPushButton("2"),3,1,1,1)
        self.add_btn(QPushButton("3"),3,2,1,1)
        self.add_btn(QPushButton("+"),3,3,1,1)
        self.add_btn(QPushButton("="),3,4,2,1,
            self.btn_igual, 'background: #006400; color: white; font-size: 20px;'
        )

        self.add_btn(QPushButton("0"),4,0,1,2)
        self.add_btn(QPushButton("."),4,2,1,1)
        self.add_btn(QPushButton("-"),4,3,1,1)


        self.setCentralWidget(self.cw) 

    def add_btn(self,btn,row,column,rowspan, columnspan,funcao=None,style=None):
        self.grid.addWidget(btn,row,column,rowspan,columnspan)
        if not funcao:
            btn.clicked.connect(
                lambda: self.display.setText(
                    self.display.text() + btn.text()
                )
            )
        else:
            btn.clicked.connect(funcao)
        
        if style:
            btn.setStyleSheet(style)
        else:
            btn.setStyleSheet("*{background: #DCDCDC ;color: #4F4F4F; font-size: 20px;}")
        
        btn.setSizePolicy(QSizePolicy.Preferred,QSizePolicy.Expanding)
    
    def btn_igual(self):
        try:
            self.display.setText(
                str(eval(self.display.text()))
            )
        except Exception:
            self.display.setText("Conta inválida")


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    sistema = Sistema()
    sistema.show()
    qt.exec_()