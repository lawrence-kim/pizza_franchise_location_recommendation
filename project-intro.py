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
    path="c:/windows/Fonts/malgun.ttf"      # font = 210 M고딕050.ttf
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

        self.pushButton1 = QPushButton("PIZZASCHOOL")
        self.pushButton1.clicked.connect(self.pushButton1Clicked)
        self.pushButton2 = QPushButton("DOMINO")
        self.pushButton2.clicked.connect(self.pushButton2Clicked)
        self.pushButton3 = QPushButton("MR.PIZZA")
        self.pushButton3.clicked.connect(self.pushButton3Clicked)
        self.pushButton4 = QPushButton("PIZZAHUT")
        self.pushButton4.clicked.connect(self.pushButton4Clicked)
        self.pushButton5 = QPushButton("PIZZAALVOLO")
        self.pushButton5.clicked.connect(self.pushButton5Clicked)
        self.pushButton6 = QPushButton("59쌀PIZZA")
        self.pushButton6.clicked.connect(self.pushButton6Clicked)
        self.pushButton7 = QPushButton("PIZZAETANG")
        self.pushButton7.clicked.connect(self.pushButton7Clicked)
        self.pushButton8 = QPushButton("PIZZAMARU")
        self.pushButton8.clicked.connect(self.pushButton8Clicked)

        self.label1 = QLabel("\n\n\n\n\n\n\n\n\n\n")
        
        # Figure Canvas
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)

        topLayout = QGridLayout()
        topLayout.addWidget(self.pushButton1, 0, 0)
        topLayout.addWidget(self.pushButton2, 0, 1)
        topLayout.addWidget(self.pushButton3, 0, 2)
        topLayout.addWidget(self.pushButton4, 0, 3)
        topLayout.addWidget(self.pushButton5, 1, 0)
        topLayout.addWidget(self.pushButton6, 1, 1)
        topLayout.addWidget(self.pushButton7, 1, 2)
        topLayout.addWidget(self.pushButton8, 1, 3)

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

    def pushButton3Clicked(self) :
        self.label1.setText("""
        미스터피자(Mr. Pizza)는 대한민국의 MP그룹이 운영하는 피자 전문 외식브랜드이다.\n
        미스터피자는 여성들이 선호하는 취향의 메뉴를 개발하여, 피자의 주된 소비층인 \n
        20대~30대 여성에게 특히 인기가 높아 더욱 성장할 수 있었고, \n
        2008년~2009년을 기점으로 피자헛과 도미노피자를 제치고 대한민국의 1등 피자 전문 브랜드로 자리 잡았다.\n
        국내 피자 업계에서 무너지지 않을 것 같던 피자헛을 위협하고 있으며 여성 중심의 마케팅과 \n
        다른 피자 브랜드에는 없는 독특한 프리미엄 피자들을 판매하는데, 2000년대 중후반 웰빙 바람을 타고 급성장하였다.\n
        2019년 7월 현재 전국 267개의 매장을 운영하고 있으며, 부산에는 14개의 매장이 있다.\n""")
        
    def pushButton4Clicked(self) :
        self.label1.setText("""
        피자헛(Pizza Hut)은 미국의 피자 프랜차이즈이다.\n
        현재 100여 개국 이상에 피자헛 점포를 두고 있으며, 일부 점포에서는 고객이 직접 와서 피자헛 제품을 먹거나 \n
        테이크아웃을 할 수 있는 피자헛 레스토랑이기도 한다.\n
        대한민국에서는 2019년 7월 현재 전국 348개의 매장을 운영하고 있으며, 부산에는 24개의 매장이 있다.\n""")

    def pushButton5Clicked(self) :
        self.label1.setText("""
        호텔 조리학과를 수료한 이재욱, 이재원 형제가 2005년 목동에 처음 1호점을 개업.\n
        알볼로는 이탈리아어로 비행, 비상이라는 단어.\n
        '라이트 형제가 하늘의 문을 열었던 것처럼 피자로 새로운 세상의 문을 열겠다'라는 의미에서 명명했다고 한다.\n
        컨셉을 '마케팅과 이벤트에 쏟을 비용을 재료에 돌려서 푸짐하게 피자를 만들자'로 잡고 영업을 개시했는데, \n
        이게 생각 이상으로 대박이 나서 2006년부터 여러 TV프로그램에 소개되면서 인지도가 크게 높아지게 되고 \n
        그 결과 작은 가게에서 브랜드 기업으로 성장.\n
        이렇게 마케팅에 투자하지 않는 대신 브랜드에서 주장하는대로 재료에 투자한다는게 허언이 아닌지, \n
        토핑이 굉장히 실하게 올라오는 것으로 유명하다.\n
        다른 피자 브랜드에서 치즈 추가+토핑 추가를 신청해야 볼 수 있는 퀄리티가 기본적으로 보장되며, \n
        모 피자 커뮤니티에서는 전단지에 나와있는 사진과 실물이 일치하는 유일한 브랜드라고도 언급되기도 한다.\n
        2019년 7월 현재 전국 283개의 매장을 운영하고 있으며, 부산에는 14개의 매장이 있다.\n""")

    def pushButton6Clicked(self) :
        self.label1.setText("""
        테이크아웃을 전문으로 하는 중저가 피자 브랜드의 하나.\n
        59피자라는 명칭은 가장 기본적이며 저렴한 콤비네이션 피자가 5900원인 것에서 유래하였으며, \n
        광고 카피인 '맛있어서 오구, 생각나서 오구' 역시 여기에서 나왔다. \n
        2006년 5월에 프랜차이즈 설립 후 2011년 5월에 가맹점 500호를 돌파하였다.\n
        국산 쌀과 보리, 조, 밀에 검은깨를 첨가한 소위 오곡 웰빙 도우 사용을 표방하고 있으며, \n
        꽤나 다양한 토핑을 고를 수 있고 치즈 크러스트나 고구마 무스 유무를 선택할 수 있는 등 \n
        선택의 폭은 어지간한 대형 프랜차이즈 못지 않은 편.\n
        물론 이렇게 여러가지를 추가하면 값이 어느 정도 올라가지만 그래도 대체로 라지 기준 \n
        8천원에서 1만 2천원대의 가격으로 일반적인 프랜차이즈에 비하면 무진장 저렴한 축에 속한다.\n
        2019년 7월 현재 전국 581개의 매장을 운영하고 있으며, 부산에는 5개의 매장이 있다.\n""")

    def pushButton7Clicked(self) :
        self.label1.setText("""
        주식회사 에땅이 운영하는 피자 체인점.\n
        에땅은 프랑스어로 호수,연못을 뜻하는 etang인데, 홈페이지에 따르면 \n
        이탈리아에서 프랑스로 이민간 세르지오 가문이 틀루스 시에서 피자를 팔았는데 \n
        사람들이 근처 호숫가에서 먹으면서 pizza etang이라고 부른 데에서 유래했다고 한다.\n
        고급 브랜드 피자 한 판 가격이면 두 판을 먹을 수 있다는 1+1 광고로 유명하듯 \n
        고급 피자 브랜드라기 보단 배달서비스가 가능한 중저가브랜드 이다.\n
        질보단 양을 추구하는 사람들에게는 나름 적절한 아이템.\n
        2019년 7월 현재 전국 261개의 매장을 운영하고 있으며, 부산에는 33개의 매장이 있다.\n""")


    def pushButton8Clicked(self) :
        self.label1.setText("""
        테이크아웃 피자 브랜드. 피자스쿨과 비슷하다.\n
        피자스쿨보다 가격이 비싼 편이다.\n
        대체로 피자스쿨보다 1,000원~2000원씩 더 높다.\n
        그 대신 피자스쿨에 비해 약간 더 크고 토핑이 풍성한 편.\n
        피자스쿨과는 달리 핫소스와 치즈 가루 등이 기본 제공된다.\n
        2019년 7월 현재 전국 652개의 매장을 운영하고 있으며, 부산에는 20개의 매장이 있다.\n""")

        
    
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    mywindow = machineLearingDialog()
    mywindow.show()
    app.exec_()