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

if platform.system() == "Darwin" :    #Darwin은 MAC OS
    rc('font', family = 'AppleGothic')
elif platform.system() == 'Windows' :
    path="c:/windows/Fonts/malgun.ttf"      # 210 M고딕050.ttf
    font_name = font_manager.FontProperties(fname = path).get_name()
    rc('font', family = font_name)
else :
    print("Unknown System")


# chart 그리기

class graphDialog(QDialog) :
    def __init__(self) :
        super().__init__()
        self.setupUI()

    def setupUI(self) :
        # 윈도우 frame
        self.setWindowTitle("Chart")
        self.setGeometry(200, 100, 1600, 800)                # (x축 좌표, y축 좌표, x축 크기, y축 크기)
        self.setWindowIcon(QIcon('logo.png'))         # 왼쪽 상단에 icon 넣기

        self.pushButton1 = QPushButton("피자스쿨 점포수")
        self.pushButton1.clicked.connect(self.pushButton1Clicked)
        self.pushButton2 = QPushButton("피자헛 점포수")
        self.pushButton2.clicked.connect(self.pushButton2Clicked)
        self.pushButton3 = QPushButton("도미노피자 점포수")
        self.pushButton3.clicked.connect(self.pushButton3Clicked)
        self.pushButton4 = QPushButton("미스터피자 점포수")
        self.pushButton4.clicked.connect(self.pushButton4Clicked)
        self.pushButton5 = QPushButton("전국 브랜드 점포수")
        self.pushButton5.clicked.connect(self.pushButton5Clicked)

        # Figure Canvas
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)
        
        # Left Layout
        leftLayout = QVBoxLayout()
        leftLayout.addWidget(self.canvas)

        # Right Layout
        rightLayout = QVBoxLayout()
        rightLayout.addWidget(self.pushButton1)
        rightLayout.addWidget(self.pushButton2)
        rightLayout.addWidget(self.pushButton3)
        rightLayout.addWidget(self.pushButton4)
        rightLayout.addWidget(self.pushButton5)
        rightLayout.addStretch(1)   # 제일 상단에 배치

        # Layout : V Layout 2개를 나란히 붙이려면 H Layout을 사용해야함
        layout = QHBoxLayout()
        layout.addLayout(leftLayout)
        layout.addLayout(rightLayout)
        layout.setStretchFactor(leftLayout, 1)
        layout.setStretchFactor(rightLayout, 0)  # 0은 크기 조절시 크기 변경 안됨

        self.setLayout(layout)


    def pushButton1Clicked(self) :
        
        pizzaschool = pd.read_csv("./Data/pizzaschoolComplete.csv")
        pizzaschool_counts = pizzaschool.groupby('city')['store'].count().sort_values(ascending = False)

        ax = self.fig.add_subplot(111)
        ax.clear()
        result = pizzaschool.groupby('city')['store'].count().sort_values(ascending = False)
        colors = cm.coolwarm(np.linspace(1,0,len(result)))
        labels = list(pizzaschool.groupby('city')['store'].count().sort_values(ascending = False).values)

        result.plot(kind = 'bar', color = colors, ax = ax)
        rects = ax.patches

        for rect, label in zip(rects, labels) :
            plt.text(rect.get_x() + rect.get_width() / 2, 
                    rect.get_height() + 1, s = label, ha = 'center', va = 'bottom', fontsize=17)
                    
        ax.set_xlabel('광역 자치 단체', fontsize = 20)
        ax.set_title('피자스쿨 전국 점포수', fontsize = 25)
        for tick in ax.get_xticklabels():
            tick.set_rotation(0)
        self.canvas.draw()

    def pushButton2Clicked(self) :
        
        pizzahut = pd.read_csv("./Data/pizza_hut_address_complete.csv")
        pizzahut_counts = pizzahut.groupby('city')['store'].count().sort_values(ascending = False)

        ax = self.fig.add_subplot(111)
        ax.clear()
        result = pizzahut.groupby('city')['store'].count().sort_values(ascending = False)
        colors = cm.coolwarm(np.linspace(1,0,len(result)))
        labels = list(pizzahut.groupby('city')['store'].count().sort_values(ascending = False).values)

        result.plot(kind = 'bar', color = colors, ax = ax)
        rects = ax.patches

        for rect, label in zip(rects, labels) :
            plt.text(rect.get_x() + rect.get_width() / 2, 
            rect.get_height() + 1, s = label, ha = 'center', va = 'bottom', fontsize=17)

        ax.set_xlabel('광역 자치 단체', fontsize = 20)
        ax.set_title('피자헛 전국 점포수', fontsize = 25)
        for tick in ax.get_xticklabels():
            tick.set_rotation(0)
        self.canvas.draw()

    def pushButton3Clicked(self) :
        
        domino = pd.read_csv("./Data/dominopizza_complete.csv")
        domino.loc[domino['city'] == '경산북도', 'city'] = '경상북도'
        domino_counts = domino.groupby('city')['store'].count().sort_values(ascending = False)

        ax = self.fig.add_subplot(111)
        ax.clear()
        result = domino.groupby('city')['store'].count().sort_values(ascending = False)
        colors = cm.coolwarm(np.linspace(1,0,len(result)))
        labels = list(domino.groupby('city')['store'].count().sort_values(ascending = False).values)

        result.plot(kind = 'bar', color = colors, ax = ax)
        rects = ax.patches

        for rect, label in zip(rects, labels) :
            plt.text(rect.get_x() + rect.get_width() / 2, 
            rect.get_height() + 1, s = label, ha = 'center', va = 'bottom', fontsize=17)

        ax.set_xlabel('광역 자치 단체', fontsize = 20)
        ax.set_title('도미노 전국 점포수', fontsize = 25)
        for tick in ax.get_xticklabels():
            tick.set_rotation(0)
        self.canvas.draw()
    
    def pushButton4Clicked(self) :
        
        #mrpizza = pd.read_csv("./Data/mrpizza_complete.csv")
        mrpizza = pd.read_csv("./Data/mrpizza_complete.csv")
        mrpizza_counts = mrpizza.groupby('city')['store'].count().sort_values(ascending = False)

        ax = self.fig.add_subplot(111)
        ax.clear()
        result = mrpizza.groupby('city')['store'].count().sort_values(ascending = False)
        colors = cm.coolwarm(np.linspace(1,0,len(result)))
        labels = list(mrpizza.groupby('city')['store'].count().sort_values(ascending = False).values)

        result.plot(kind = 'bar', color = colors, ax = ax)
        rects = ax.patches

        for rect, label in zip(rects, labels) :
            plt.text(rect.get_x() + rect.get_width() / 2, 
            rect.get_height() + 1, s = label, ha = 'center', va = 'bottom', fontsize=17)

        ax.set_xlabel('광역 자치 단체', fontsize = 20)
        ax.set_title('미스터피자 전국 점포수', fontsize = 25)
        for tick in ax.get_xticklabels():
            tick.set_rotation(0)
        self.canvas.draw()

    def pushButton5Clicked(self) :
        
        pizzaschool = pd.read_csv("./Data/pizzaschoolComplete.csv")
        pizzahut = pd.read_csv("./Data/pizza_hut_address_complete.csv")
        domino = pd.read_csv("./Data/dominopizza_complete.csv")
        domino.loc[domino['city'] == '경산북도', 'city'] = '경상북도'
        mrpizza = pd.read_csv("./Data/mrpizza_complete.csv")

        pizzaschool_counts = pizzaschool.groupby('city')['store'].count().sort_values(ascending = False)
        pizzahut_counts = pizzahut.groupby('city')['store'].count().sort_values(ascending = False)
        domino_counts = domino.groupby('city')['store'].count().sort_values(ascending = False)
        mrpizza_counts = mrpizza.groupby('city')['store'].count().sort_values(ascending = False)

        pizza_counts = pd.merge(pizzahut_counts, domino_counts, on = 'city', how = 'outer')
        pizza_counts.rename(columns = {
            pizza_counts.columns[0] : 'pizzahut', 
            pizza_counts.columns[1] : 'domino'
        }, inplace = True)
        pizza_counts = pd.merge(pizzaschool_counts, pizza_counts, on = 'city', how = 'outer')
        pizza_counts.rename(columns = {
            pizza_counts.columns[0] : 'pizzaschool'
        }, inplace = True)
        pizza_counts = pd.merge(mrpizza_counts, pizza_counts, on = 'city', how = 'outer')
        pizza_counts.rename(columns = {
            pizza_counts.columns[0] : 'mrpizza'
        }, inplace = True)

        pizza_counts['pizzaschool'].fillna(0, inplace = True)
        pizza_counts['mrpizza'].fillna(0, inplace = True)
        pizza_counts['pizzaschool'] = pizza_counts['pizzaschool'].apply(lambda x: int(x))
        pizza_counts['mrpizza'] = pizza_counts['mrpizza'].apply(lambda x: int(x))
        #pizza_counts = pizza_counts.sort_values(by = 'pizzaschool', ascending = False)
        pizza_counts = pizza_counts[['pizzaschool', 'domino', 'pizzahut', 'mrpizza']]


        df_1 = pd.DataFrame(pizza_counts['pizzaschool'])
        df_2 = pd.DataFrame(pizza_counts['domino'])
        df_3 = pd.DataFrame(pizza_counts['pizzahut'])
        df_4 = pd.DataFrame(pizza_counts['mrpizza'])

        df_1.rename(columns = {'pizzaschool' : 'count'}, inplace = True)
        df_2.rename(columns = {'domino' : 'count'}, inplace = True)
        df_3.rename(columns = {'pizzahut' : 'count'}, inplace = True)
        df_4.rename(columns = {'mrpizza' : 'count'}, inplace = True)

        df_1['brand'] = 'pizzashcool'
        df_2['brand'] = 'domino'
        df_3['brand'] = 'pizzahut'
        df_4['brand'] = 'mrpizza'

        pizza_counts2 = pd.concat([df_1, df_2, df_3, df_4], axis = 0)
        pizza_counts2.reset_index(inplace = True)
        pizza_counts2.fillna(0, inplace = True)
        pizza_counts2['count'] = pizza_counts2['count'].apply(lambda x : int(x))

        ax = self.fig.add_subplot(111)
        ax.clear()
        labels = list(pizza_counts2['count'].values)

        sns.barplot(x = 'city', y = 'count', data = pizza_counts2, hue = 'brand', palette= sns.color_palette("bwr_r", 6), ax = ax)
        rects = ax.patches

        for rect, label in zip(rects, labels) :
            plt.text(rect.get_x() + 0.02 + rect.get_width() / 2, rect.get_height() + 1.5, s = label, ha = 'center', va = 'bottom', fontsize=13)

        ax.set_xlabel('광역 자치 단체', fontsize = 20)
        ax.set_title('피자 브랜드 전국 점포수', fontsize = 25)
        for tick in ax.get_xticklabels():
            tick.set_rotation(0)
        self.canvas.draw()

class mywindows(QWidget) :
    def __init__(self) :
        super().__init__()
        self.setupUI()

    def setupUI(self) :
        # 윈도우 frame
        self.setWindowTitle("project-01")
        self.setGeometry(800, 200, 300, 300)                # (x축 좌표, y축 좌표, x축 크기, y축 크기)
        self.setWindowIcon(QIcon('light.png'))          # 왼쪽 상단에 icon 넣기
        
        self.pushButton = QPushButton('chart')  # Button, layout생성해서 사용할 때는 self 없이
        self.pushButton.clicked.connect(self.pushButtonClicked)
        self.label = QLabel()

        # Layout 생성
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.pushButton)
        self.setLayout(layout)
    
    def pushButtonClicked(self) :
        dlg = graphDialog()        
        dlg.exec_()
        
    
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    mywindow = graphDialog()
    mywindow.show()
    app.exec_()