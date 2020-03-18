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

        self.pushButton1 = QPushButton('Intro')  
        self.pushButton1.clicked.connect(self.pushButton1Clicked)
        self.pushButton2 = QPushButton('Data')  
        self.pushButton2.clicked.connect(self.pushButton2Clicked)
        self.pushButton3 = QPushButton('Chart')  
        self.pushButton3.clicked.connect(self.pushButton3Clicked)
        self.pushButton4 = QPushButton('Brand Recommendation')  
        self.pushButton4.clicked.connect(self.pushButton4Clicked)
        self.pushButton5 = QPushButton('Sample Map')  
        self.pushButton5.clicked.connect(self.pushButton5Clicked)
        self.pushButton6 = QPushButton('Selected Map')  
        self.pushButton6.clicked.connect(self.pushButton6Clicked)
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



        image = QLabel(self)
        pixmap = QPixmap("./Data/main_logo.png")
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
        bottomLayout.addWidget(self.pushButton2, 3, 1)
        bottomLayout.addWidget(self.pushButton3, 4, 1)
        bottomLayout.addWidget(self.pushButton4, 5, 1)
        bottomLayout.addWidget(self.pushButton5, 6, 1)
        bottomLayout.addWidget(self.pushButton6, 7, 1)

        layout = QVBoxLayout()
        layout.addLayout(topLayout)
        layout.addLayout(bottomLayout)
        layout.setStretchFactor(topLayout, 1)
        layout.setStretchFactor(bottomLayout, 1)

        self.setLayout(layout)
    
    def pushButton1Clicked(self) : # intro
        os.system('python project-intro.py')

    def pushButton2Clicked(self) : # Data
        os.system('python project-data.py')

    def pushButton3Clicked(self) : # chart
        os.system('python project-chart.py')
        
    def pushButton4Clicked(self) : # ml1 recommend brand by location and budget
        os.system('python project-brandrecommendation.py')

    def pushButton5Clicked(self) : # map of all the pizza stores with commercial area clusters
        os.system('python project-samplemap.py')

    def pushButton6Clicked(self) : # ml2 map according to input location and the number of cluster
        os.system('python project-selectedmap.py')
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = mywindows()
    mywindow.show()
    app.exec_()