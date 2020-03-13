import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *       
from PyQt5.QtGui import QImage
from PyQt5.QtGui import *
import subprocess
import os


class mywindows(QWidget) :
    def __init__(self) :
        super().__init__()
        self.setupUI()
        self.setStyleSheet('font-size: 13pt; font-family: Courier;')
        self.setWindowIcon(QIcon('logo.png'))
        self.setStyleSheet("background-color: white;")

    def setupUI(self) :
        # windows frame
        self.setWindowTitle("Pizza brand prediction")
        self.setGeometry(750, 150, 500, 700)               

        self.pushButton1 = QPushButton('BRAND INTRODUCE')  
        self.pushButton1.clicked.connect(self.pushButton1Clicked)
        self.pushButton2 = QPushButton('CHART')  
        self.pushButton2.clicked.connect(self.pushButton2Clicked)
        self.pushButton3 = QPushButton('VISUALIZATION')  
        self.pushButton3.clicked.connect(self.pushButton3Clicked)
       

        self.pushButton4 = QPushButton('BUSAN MAP')  
        self.pushButton4.clicked.connect(self.pushButton4Clicked)


        self.pushButton5 = QPushButton('MACHINE LEARNING 1')  
        self.pushButton5.clicked.connect(self.pushButton5Clicked)
        self.pushButton6 = QPushButton('MACHINE LEARNING 2')  
        self.pushButton6.clicked.connect(self.pushButton6Clicked)
        self.pushButton7 = QPushButton('USING DATA')  
        self.pushButton7.clicked.connect(self.pushButton7Clicked)
        self.label1 = QLabel("")

        self.pushButton1.setSizePolicy(
            QSizePolicy.Preferred,
            QSizePolicy.Expanding)
        self.pushButton2.setSizePolicy(
            QSizePolicy.Preferred,
            QSizePolicy.Expanding)
        self.pushButton3.setSizePolicy(
            QSizePolicy.Preferred,
            QSizePolicy.Expanding)
        self.pushButton4.setSizePolicy(
            QSizePolicy.Preferred,
            QSizePolicy.Expanding)
        self.pushButton5.setSizePolicy(
            QSizePolicy.Preferred,
            QSizePolicy.Expanding)
        self.pushButton6.setSizePolicy(
            QSizePolicy.Preferred,
            QSizePolicy.Expanding)
        self.pushButton7.setSizePolicy(
            QSizePolicy.Preferred,
            QSizePolicy.Expanding)


        image = QLabel(self)
        pixmap = QPixmap("./Data/noun_pizza-1.png")
        image.setPixmap(pixmap)
        image.setGeometry(0, 0, 0, 0)
        image.show()

        # Layout 
        topLayout = QVBoxLayout()

        
        # Right Layout
        bottomLayout = QGridLayout()
        bottomLayout.addWidget(image, 0, 1, 1, 1)
        bottomLayout.addWidget(self.label1, 0, 0)
        bottomLayout.addWidget(self.label1, 0, 2)
        bottomLayout.addWidget(self.pushButton1, 2, 1)
        bottomLayout.addWidget(self.pushButton7, 3, 1)
        bottomLayout.addWidget(self.pushButton2, 4, 1)
        bottomLayout.addWidget(self.pushButton3, 5, 1)
        bottomLayout.addWidget(self.pushButton4, 6, 1)
        bottomLayout.addWidget(self.pushButton5, 9, 1)
        bottomLayout.addWidget(self.pushButton6, 10, 1)

        layout = QVBoxLayout()
        layout.addLayout(topLayout)
        layout.addLayout(bottomLayout)
        layout.setStretchFactor(topLayout, 1)
        layout.setStretchFactor(bottomLayout, 1)

        self.setLayout(layout)
    
    def pushButton1Clicked(self) : # 브랜드 소개
        os.system('python project-08.py')

    def pushButton2Clicked(self) : # chart
        os.system('python project-01.py')
    
    def pushButton3Clicked(self) : # visualize
        os.system('python project-02.py')
    
    def pushButton4Clicked(self) : # map - 용제씨
        os.system('python pizzastore.py')

    def pushButton5Clicked(self) : # machineLearning 1
        os.system('python project-06.py')

    def pushButton6Clicked(self) : # machineLearning 2
        os.system('python pizza_geo2.py')
    
    def pushButton7Clicked(self) : # using Data
        os.system('python project-07.py')

    def pushButton9Clicked(self) : # map - 로렌스씨
        os.system('python pizza_project.py')

    def pushButton10Clicked(self) : # map - 로렌스씨
        os.system('python pizza_project3.py')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = mywindows()
    mywindow.show()
    app.exec_()