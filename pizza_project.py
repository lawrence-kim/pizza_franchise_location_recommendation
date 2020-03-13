import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import pytz as tz
import matplotlib.pyplot as plt
from datetime import datetime
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
##
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
#pyqt에 그림그리는데 필요한것!
#pyqt에 차드를 그릴때 사용
#from matplotlib.backends.backand_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import seaborn as sns
#%matplotlib nbagg
import matplotlib.pyplot as plt
import matplotlib
# 한글 폰트 문제 해결
# matplotlib는 한글폰트를 지원하지 않음
# is 정보
import platform # 맥도 똑같이 쓸수 있다.
# font_manager : 폰트관리 모듈
# rc : 폰트 변경 모듈
from matplotlib import font_manager, rc
#시각화 도구
from matplotlib import pyplot as plt
#%matplotlib inline
#%matplotlib nbagg
# uniccode 설정
plt.rcParams['axes.unicode_minus'] = False
if platform.system() == 'Darwin': #os 가 mac일때
    rc('font', family = 'AppleGothic')
elif platform.system() == 'Windows':
    path = 'C:/Windows/Fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font',family = font_name)
else:
    print("Unknown system")



class MyWindows(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        # 윈도우 Frame
        self.setWindowTitle("피자 K-Means 클러스터링")
        self.setGeometry(600,200,300,400) #(x축 좌표,y축 좌표,x축 크기,y축 크기)
        self.setWindowIcon(QIcon('f1car.jpg')) # Icon 만들기
        # 그룹박스
        groupBox = QGroupBox("클러스터링 분석하기", self)
        # groupBox.move(10, 10)
        # groupBox.resize(280, 80)
        # 라디오
        self.radio1 = QRadioButton("on", self)
        # self.radio1.move(10, 20)
        # self.radio1.clicked.connect(self.radioButtonClicked)
        self.radio2 = QRadioButton("off", self)

        if self.radio2.isChecked() == True :
            self.label4.setText("off는 지원하지 않습니다.")

        # self.radio2.move(20, 20)
        self.radio2.setChecked(True)
        # self.radio2.clicked.connect(self.radioButtonClicked)
        self.lineEdit = QLineEdit("", self)
        self.pushButton1 = QPushButton("분석하기")
        self.pushButton1.clicked.connect(self.pushButton1Clicked)
        # Figure Canvas
  

        rightlayout = QVBoxLayout()
        self.label1 = QLabel("클러스터링")
        self.label2 = QLabel("n_clusters :")
        self.label3 = QLabel("\n\n\n\n\n\n\n")
        self.label4 = QLabel("")
        rightlayout.addWidget(self.label1)
        rightlayout.addWidget(groupBox)
        rightlayout.addWidget(self.radio1)
        rightlayout.addWidget(self.radio2)
        rightlayout.addWidget(self.label2)
        rightlayout.addWidget(self.lineEdit)
        rightlayout.addWidget(self.pushButton1)
        rightlayout.addWidget(self.label3)
        rightlayout.addWidget(self.label4)
        rightlayout.addStretch(1)# 제일 상단에 배치
        layout = QHBoxLayout()
        layout.addLayout(rightlayout)
        layout.setStretchFactor(rightlayout,0) #크기 조절시 크기 변경 않됨
        # Status Bar
        # self.statusBar = QStatusBar(self)
        # self.setStatusBar(self.statusBar)
        self.setLayout(layout)
    # def radioButtonClicked(self):
    #     msg = ""
    #     if self.radio1.isChecked():
    #         msg = "일봉"
    #     else:
    #         msg = "월봉"
    #     self.statusBar.showMessage(msg + "선택 됨")
    def pushButton1Clicked(self):
        msg = ""
        n_cluster = int(self.lineEdit.text())
        print(self.lineEdit.text())

        if (self.radio1.isChecked() and n_cluster>0):
            msg = '통과'

            df = pd.read_csv('./Data/전국 상권 최종본.csv',encoding='utf-8')
            lon_min, lat_min, lon_max, lat_max = 126.261350753975, 33.2456207826882, 129.557655851988, 38.449009493943
            korea_events = df[(df['lng']>lon_min) & 
           (df['lng']<lon_max) & 
           (df['lat']>lat_min) & 
           (df['lat']<lat_max)]

           # Rule of thumb for k: sqrt(n/2); here n is 112390 - total no. of NYC events
            kmeans = KMeans(n_clusters= n_cluster, init='k-means++')

            # Compute the clusters based on longitude and latitude features
            X_sample = korea_events[['lng','lat']].sample(frac=0.1)
            kmeans.fit(X_sample)
            y = kmeans.labels_
            print("k = 800", " silhouette_score ", silhouette_score(X_sample, y, metric='euclidean'))
            korea_events['cluster'] = kmeans.predict(korea_events[['lng','lat']])
            #korea_events['new_index'] = range(len(korea_events))
            korea_events.sort_values(by='cluster', inplace=True)
            korea_events.index = range(len(korea_events))

            # 각 클러스터별 최소/최대 위도/경도 추가하기
            templist_lng = []
            templist_lat = []
            templist_lng_max = []
            templist_lng_min = []
            templist_lat_max = []
            templist_lat_min = []
            templist1 = []
            templist2 = []
            count = 0
            for i in range(len(korea_events)):
                while 1:
                    if korea_events['cluster'][i] == (count):
                        templist1.append(korea_events['lng'][i])
                        templist2.append(korea_events['lat'][i])
                        break
                    else:
                        count +=1
                        a =sum(templist1)/len(templist1)
                        b =sum(templist2)/len(templist2)
                        c = max(templist1)
                        d = min(templist1)
                        e = max(templist2)
                        f = min(templist2)
                        templist_lng.append(a)
                        templist_lat.append(b)
                        templist_lng_max.append(c)
                        templist_lng_min.append(d)
                        templist_lat_max.append(e)
                        templist_lat_min.append(f)
                        templist1 = []
                        templist2 = []
            gdf = korea_events.groupby(['cluster']).size().reset_index()
            gdf.columns = ['cluster', 'count']

            templist_count = []
            templist_count1= []
            count = 0
            for i in range(len(gdf+1)):

                while 1:
                    if gdf['cluster'][i] == (count):
                        templist_count1.append(gdf['count'][i])
                        break
                    else:
                        count +=1
                        a =sum(templist_count1)
                        templist_count.append(a)
                        templist_count1 = []
            my_dict = {'lng':templist_lng, 'lat':templist_lat, 'count':templist_count, 'max_lng':templist_lng_max, 'min_lng':templist_lng_min,
                    'max_lat':templist_lat_max,'min_lat':templist_lat_min}
            cluster_df0 = pd.DataFrame(my_dict)
            cluster_df0.index = range(len(cluster_df0))
            cluster_df0['cluster'] = range(len(cluster_df0))
            cluster_df0.to_csv("./Data/상권cluster별위치", index=False)
        
        else:
            msg = "설정 on과 클러스트를 입력 해 주세요"
        print(msg)























if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindows()
    mywindow.show()
    app.exec_()

