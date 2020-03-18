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

if platform.system() == "Darwin" :    #Darwin is for MAC OS
    rc('font', family = 'AppleGothic')
elif platform.system() == 'Windows' :
    path="c:/windows/Fonts/malgun.ttf"     
    font_name = font_manager.FontProperties(fname = path).get_name()
    rc('font', family = font_name)
else :
    print("Unknown System")


class graphDialog(QDialog) :
    def __init__(self) :
        super().__init__()
        self.setupUI()

    def setupUI(self) :
        # windows frame
        self.setWindowTitle("Chart")
        self.setGeometry(200, 100, 1600, 800)         
        self.setWindowIcon(QIcon('logo.png'))         

        self.pushButton1 = QPushButton("number of Pizza School stores")
        self.pushButton1.clicked.connect(self.pushButton1Clicked)
        self.pushButton2 = QPushButton("number of Pizza Hut stores")
        self.pushButton2.clicked.connect(self.pushButton2Clicked)
        self.pushButton3 = QPushButton("number of Domino Pizza stores")
        self.pushButton3.clicked.connect(self.pushButton3Clicked)
        

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
        rightLayout.addStretch(1)   

        layout = QHBoxLayout()
        layout.addLayout(leftLayout)
        layout.addLayout(rightLayout)
        layout.setStretchFactor(leftLayout, 1)
        layout.setStretchFactor(rightLayout, 0)  

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
    
        
    
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    mywindow = graphDialog()
    mywindow.show()
    app.exec_()