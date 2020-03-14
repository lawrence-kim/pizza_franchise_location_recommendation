import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *       # 종료하는 것은 widget만으로 안됨. 추가적으로 import 해줘야 함
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

from sklearn.tree import DecisionTreeClassifier      # 0인지 1인지 객관식이기때문에 Classifier로 사용
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import os

if platform.system() == "Darwin" :    #Darwin은 MAC OS
    rc('font', family = 'AppleGothic')
elif platform.system() == 'Windows' :
    path="c:/windows/Fonts/malgun.ttf"      # 210 M고딕050.ttf
    font_name = font_manager.FontProperties(fname = path).get_name()
    rc('font', family = font_name)
else :
    print("Unknown System")


# 머신러닝
class machineLearingDialog(QDialog) :
    def __init__(self) :
        super().__init__()
        self.setupUI()
        self.setStyleSheet('font-size: 13pt; font-family: Courier;')

    def setupUI(self) :
        # 윈도우 frame
        self.setWindowTitle("MACHINE LEARNING")
        self.setGeometry(700, 150, 500, 350)                # (x축 좌표, y축 좌표, x축 크기, y축 크기)
        self.setWindowIcon(QIcon('logo.png'))          # 왼쪽 상단에 icon 넣기

        self.pushButton1 = QPushButton("브랜드 예측")
        self.pushButton1.clicked.connect(self.pushButton1Clicked)
        self.pushButton2 = QPushButton("입지 선정")
        self.pushButton2.clicked.connect(self.pushButton2Clicked)

        self.label1 = QLabel("지역 : ")
        self.label2 = QLabel("예산 : ")
        self.label3 = QLabel("")
        self.label4 = QLabel("")

        self.lineEdit1 = QLineEdit()
        self.lineEdit2 = QLineEdit()
    

        # Layout : V Layout 2개를 나란히 붙이려면 H Layout을 사용해야함
        layout = QGridLayout()
        layout.addWidget(self.label1, 0, 0,)
        layout.addWidget(self.lineEdit1, 0, 1)
        layout.addWidget(self.label2, 1, 0)
        layout.addWidget(self.lineEdit2, 1, 1)
        layout.addWidget(self.pushButton1, 2, 1)
        layout.addWidget(self.label3, 3, 1)
        layout.addWidget(self.pushButton2, 4, 1)


    
        self.setLayout(layout)

    def pushButton2Clicked(self) :
        os.system('python pizza_geo2.py')

    def pushButton1Clicked(self) :
        cost = int(self.lineEdit2.text())
        area = str(self.lineEdit1.text())

        mlDF = pd.read_csv("./Data/machindLearning_data.csv")

        city = mlDF[mlDF['area'].apply(lambda x : x.find(area)) != -1]['city'].values[0]
        citycode = mlDF[mlDF['area'].apply(lambda x : x.find(area)) != -1]['citycode'].values[0]
        count = mlDF[mlDF['area'].apply(lambda x : x.find(area)) != -1]['count'].values[0]
        population = mlDF[mlDF['area'].apply(lambda x : x.find(area)) != -1]['population'].values[0]
        EaringRatio = mlDF[mlDF['area'].apply(lambda x : x.find(area)) != -1]['EarningRatio'].values[0]
        mincost = mlDF[mlDF['city'] == city]['cost'].min()

        if cost >= mincost :
            train,test = train_test_split(mlDF, random_state = 0)
            target_col = ['cost', 'citycode', 'count', 'population', 'EarningRatio']
            train_X = train[target_col]
            train_Y = train['brand']
            test_X = test[target_col]
            test_Y = test['brand']

            features_one = train_X.values
            target = train_Y.values

            clf = RandomForestClassifier(max_depth = 7, n_estimators = 10, max_features = 3)
            clf.fit(features_one, target)
            
            wantBrand = np.array([cost, citycode, count, population, EaringRatio])
            pre = clf.predict([wantBrand])
            cost = format(cost, ",") + "원"
            self.label3.setText("창업 비용 : " + str(cost) + "\n원하는 지역 : " + str(area) + "\n\n피자 브랜드 : " + str(pre[0]))

        else :
            cost = format(cost, ",") + "원"
            #self.label3.setText("최소 창업 비용 :", mincost, "\n원하는 지역 :", city, "\n안타깝지만 해당 비용으로 원하는 지역에서 창업하실 수 없습니다.")
            self.label3.setText("창업 비용 : " + str(cost) + "\n원하는 지역 : " + str(area) + "\n\n안타깝지만 해당 비용으로 \n원하는 지역에서 창업하실 수 없습니다.")
            #self.label4.setText("안타깝지만 해당 비용으로 원하는 지역에서 창업하실 수 없습니다.")

            
class mywindows(QWidget) :
    def __init__(self) :
        super().__init__()
        self.setupUI()

    def setupUI(self) :
        # 윈도우 frame
        self.setWindowTitle("project-06")
        self.setGeometry(800, 200, 300, 300)                # (x축 좌표, y축 좌표, x축 크기, y축 크기)
        self.setWindowIcon(QIcon('light.png'))          # 왼쪽 상단에 icon 넣기
        
        self.pushButton = QPushButton('MACHINE LEARNING')  # Button, layout생성해서 사용할 때는 self 없이
        self.pushButton.clicked.connect(self.pushButtonClicked)
        self.label = QLabel()

        # Layout 생성
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.pushButton)
        self.setLayout(layout)
    
    def pushButtonClicked(self) :
        dlg = machineLearingDialog()        
        dlg.exec_()
        
    
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    mywindow = machineLearingDialog()
    mywindow.show()
    app.exec_()