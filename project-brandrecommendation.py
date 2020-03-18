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
import os

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
        self.setStyleSheet('font-size: 13pt; font-family: Courier;')

    def setupUI(self) :
        # windows frame
        self.setWindowTitle("Machine Learning")
        self.setGeometry(700, 150, 500, 350)                
        self.setWindowIcon(QIcon('logo.png'))          

        self.pushButton1 = QPushButton("execute")
        self.pushButton1.clicked.connect(self.pushButton1Clicked)

        self.label1 = QLabel("District : ")
        self.label2 = QLabel("Initial Investment : ")
        self.label3 = QLabel("")
        self.label4 = QLabel("")

        self.lineEdit1 = QLineEdit()
        self.lineEdit2 = QLineEdit()
        layout = QGridLayout()
        layout.addWidget(self.label1, 0, 0,)
        layout.addWidget(self.lineEdit1, 0, 1)
        layout.addWidget(self.label2, 1, 0)
        layout.addWidget(self.lineEdit2, 1, 1)
        layout.addWidget(self.pushButton1, 2, 1)
        layout.addWidget(self.label3, 3, 1)
        self.setLayout(layout)


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
            
            self.label3.setText("창업 비용 : " + str(cost) + "\n원하는 지역 : " + str(area) + "\n\n안타깝지만 해당 비용으로 \n원하는 지역에서 창업하실 수 없습니다.")
            

            
class mywindows(QWidget) :
    def __init__(self) :
        super().__init__()
        self.setupUI()
        
    
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    mywindow = machineLearingDialog()
    mywindow.show()
    app.exec_()