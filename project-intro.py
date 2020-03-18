import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *      
from PyQt5.QtGui import *
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import seaborn as sns

import platform
from matplotlib import font_manager,rc
import matplotlib as mpl
import matplotlib.cm as cm

from sklearn.tree import DecisionTreeClassifier      
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

if platform.system() == "Darwin" :    #Darwin is for MAC OS
    rc('font', family = 'AppleGothic')
elif platform.system() == 'Windows' :
    path="c:/windows/Fonts/malgun.ttf"      
    font_name = font_manager.FontProperties(fname = path).get_name()
    rc('font', family = font_name)
else :
    print("Unknown System")

class machineLearingDialog(QDialog) :
    def __init__(self) :
        super().__init__()
        self.setupUI()

    def setupUI(self) :
        # windows frame
        self.setWindowTitle("Brand Introduction")
        self.setGeometry(400, 100, 1000, 600)                
        self.setWindowIcon(QIcon('logo.png'))          

        self.pushButton1 = QPushButton("Pizza School")
        self.pushButton1.clicked.connect(self.pushButton1Clicked)
        self.pushButton2 = QPushButton("Domino's")
        self.pushButton2.clicked.connect(self.pushButton2Clicked)
        self.pushButton4 = QPushButton("Pizza Hut")
        self.pushButton4.clicked.connect(self.pushButton4Clicked)


        self.label1 = QLabel("\n\n\n\n\n\n\n\n\n\n")
        
        # Figure Canvas
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)

        topLayout = QGridLayout()
        topLayout.addWidget(self.pushButton1, 0, 0)
        topLayout.addWidget(self.pushButton2, 0, 1)
        topLayout.addWidget(self.pushButton4, 0, 2)

        global bottomLayout
        bottomLayout = QVBoxLayout()
        bottomLayout.addWidget(self.label1)

        layout = QVBoxLayout()
        layout.addLayout(topLayout)
        layout.addLayout(bottomLayout)
        layout.setStretchFactor(topLayout, 0)
        layout.setStretchFactor(bottomLayout, 0)  
        self.setLayout(layout)


    def pushButton1Clicked(self) :
        self.label1.setText("""
        피자스쿨(Pizza School)은 대한민국의 피자 전문 프랜차이즈이다. \n
        피자스쿨은 2004년 12월 가맹사업을 시작하였다. 당초에는 차량을 이용한 이동식 피자 판매점을 모델로 하였으나, \n
        이후 매장을 갖춘 프랜차이즈 형태로 전환하였다. \n
        2006년부터는 기존 8천원에서 1만원이었던 가격을 모두 5천원으로 내리는 가격 인하 마케팅을 시작하였다. \n
        동네 피자보단 왠지 브랜드라서 안심이 되는 이미지와 저렴한 가격으로 가맹점 수를 급격히 늘렸다. \n
        피자스쿨의 성공 이후 피자마루, 59쌀피자 등의 저가 피자 전문 브랜드가 등장했다. \n
        2019년 7월 현재 전국 925개의 매장을 운영하고 있으며, 부산에는 40개의 매장이 있다.\n""")

    def pushButton2Clicked(self) :
        self.label1.setText("""
        도미노피자(Domino's Pizza, Inc. 또는 간단히 Domino's)는 미국의 피자 배달 전문 브랜드이다.\n
        현재 전 세계 70개국, 1만개 이상의 점포를 두고 있다.\n
        대한민국에는 1990년에 첫 점포인 송파구 오금점이 문을 연 후, 1999년 100호점을 돌파했고 \n
        2003년에는 200호점, 2008년에는 300호점을 돌파하였다.\n
        2019년 7월 현재 전국 459개의 매장을 운영하고 있으며, 부산에는 28개의 매장이 있다.\n""")
       
    def pushButton4Clicked(self) :
        self.label1.setText("""
        피자헛(Pizza Hut)은 미국의 피자 프랜차이즈이다.\n
        현재 100여 개국 이상에 피자헛 점포를 두고 있으며, 일부 점포에서는 고객이 직접 와서 피자헛 제품을 먹거나 \n
        테이크아웃을 할 수 있는 피자헛 레스토랑이기도 한다.\n
        대한민국에서는 2019년 7월 현재 전국 348개의 매장을 운영하고 있으며, 부산에는 24개의 매장이 있다.\n""")

        
    
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    mywindow = machineLearingDialog()
    mywindow.show()
    app.exec_()