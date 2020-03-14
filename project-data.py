import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *      
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys
import os

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

import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QBoxLayout

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

if platform.system() == "Darwin" :    #Darwin is for MAC OS
    rc('font', family = 'AppleGothic')
elif platform.system() == 'Windows' :
    path="c:/windows/Fonts/malgun.ttf"      # font = 210 M고딕050.ttf
    font_name = font_manager.FontProperties(fname = path).get_name()
    rc('font', family = font_name)
else :
    print("Unknown System")

class visualialog(QDialog) :
    def __init__(self) :
        super().__init__()
        self.setupUI()

    def setupUI(self) :
        # windows frame
        self.setWindowTitle("Data")
        self.setGeometry(300, 80, 1300, 800)                
        self.setWindowIcon(QIcon('logo.png'))        

        self.label1 = QLabel("")
        self.label2 = QLabel("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

        self.pushButton1 = QPushButton("ALL PIZZA BRAND")
        self.pushButton1.clicked.connect(self.pushButton1Clicked)
        self.pushButton2 = QPushButton("PIZZA BRAND IN BUSAN")
        self.pushButton2.clicked.connect(self.pushButton2Clicked)
        self.pushButton3 = QPushButton("SALESPRICE PER 3.3㎥")
        self.pushButton3.clicked.connect(self.pushButton3Clicked)
        self.pushButton4 = QPushButton("KOREA COMMERCIAL")
        self.pushButton4.clicked.connect(self.pushButton4Clicked)
        self.pushButton5 = QPushButton("KOREA SINGLES RATIO")
        self.pushButton5.clicked.connect(self.pushButton5Clicked)
        self.pushButton6 = QPushButton("MIN FOUNDING COST")
        self.pushButton6.clicked.connect(self.pushButton6Clicked)
        
        # Table Widget
        global tableWidget
        self.tableWidget = QTableWidget(self)
        self.tableWidget.resize(500, 500)
        #self.setTableWidgetData()

        # Left Layout
        global leftLayout
        leftLayout = QVBoxLayout()
        leftLayout.addWidget(self.tableWidget)

        # Right Layout
        rightLayout = QVBoxLayout()
        rightLayout.addWidget(self.pushButton1)
        rightLayout.addWidget(self.pushButton2)
        rightLayout.addWidget(self.pushButton3)
        rightLayout.addWidget(self.pushButton4)
        rightLayout.addWidget(self.pushButton5)
        rightLayout.addWidget(self.pushButton6)
        rightLayout.addWidget(self.label2)
        rightLayout.addWidget(self.label1)
        rightLayout.addStretch(1)   

        layout = QHBoxLayout()
        layout.addLayout(leftLayout)
        layout.addLayout(rightLayout)
        layout.setStretchFactor(leftLayout, 1)
        layout.setStretchFactor(rightLayout, 0)  

        self.setLayout(layout)


    def pushButton1Clicked(self) :
        pizza = pd.read_csv("./Data/pizza_all_count.csv")
        pizza.fillna(0, inplace = True)

        self.tableWidget.setRowCount(pizza.shape[0])             # table 2 x 2
        self.tableWidget.setColumnCount(pizza.shape[1])
        self.label1.setText("The total number of data instances are: " + str(pizza.shape[0]) )
        self.tableWidget.setHorizontalHeaderLabels(list(pizza.columns))

        pizzaLists = []
        pizzaData = {}
        for i in range(len(pizza)) :
            for row in pizza.itertuples():
                pizzaData['city'] = row.city
                pizzaData['district'] = row.district
                pizzaData['domino'] = str(row.domino)
                pizzaData['pizza_hut'] = str(row.pizza_hut)
                pizzaData['pizza_school'] = str(row.pizza_school)
                pizzaData['total'] = str(row.total)
                pizzaData['mr_pizza'] = str(row.mr_pizza)
                pizzaLists.append(list(pizzaData.values()))

        data = pizzaLists

        for idx, (city, district, domino, pizza_hut, pizza_school, total, mr_pizza) in enumerate(pizzaLists): 
            self.tableWidget.setItem(idx, 0, QTableWidgetItem(city))
            self.tableWidget.setItem(idx, 1, QTableWidgetItem(district))
            self.tableWidget.setItem(idx, 2, QTableWidgetItem(domino))
            self.tableWidget.setItem(idx, 3, QTableWidgetItem(pizza_hut))
            self.tableWidget.setItem(idx, 4, QTableWidgetItem(pizza_school))
            self.tableWidget.setItem(idx, 5, QTableWidgetItem(total))
            self.tableWidget.setItem(idx, 6, QTableWidgetItem(mr_pizza))
    
    def pushButton2Clicked(self) :
        busan_pizza = pd.read_csv("./Data/부산피자.csv")
        busan_pizza.fillna(0, inplace = True)

        self.tableWidget.setRowCount(busan_pizza.shape[0])             # table을 2 x 2로 만듦
        self.tableWidget.setColumnCount(busan_pizza.shape[1])
        self.label1.setText("The total number of data instances are: " + str(busan_pizza.shape[0]))
        self.tableWidget.setHorizontalHeaderLabels(list(busan_pizza.columns))

        pizzaData = {}
        pizzaLists = []
        for i in range(len(busan_pizza)) :
            for row in busan_pizza.itertuples():
                pizzaData['city'] = row.시도
                pizzaData['district'] = row.시군구
                pizzaData['store'] = row.지점명
                pizzaData['address'] = row.주소
                pizzaData['lng'] = str(round(row.lng,3))
                pizzaData['lat'] = str(round(row.lat,3))
                pizzaData['brand'] = row.브랜드
                pizzaLists.append(list(pizzaData.values()))

        data = pizzaLists

        for idx, (city, district, store, address, lng, lat, brand) in enumerate(pizzaLists): 
            self.tableWidget.setItem(idx, 0, QTableWidgetItem(city))
            self.tableWidget.setItem(idx, 1, QTableWidgetItem(district))
            self.tableWidget.setItem(idx, 2, QTableWidgetItem(store))
            self.tableWidget.setItem(idx, 3, QTableWidgetItem(address))
            self.tableWidget.setItem(idx, 4, QTableWidgetItem(lng))
            self.tableWidget.setItem(idx, 5, QTableWidgetItem(lat))
            self.tableWidget.setItem(idx, 6, QTableWidgetItem(brand))
    
    def pushButton3Clicked(self) :
        for_sales = pd.read_csv("./Data/지역별 평당 매매가.csv")
        for_sales.rename(columns = {'평당 매매가' : '평당매매가'}, inplace = True)
        for_sales.fillna(0, inplace = True)

        self.tableWidget.setRowCount(for_sales.shape[0])             # table 2 x 2
        self.tableWidget.setColumnCount(for_sales.shape[1])
        self.label1.setText("The total number of data instances are: " + str(for_sales.shape[0]) )
        self.tableWidget.setHorizontalHeaderLabels(list(for_sales.columns))

        pizzaData = {}
        pizzaLists = []
        for i in range(len(for_sales)) :
            for row in for_sales.itertuples():
                pizzaData['city'] = row.city
                pizzaData['district'] = row.district
                pizzaData['population'] = str(row.population)
                pizzaData['salesPrice'] = str(round(row.평당매매가,3))
                pizzaLists.append(list(pizzaData.values()))

        data = pizzaLists

        for idx, (city, district, population, salesPrice) in enumerate(pizzaLists): 
            self.tableWidget.setItem(idx, 0, QTableWidgetItem(city))
            self.tableWidget.setItem(idx, 1, QTableWidgetItem(district))
            self.tableWidget.setItem(idx, 2, QTableWidgetItem(population))
            self.tableWidget.setItem(idx, 3, QTableWidgetItem(salesPrice))

    def pushButton4Clicked(self) :
        commercial = pd.read_csv("./Data/전국 상권 최종본.csv")

        self.label1.setText("The total number of data instances are: " + str(commercial.shape[0]) )

        commercial = pd.concat([commercial.head(100), commercial.tail(100)], axis = 0)

        self.tableWidget.setRowCount(commercial.shape[0])             # table 2 x 2
        self.tableWidget.setColumnCount(commercial.shape[1])

        self.tableWidget.setHorizontalHeaderLabels(list(commercial.columns))

        pizzaData = {}
        pizzaLists = []
        for i in range(len(commercial)) :
            for row in commercial.itertuples():
                pizzaData['city'] = row.city
                pizzaData['district'] = row.district
                pizzaData['lng'] = str(round(row.lng,3))
                pizzaData['lat'] = str(round(row.lat,3))
                pizzaLists.append(list(pizzaData.values()))

        data = pizzaLists

        for idx, (city, district, lng, lat) in enumerate(pizzaLists): 
            self.tableWidget.setItem(idx, 0, QTableWidgetItem(city))
            self.tableWidget.setItem(idx, 1, QTableWidgetItem(district))
            self.tableWidget.setItem(idx, 2, QTableWidgetItem(lng))
            self.tableWidget.setItem(idx, 3, QTableWidgetItem(lat))

    def pushButton5Clicked(self) :
        singles = pd.read_csv("./Data/1인가구.csv")
        singles.rename(columns = {'시 도' : '시도', '시 군 구' :'시군구', '1인 가구 비율' : '일인가구비율'}, inplace = True)
        self.label1.setText("The total number of data instances are: " + str(singles.shape[0]) )

        self.tableWidget.setRowCount(singles.shape[0])             # table 2 x 2
        self.tableWidget.setColumnCount(singles.shape[1])

        self.tableWidget.setHorizontalHeaderLabels(list(singles.columns))

        pizzaData = {}
        pizzaLists = []
        for i in range(len(singles)) :
            for row in singles.itertuples() :
                pizzaData['city'] = row.시도
                pizzaData['district'] = row.시군구
                pizzaData['SinglesRatio'] = str(row.일인가구비율)
                pizzaLists.append(list(pizzaData.values()))

        data = pizzaLists

        for idx, (city, district, SinglesRatio) in enumerate(pizzaLists): 
            self.tableWidget.setItem(idx, 0, QTableWidgetItem(city))
            self.tableWidget.setItem(idx, 1, QTableWidgetItem(district))
            self.tableWidget.setItem(idx, 2, QTableWidgetItem(SinglesRatio))
    
    def pushButton6Clicked(self) :
        cost = pd.read_csv("./Data/피자 브랜드별 최소 창업비용.csv")
        cost.rename(columns = {'평당 매매가' : '평당매매가'}, inplace = True)
        self.label1.setText("The total number of data instances are: " + str(cost.shape[0]) )

        self.tableWidget.setRowCount(cost.shape[0])             # table 2 x 2 
        self.tableWidget.setColumnCount(cost.shape[1])

        self.tableWidget.setHorizontalHeaderLabels(list(cost.columns))

        pizzaData = {}
        pizzaLists = []
        for i in range(len(cost)) :
            for row in cost.itertuples():
                pizzaData['city'] = row.city
                pizzaData['district'] = row.district
                pizzaData['population'] = str(row.population)
                pizzaData['salesPrice'] = str(round(row.평당매매가,3))
                pizzaData['pizza_school'] = str(row.pizza_school)
                pizzaData['mr_pizza'] = str(row.mr_pizza)
                pizzaData['pizza_hut'] = str(row.pizza_hut)
                pizzaData['domino'] = str(row.domino)
                pizzaLists.append(list(pizzaData.values()))

        data = pizzaLists

        for idx, (city, district, population, salesPrice, pizza_school, mr_pizza, pizza_hut, domino) in enumerate(pizzaLists): 
            self.tableWidget.setItem(idx, 0, QTableWidgetItem(city))
            self.tableWidget.setItem(idx, 1, QTableWidgetItem(district))
            self.tableWidget.setItem(idx, 2, QTableWidgetItem(population))
            self.tableWidget.setItem(idx, 3, QTableWidgetItem(salesPrice))
            self.tableWidget.setItem(idx, 4, QTableWidgetItem(pizza_school))
            self.tableWidget.setItem(idx, 5, QTableWidgetItem(mr_pizza))
            self.tableWidget.setItem(idx, 6, QTableWidgetItem(pizza_hut))
            self.tableWidget.setItem(idx, 7, QTableWidgetItem(domino))



        
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    mywindow = visualialog()
    mywindow.show()
    app.exec_()