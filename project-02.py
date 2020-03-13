import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *       # 종료하는 것은 widget만으로 안됨. 추가적으로 import 해줘야 함
from PyQt5.QtGui import *

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import seaborn as sns
import urllib.request
import json
import bs4
import locale
from locale import atof  
from matplotlib import rcParams, style
from matplotlib import cm, colors, _cm

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QBoxLayout

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

import platform
from matplotlib import font_manager,rc
import matplotlib as mpl

import time

if platform.system() == "Darwin" :    #Darwin은 MAC OS
    rc('font', family = 'AppleGothic')
elif platform.system() == 'Windows' :
    path="c:/windows/Fonts/malgun.ttf"      # 210 M고딕050.ttf
    font_name = font_manager.FontProperties(fname = path).get_name()
    rc('font', family = font_name)
else :
    print("Unknown System")


# 시각화 자료 그리기

class visualialog(QDialog) :
    def __init__(self) :
        super().__init__()
        self.setupUI()

    def setupUI(self) :
        # 윈도우 frame
        self.setWindowTitle("VISUALIZATION")
        self.setGeometry(300, 70, 1300, 800)                # (x축 좌표, y축 좌표, x축 크기, y축 크기)
        self.setWindowIcon(QIcon('logo.png'))          # 왼쪽 상단에 icon 넣기

        self.pushButton15 = QPushButton("KOREA SINGLES RATIO")
        self.pushButton15.clicked.connect(self.pushButton15Clicked)
        self.pushButton16 = QPushButton("PIZZASCHOOL STORE COUNT")
        self.pushButton16.clicked.connect(self.pushButton16Clicked)

        self.pushButton1 = QPushButton("PIZZA INDEX")
        self.pushButton1.clicked.connect(self.pushButton1Clicked)
        self.pushButton2 = QPushButton("→ VISUALIZATION")
        self.pushButton2.clicked.connect(self.pushButton2Clicked)
        self.pushButton3 = QPushButton("DOMINO")
        self.pushButton3.clicked.connect(self.pushButton3Clicked)
        self.pushButton4 = QPushButton("→ VISUALIZATION")
        self.pushButton4.clicked.connect(self.pushButton4Clicked)
        self.pushButton5 = QPushButton("MR.PIZZA")
        self.pushButton5.clicked.connect(self.pushButton5Clicked)
        self.pushButton6 = QPushButton("→ VISUALIZATION")
        self.pushButton6.clicked.connect(self.pushButton6Clicked)
        self.pushButton7 = QPushButton("PIZZAHUT")
        self.pushButton7.clicked.connect(self.pushButton7Clicked)
        self.pushButton8 = QPushButton("→ VISUALIZATION")
        self.pushButton8.clicked.connect(self.pushButton8Clicked)
        self.pushButton9 = QPushButton("PIZZASCHOOL")
        self.pushButton9.clicked.connect(self.pushButton9Clicked)
        self.pushButton10 = QPushButton("→ VISUALIZATION")
        self.pushButton10.clicked.connect(self.pushButton10Clicked)
        self.pushButton11 = QPushButton("ALL PIZZA BRAND")
        self.pushButton11.clicked.connect(self.pushButton11Clicked)
        self.pushButton12 = QPushButton("→ VISUALIZATION")
        self.pushButton12.clicked.connect(self.pushButton12Clicked)
        self.labelDone = QLabel("")
        self.label1 = QLabel("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        self.label2 = QLabel("\n\n\n\n\n\n\n")
        #self.labelintro1 = QLabel("")
        
        # Left Layout
        global leftLayout
        leftLayout = QVBoxLayout()

        # Right Layout
        rightLayout = QVBoxLayout()

        righttopLayout = QVBoxLayout()
        rightmidLayout = QGridLayout()
        rightbottomLayout = QVBoxLayout()

        righttopLayout.addWidget(self.label2)
        righttopLayout.addWidget(self.pushButton15)
        righttopLayout.addWidget(self.pushButton16)

        rightmidLayout.addWidget(self.pushButton1, 0, 0)
        rightmidLayout.addWidget(self.pushButton2, 0, 1)
        rightmidLayout.addWidget(self.pushButton3, 1, 0)
        rightmidLayout.addWidget(self.pushButton4, 1, 1)
        rightmidLayout.addWidget(self.pushButton5, 2, 0)
        rightmidLayout.addWidget(self.pushButton6, 2, 1)
        rightmidLayout.addWidget(self.pushButton7, 3, 0)
        rightmidLayout.addWidget(self.pushButton8, 3, 1)
        rightmidLayout.addWidget(self.pushButton9, 4, 0)
        rightmidLayout.addWidget(self.pushButton10, 4, 1)
        rightmidLayout.addWidget(self.pushButton11, 5, 0)
        rightmidLayout.addWidget(self.pushButton12, 5, 1)
        #rightmidLayout.addWidget(self.labelDone, 7, 0)

        rightbottomLayout.addWidget(self.label1)
        rightbottomLayout.addWidget(self.labelDone)


        rightLayout.addLayout(righttopLayout)
        rightLayout.addLayout(rightmidLayout)
        rightLayout.addLayout(rightbottomLayout)
        #rightLayout.addStretch(1)   # 제일 상단에 배치

        # Layout : V Layout 2개를 나란히 붙이려면 H Layout을 사용해야함
        layout = QHBoxLayout()
        layout.addLayout(leftLayout)
        layout.addLayout(rightLayout)
        layout.setStretchFactor(leftLayout, 1)
        layout.setStretchFactor(rightLayout, 0)  # 0은 크기 조절시 크기 변경 안됨

        self.setLayout(layout)


    def pushButton15Clicked(self) :
        web = QWebEngineView()
        web.setUrl(QUrl("./Data/map1.html"))
        leftLayout.addWidget(web)
        for i in range(leftLayout.count()):
            leftLayout.itemAt(i).widget().close()
        self.labelDone.setText("전국 1인 가구 비율")

    
    def pushButton16Clicked(self) :
        web = QWebEngineView()
        web.setUrl(QUrl("./Data/map2.html"))
        leftLayout.addWidget(web)
        for i in range(leftLayout.count()):
            leftLayout.itemAt(i).widget().close()
        self.labelDone.setText("전국 피자스쿨 점포수")


    def pushButton1Clicked(self) : # 피자지수
        pizza = pd.read_csv("./Data/pizza_all_count.csv")
        pizza_sales = pd.read_csv("./Data/pizza_sales.csv")
        pizza.index = pizza.apply(lambda r : r['city'] + ' ' + r['district'], axis = 1)

        tmp = pd.read_excel("./Data/인구_서울특별시.xlsx", usecols=[0,1], names=["d1d2d3", "population"])
        tmp['d1'], tmp['d2d3'] = tmp['d1d2d3'].str.split(' ', 1).str
        tmp['d2'], tmp['d3'] = tmp['d2d3'].str.split(' ', 1).str
        tmp = tmp[3:]
        district = pd.DataFrame({'d1': tmp.d1, 'd2': tmp.d2, 'd3': tmp.d3, 'population': tmp.population})

        def get_distDF(loc):
            filename = "./Data/인구_" + loc + ".xlsx"
            tmp = pd.read_excel(filename, usecols=[0,1], names=["d1d2d3", "population"])
            tmp['d1'], tmp['d2d3'] = tmp['d1d2d3'].str.split(' ', 1).str
            tmp['d2'], tmp['d3'] = tmp['d2d3'].str.split(' ', 1).str
            tmp = tmp[3:]
            dist = pd.DataFrame({'d1': tmp.d1, 'd2': tmp.d2, 'd3': tmp.d3, 'population': tmp.population})
            return dist

        locs = ["강원도", "경기도", "경상남도", "경상북도", "광주광역시", "대구광역시", "대전광역시", "부산광역시", "세종특별자치시", "울산광역시", "인천광역시", "전라남도", "전라북도", "제주특별자치도", "충청남도", "충청북도"]
        for loc in locs:
            district = district.append(get_distDF(loc), ignore_index=True)

        district.index = district.apply(lambda r: r['d1'] + ' ' + r['d2'], axis=1)
        district = district[district['d3'].str.startswith("(")]

        pizza_complete = pd.merge(district, pizza, how = 'outer', left_index = True, right_index = True)
        pizza_complete = pizza_complete[['city', 'district', 'd3', 'population', 'domino', 'pizza_hut', 'pizza_school', 'mr_pizza', 'total']]
        pizza_complete.rename(columns = { 'domino': 'D', 'pizza_hut': 'H', 'pizza_school' : 'S', 'mr_pizza' : 'M'}, inplace = True)

        pizza_complete.loc[pizza_complete['total'].isnull(), 'total'] = 0.0

        # NaN값 0으로 대체하기
        pizza_complete['D'].fillna(0, inplace = True)
        pizza_complete['H'].fillna(0, inplace = True)
        pizza_complete['S'].fillna(0, inplace = True)
        pizza_complete['M'].fillna(0, inplace = True)
        pizza_complete['total'].fillna(0, inplace = True)

        # float값 int로 변경
        pizza_complete['D'] = pizza_complete['D'].apply(lambda x : int(x))
        pizza_complete['H'] = pizza_complete['H'].apply(lambda x : int(x))
        pizza_complete['S'] = pizza_complete['S'].apply(lambda x : int(x))
        pizza_complete['M'] = pizza_complete['M'].apply(lambda x : int(x))
        pizza_complete['total'] = pizza_complete['total'].apply(lambda x : int(x))

        # 새로운 값 만들기
        pizza_complete['DHM'] = pizza_complete['D'] + pizza_complete['H'] + pizza_complete['M']
        pizza_complete['total'] = pizza_complete['DHM'] + pizza_complete['S']

        pizza_complete['PizzaIdx'] = (pizza_complete['DHM'] + 1) / (pizza_complete['S'] + 1)

        def short_distr(name):
            wide, narrow = name.split()
            if narrow == '세종특별자치시': 
                return '세종'
            elif wide.endswith('광역시'):
                return wide[:2] + (narrow[:-1] if len(narrow) > 2 else narrow)
            elif narrow.endswith('구'):
                return wide[:2] + (narrow[:-1] if len(narrow) > 2 else narrow)
            elif narrow == '고성군': # 고성군은 강원도, 경상남도에 있다.
                return '고성({})'.format({'강원도': '강원', '경상남도': '경남'}[wide])
            else:
                return narrow[:-1]

        pizza_complete['shortname'] = list(map(short_distr, pizza_complete.index))

        #blockpositions = pd.read_excel('./Data/block_map.xlsx', header=None, usecols=range(15))
        blockpositions = pd.read_csv("./Data/block_map.csv", encoding = 'euc-kr', header=None)

        flatrows = []
        for y, colcities in blockpositions.iterrows():
            for x, city in colcities.iteritems():
                if isinstance(city, str):   
                    flatrows.append((x, y, city))

        blockpositions_tbl = pd.DataFrame(flatrows, columns=('x', 'y', 'city')).set_index('city').sort_index()
        pizzab = pd.merge(pizza_complete, blockpositions_tbl, how='left', left_on='shortname', right_index=True)


        locale.setlocale(locale.LC_NUMERIC, '')
        pizzab['population'] = pizzab['population'].apply(atof)

        matplotlib.rcParams['font.family'] = ['NanumGothic']

        BORDER_LINES = [
            [(3, 2), (5, 2), (5, 3), (9, 3), (9, 1)], # 인천
            [(2, 5), (3, 5), (3, 4), (8, 4), (8, 7), (7, 7), (7, 9), (4, 9), (4, 7), (1, 7)], # 서울
            [(1, 6), (1, 9), (3, 9), (3, 10), (8, 10), (8, 9),
            (9, 9), (9, 8), (10, 8), (10, 5), (9, 5), (9, 3)], # 경기도
            [(9, 12), (9, 10), (8, 10)], # 강원도
            [(10, 5), (11, 5), (11, 4), (12, 4), (12, 5), (13, 5),
            (13, 4), (14, 4), (14, 2)], # 충청남도
            [(11, 5), (12, 5), (12, 6), (15, 6), (15, 7), (13, 7),
            (13, 8), (11, 8), (11, 9), (10, 9), (10, 8)], # 충청북도
            [(14, 4), (15, 4), (15, 6)], # 대전시
            [(14, 7), (14, 9), (13, 9), (13, 11), (13, 13)], # 경상북도
            [(14, 8), (16, 8), (16, 10), (15, 10),
            (15, 11), (14, 11), (14, 12), (13, 12)], # 대구시
            [(15, 11), (16, 11), (16, 13)], # 울산시
            [(17, 1), (17, 3), (18, 3), (18, 6), (15, 6)], # 전라북도
            [(19, 2), (19, 4), (21, 4), (21, 3), (22, 3), (22, 2), (19, 2)], # 광주시
            [(18, 5), (20, 5), (20, 6)], # 전라남도
            [(16, 9), (18, 9), (18, 8), (19, 8), (19, 9), (20, 9), (20, 10)], # 부산시
        ]

        # city, district NaN값 index에서 추출해서 대체하기
        cities = []
        districts = []
        for i in range(len(pizzab[pizzab['district'].isnull()])) :
            #pizzab.loc[pizzab['district'].isnull(), 'city'][i] = pizzab[pizzab['district'].isnull()].index[i].split()[0]
            #pizzab.loc[pizzab['district'].isnull(), 'district'][i] = pizzab[pizzab['district'].isnull()].index[i].split()[1]
            cities.append(pizzab[pizzab['district'].isnull()].index[i].split()[0])
            districts.append(pizzab[pizzab['district'].isnull()].index[i].split()[1])

        # list로 만들어서 대체
        pizzab.loc[pizzab['district'].isnull(), 'city'] = cities
        pizzab.loc[pizzab['district'].isnull(), 'district'] = districts

        tbl = pizzab
        datacol = 'PizzaIdx'
        vmin = 0
        vmax = 3
        whitelabelmin = 2.0
        cmap = 'Blues'
        gamma = 0.75
        datalabel = '피자지수'
        dataticks = np.arange(0, 5.1, 1)
        title = "피자지수"
        suptitle = "(도미노 + 미스터피자 + 피자헛) \n/ 피자스쿨"

        fig = plt.figure(figsize=(10, 18))
        fig.patch.set_facecolor('xkcd:white')

        mapdata = pd.pivot_table(tbl, index='y', columns='x', values=datacol)
        masked_mapdata = np.ma.masked_where(np.isnan(mapdata), mapdata)        

        plt.pcolor(masked_mapdata.astype(float), vmin=vmin, vmax=vmax, cmap=cmap,
                edgecolor='#aaaaaa', linewidth=0.5)

        # 지역 이름 표시
        for idx, row in tbl.iterrows():
            # 광역시는 구 이름이 겹치는 경우가 많아서 시단위 이름도 같이 표시한다. (중구, 서구)
            if row['city'].endswith('시') and not row['city'].startswith('세종'):
                dispname = '{}\n{}'.format(row['city'][:2], row['district'][:-1])
                if len(row['district']) <= 2:
                    dispname += row['district'][-1]
            elif row["city"]=="세종특별자치시":
                dispname = "세종"
            else:
                dispname = row['district'][:-1]

            # 서대문구, 서귀포시 같이 이름이 3자 이상인 경우에 작은 글자로 표시한다.
            if len(dispname.splitlines()[-1]) >= 3:
                fontsize, linespacing = 11, 1.2
            else:
                fontsize, linespacing = 13, 1.03

            annocolor = 'white' if row[datacol] > whitelabelmin else 'black'
            if row['total'] == 0 :
                annocolor = 'red'  # data가 없는 경우에는 red color로 표시해주기

            plt.annotate(dispname, (row['x']+0.5, row['y']+0.5), weight='bold',
                        fontsize=fontsize, ha='center', va='center', color=annocolor,
                        linespacing=linespacing)
            
        # 시도 경계 그린다.
        for path in BORDER_LINES:
            ys, xs = zip(*path)
            plt.plot(xs, ys, c='black', lw=1.8)

        plt.gca().invert_yaxis()
        plt.gca().set_aspect(1)

        plt.axis('off')  # plot의 x축 y축 안보이게

        cb = plt.colorbar(shrink=.1, aspect=10)
        cb.set_label(datalabel)
        cb.set_ticks(dataticks)

        plt.tight_layout()
        plt.title(title, fontsize = 25, position=(0.15, 0.96))
        plt.suptitle(suptitle, fontsize=13, position=(0.18, 0.87))
        plt.savefig("./Data/visulize.jpg")
        self.labelDone.setText("피자 지수 시각화 완료 되었습니다.")

    def pushButton2Clicked(self) :
        web = QWebEngineView()
        web.setUrl(QUrl("./Data/visulize.jpg"))
        leftLayout.addWidget(web)
        for i in range(leftLayout.count()):
            leftLayout.itemAt(i).widget().close()
        
    def pushButton3Clicked(self) : # 도미노 점포수
        time.sleep(2)
        self.labelDone.setText("도미노 피자 점포 시각화 완료 되었습니다.")

    def pushButton4Clicked(self) :
        web = QWebEngineView()
        web.setUrl(QUrl("./Data/도미노피자점포수 - 복사본.jpg"))
        leftLayout.addWidget(web)
        for i in range(leftLayout.count()):
            leftLayout.itemAt(i).widget().close()

    def pushButton5Clicked(self) : # 미스터 점포수
        time.sleep(2)
        self.labelDone.setText("미스터 피자 점포 시각화 완료 되었습니다.")

    def pushButton6Clicked(self) :
        web = QWebEngineView()
        web.setUrl(QUrl("./Data/미스터피자점포수 - 복사본.jpg"))
        leftLayout.addWidget(web)
        for i in range(leftLayout.count()):
            leftLayout.itemAt(i).widget().close()

    def pushButton7Clicked(self) : # 피자헛 점포수
        time.sleep(2)
        self.labelDone.setText("피자헛 점포 시각화 완료 되었습니다.")

    def pushButton8Clicked(self) :
        web = QWebEngineView()
        web.setUrl(QUrl("./Data/피자헛점포수 - 복사본.jpg"))
        leftLayout.addWidget(web)
        for i in range(leftLayout.count()):
            leftLayout.itemAt(i).widget().close()

    def pushButton9Clicked(self) : # 피자헛 점포수
        time.sleep(2)
        self.labelDone.setText("피자스쿨 점포 시각화 완료 되었습니다.")

    def pushButton10Clicked(self) :
        web = QWebEngineView()
        web.setUrl(QUrl("./Data/피자스쿨점포수 - 복사본.jpg"))
        leftLayout.addWidget(web)
        for i in range(leftLayout.count()):
            leftLayout.itemAt(i).widget().close()

    def pushButton11Clicked(self) : # 피자헛 점포수
        time.sleep(2)
        self.labelDone.setText("피자 점포 시각화 완료 되었습니다.")

    def pushButton12Clicked(self) :
        web = QWebEngineView()
        web.setUrl(QUrl("./Data/피자점포수.jpg"))
        leftLayout.addWidget(web)
        for i in range(leftLayout.count()):
            leftLayout.itemAt(i).widget().close()

class Image1(QDialog):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.setGeometry(300, 100, 600, 900)
        self.form_layout = QBoxLayout(QBoxLayout.LeftToRight, self)
        self.setLayout(self.form_layout)
        self.init_widget()

    def init_widget(self):
        self.setWindowTitle("QWebEngineView")
        web = QWebEngineView()
        web.setUrl(QUrl("./Data/피자지수_.jpg"))
        self.form_layout.addWidget(web)

class Image2(QDialog):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.setGeometry(300, 100, 600, 900)
        self.form_layout = QBoxLayout(QBoxLayout.LeftToRight, self)
        self.setLayout(self.form_layout)
        self.init_widget()

    def init_widget(self):
        self.setWindowTitle("QWebEngineView")
        web = QWebEngineView()
        web.setUrl(QUrl("./Data/도미노피자점포수 - 복사본.jpg"))
        self.form_layout.addWidget(web)

class Image3(QDialog):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.setGeometry(300, 100, 600, 900)
        self.form_layout = QBoxLayout(QBoxLayout.LeftToRight, self)
        self.setLayout(self.form_layout)
        self.init_widget()

    def init_widget(self):
        self.setWindowTitle("QWebEngineView")
        web = QWebEngineView()
        web.setUrl(QUrl("./Data/미스터피자점포수 - 복사본.jpg"))
        self.form_layout.addWidget(web)

class Image4(QDialog):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.setGeometry(300, 100, 600, 900)
        self.form_layout = QBoxLayout(QBoxLayout.LeftToRight, self)
        self.setLayout(self.form_layout)
        self.init_widget()

    def init_widget(self):
        self.setWindowTitle("QWebEngineView")
        web = QWebEngineView()
        web.setUrl(QUrl("./Data/피자헛점포수 - 복사본.jpg"))
        self.form_layout.addWidget(web)

class Image5(QDialog):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.setGeometry(300, 100, 600, 900)
        self.form_layout = QBoxLayout(QBoxLayout.LeftToRight, self)
        self.setLayout(self.form_layout)
        self.init_widget()

    def init_widget(self):
        self.setWindowTitle("QWebEngineView")
        web = QWebEngineView()
        web.setUrl(QUrl("./Data/피자스쿨점포수 - 복사본.jpg"))
        self.form_layout.addWidget(web)

class Image6(QDialog):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.setGeometry(300, 100, 600, 900)
        self.form_layout = QBoxLayout(QBoxLayout.LeftToRight, self)
        self.setLayout(self.form_layout)
        self.init_widget()

    def init_widget(self):
        self.setWindowTitle("QWebEngineView")
        web = QWebEngineView()
        web.setUrl(QUrl("./Data/피자점포수.jpg"))
        self.form_layout.addWidget(web)

class visual_2_Dialog(QDialog) :
    def __init__(self) :
        super().__init__()
        self.setupUI()
        #self.filename = None

    def setupUI(self) :
        # 윈도우 frame
        self.setWindowTitle("Chart")
        self.setGeometry(800, 100, 900, 1000)                # (x축 좌표, y축 좌표, x축 크기, y축 크기)
        self.setWindowIcon(QIcon('light.png'))          # 왼쪽 상단에 icon 넣기

        self.lbl = QLabel(self)
        self.lbl.resize(800,1000)
        pixmap = QPixmap("./Data/visulize.jpg")
        pixmap = pixmap.scaledToHeight(1000)
        self.lbl.setPixmap(QPixmap(pixmap))

        self.resize(800,1000)
        self.show()




















class Map1(QDialog):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.setGeometry(300, 300, 1100, 600)
        self.form_layout = QBoxLayout(QBoxLayout.LeftToRight, self)
        self.setLayout(self.form_layout)
        self.init_widget()

    def init_widget(self):
        self.setWindowTitle("QWebEngineView")
        web = QWebEngineView()
        web.setUrl(QUrl("C:/JIN/BigData/workSpace/Data/map1.html"))
        
        self.form_layout.addWidget(web)
        #leftLayout.addWidget(self.form_layout)

class Map2(QDialog):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.setGeometry(300, 300, 1100, 600)
        self.form_layout = QBoxLayout(QBoxLayout.LeftToRight, self)
        self.setLayout(self.form_layout)
        self.init_widget()

    def init_widget(self):
        self.setWindowTitle("QWebEngineView")
        web = QWebEngineView()
        web.setUrl(QUrl("D:/JIN/BigData/workSpace/Data/map2.html"))
        self.form_layout.addWidget(web)

class mywindows(QWidget) :
    def __init__(self) :
        super().__init__()
        self.setupUI()

    def setupUI(self) :
        # 윈도우 frame
        self.setWindowTitle("project-02")
        self.setGeometry(800, 200, 300, 300)                # (x축 좌표, y축 좌표, x축 크기, y축 크기)
        self.setWindowIcon(QIcon('light.png'))          # 왼쪽 상단에 icon 넣기
        
        self.pushButton = QPushButton('visualize')  # Button, layout생성해서 사용할 때는 self 없이
        self.pushButton.clicked.connect(self.pushButtonClicked)
        self.label = QLabel()

        # Layout 생성
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.pushButton)
        self.setLayout(layout)
    
    def pushButtonClicked(self) :
        dlg = visualialog()        
        dlg.exec_()
        
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    mywindow = visualialog()
    mywindow.show()
    app.exec_()