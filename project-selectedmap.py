# 이제 데이터 받는거 한다.
import sys
from PyQt5.QtWidgets import *

from PyQt5.QtCore import*
from PyQt5.QtGui import *
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd


from bs4 import BeautifulSoup
import urllib.request as req
import pymysql
from sqlalchemy import create_engine

from sklearn.tree import DecisionTreeClassifier #살았냐 죽었냐 객관식이기 때문에 Classifier 
                                                 # 주관식 우리 회사의 상품이 몇개 팔릴까?? Regressor 이다.
from sklearn.model_selection import train_test_split
from sklearn import metrics

from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QBoxLayout

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

import folium
from folium import plugins
import os

import json
import math
from haversine import haversine

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

class myWindows(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()
        
        #self.location = None
        

    def setupUI(self):
        # 윈도우 Frame
        self.setWindowTitle("지도창")
        self.setGeometry(700,250,1200,700) #(x축 좌표,y축 좌표,x축 크기,y축 크기)
        #self.setWindowIcon(QIcon('f1car.jpg')) # Icon 만들기

        #right로 가겠지!!!!!!!!
        #self.label1 = QLabel("◎ 피자브랜드 선택 ")
        
        
        # 그룹박스
        groupBox = QGroupBox("클러스터링 분석하기", self)
        
        # 라디오
        self.radio1 = QRadioButton("on", self)
       
        self.radio2 = QRadioButton("off", self)
        
        self.radio2.setChecked(True)
        
        self.lineEdit = QLineEdit("", self)
        self.pushButton1 = QPushButton("분석하기")
        self.pushButton1.clicked.connect(self.pushButton1Clicked)
        
        
        self.label3 = QLabel("◎ 지역 입력 : ")
        
        #global lineEdit1
        self.lineEdit1 = QLineEdit()
        
        
        self.pushButton = QPushButton("지도보기")
        self.pushButton.clicked.connect(self.checkBox)
        
        # Figure Canvas
        # self.fig = plt.Figure()
        # self.canvas = FigureCanvas(self.fig)

        
        
        
        #Left Layout
        global leftlayout
        leftlayout = QVBoxLayout()
        #leftlayout.addWidget(self.canvas)

        #Right Layout        
        rightlayout = QVBoxLayout()
        #rightlayout.addWidget(self.label1,0,0)
        
        self.label1 = QLabel("클러스터링")
        self.label2 = QLabel("n_clusters :")

        rightlayout.addWidget(self.label1)
        rightlayout.addWidget(groupBox)
        rightlayout.addWidget(self.radio1)
        rightlayout.addWidget(self.radio2)
        rightlayout.addWidget(self.label2)
        rightlayout.addWidget(self.lineEdit)
        rightlayout.addWidget(self.pushButton1)
        self.textLabel2 = QLabel()
        self.textLabel3 = QLabel("\n\n")
        rightlayout.addWidget(self.textLabel2)
        rightlayout.addWidget(self.textLabel3)

        rightlayout.addWidget(self.label3)
        rightlayout.addWidget(self.lineEdit1)
        rightlayout.addWidget(self.pushButton)
        rightlayout.addStretch(1)# 제일 상단에 배치
        
        
        
        layout = QHBoxLayout()
        layout.addLayout(leftlayout)
        layout.addLayout(rightlayout)
        layout.setStretchFactor(leftlayout,1)
        layout.setStretchFactor(rightlayout,0)
        self.setLayout(layout)

        

    # def pushButtonClicked(self):
    #     self.location = self.lineEdit1.text()
        
        #self.close()


    def pushButton1Clicked(self):
        msg = ""
        n_cluster = int(self.lineEdit.text())
        print(self.lineEdit.text())

        if (self.radio1.isChecked() and n_cluster>0):
            msg = '통과'
            self.textLabel2.setText("통과")

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
            self.textLabel2.setText("k = 800"+" silhouette_score "+str(silhouette_score(X_sample, y, metric='euclidean')))  

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
            cluster_df0.to_csv("./Data/상권cluster별위치2.csv", index=False, encoding='utf-8')
        
        else:
            msg = "설정 on과 클러스트를 입력 해 주세요"
        print(msg)
        self.textLabel2.setText(msg)




        

    def checkBox(self):
        self.location = self.lineEdit1.text()
        c_d = self.location
        domino = pd.read_csv("./Data/domino_population.csv")
        pizza_school = pd.read_csv("./Data/pizzaschool_populationComplete.csv")
        pizza_hut = pd.read_csv("./Data/pizza_hut_address_complete.csv")
        mr_pizza = pd.read_csv("./Data/mrpizza_complete_complete.csv")

        busan_pizza = pd.read_csv("./Data/busan_pizza.csv")
        pizza_alvolo=busan_pizza[busan_pizza['브랜드']=='피자알볼로']
        pizza_59ssal=busan_pizza[busan_pizza['브랜드']=='오구쌀피자']
        pizza_ddang=busan_pizza[busan_pizza['브랜드']=='피자에땅']
        pizza_maru=busan_pizza[busan_pizza['브랜드']=='피자마루']



            
        #cluster_df = pd.read_csv("./Data/cluster_df.csv")
        cluster_df0 = pd.read_csv("./Data/상권cluster별위치2.csv")
                #c_d = '충청북도 충주시'
        c_d_r = ''.join(c_d.split())
        pizza_hut_input=pizza_hut[pizza_hut['city_district'].str.contains(c_d_r)]
        mr_pizza_input=mr_pizza[mr_pizza['city_district'].str.contains(c_d_r)]
        pizza_school_input=pizza_school[pizza_school['city_district'].str.contains(c_d_r)]
        domino_input=domino[domino['city_district'].str.contains(c_d_r)]
                
        state_geo = './Data/TL_SCCO_SIG_WGS84.json'
        state_apart = './Data/korea_apart_decoded2.csv'
        state_data = pd.read_csv(state_apart, encoding = 'utf-8')

                # Initialize the map:
        c_d_lat=pizza_school_input['lat']
        c_d_lat=c_d_lat[c_d_lat.index[0]]
                
        c_d_lng=pizza_school_input['lng']
        c_d_lng=c_d_lng[c_d_lng.index[0]]

        m = folium.Map(location=[c_d_lat, c_d_lng],  zoom_start=12)

        m.choropleth(
        geo_data=state_geo,
        name='평당 매매가',
        data=state_data,
        columns=['Code', '평당 매매가'],
        key_on='feature.properties.SIG_CD',
        fill_color='YlGn',
        fill_opacity=0.7,
        line_opacity=0.5,
        legend_name='평당가격'
        )        

        #folium.LayerControl().add_to(m)

        #cluster_df['log_count']=np.log1p(cluster_df['count'])



        mcg = folium.plugins.MarkerCluster(control=False)
        m.add_child(mcg)
            
        g0 = plugins.FeatureGroupSubGroup(m, 'K-Means Cluster')
        m.add_child(g0)

        g1 = plugins.FeatureGroupSubGroup(m, "DOMINO")
        m.add_child(g1)

        g2 = plugins.FeatureGroupSubGroup(m, 'PIZZAHUT')
        m.add_child(g2)

        g3 = plugins.FeatureGroupSubGroup(m, 'Mr.Pizza')
        m.add_child(g3)

        g4 = plugins.FeatureGroupSubGroup(m, 'PIZZASCHOOL')
        m.add_child(g4)

        g5 = plugins.FeatureGroupSubGroup(m, 'PIZZAALVOLO')
        m.add_child(g5)

        g6 = plugins.FeatureGroupSubGroup(m, '59쌀PIZZA')
        m.add_child(g6)

        g7 = plugins.FeatureGroupSubGroup(m, 'PIZZAETANG')
        m.add_child(g7)

        g8 = plugins.FeatureGroupSubGroup(m, 'PIZZAMARU')
        m.add_child(g8)
                    


                
        #Circle        
        area_list = []
        for n in range(len(cluster_df0)):
                    point1 = cluster_df0['max_lat'][n], cluster_df0['max_lng'][n]
                    point2 = cluster_df0['min_lat'][n], cluster_df0['min_lng'][n]
                    distance= haversine(point1, point2) * 1000
                    area_list.append(math.pi *(distance/2)**2)
                    folium.Circle([cluster_df0['lat'][n],cluster_df0['lng'][n]], radius = distance/2, fill=False, fill_color='#00ff00').add_to(g0)
                    
                    
        # for n in range(len(cluster_df)):
        #     folium.Circle([cluster_df['lat'][n],cluster_df['lng'][n]], radius=cluster_df['log_count'][n]*100, 
        #                 fill=True, fill_color='#0000ff').add_to(g0)

                    
        #도미노피자
        for n in domino_input.index : 
            folium.Marker([domino_input['lat'][n], domino_input['lng'][n]],
                    icon = folium.Icon(color= 'blue'),  #, icon = './Data/도미노피자.png'
                    popup=('도미노피자'+' '+domino_input['store'][n])).add_to(g1)
        # 피자헛
        for n in pizza_hut_input.index : 
            folium.Marker([pizza_hut_input['lat'][n], pizza_hut_input['lng'][n]],
                        icon = folium.Icon(color= 'red'),  #, icon = './Data/도미노피자.png'
                        popup=('피자헛'+' '+pizza_hut_input['store'][n])).add_to(g2)      


            
        # 미스터피자
        for n in mr_pizza_input.index : 
            folium.Marker([mr_pizza_input['lat'][n], mr_pizza_input['lng'][n]],
                icon = folium.Icon(color= 'darkpurple'),  #, icon = './Data/도미노피자.png'
                popup=('미스터피자'+' '+mr_pizza_input['store'][n])).add_to(g3)
                
        # 피자스쿨
        for n in pizza_school_input.index : 
            folium.Marker([pizza_school_input['lat'][n], pizza_school_input['lng'][n]],
                        icon = folium.Icon(color= 'orange'),  #, icon = './Data/도미노피자.png'
                        popup=('피자스쿨'+' '+pizza_school_input['store'][n])).add_to(g4)

        #피자알볼로
        for n in pizza_alvolo.index : 
            folium.Marker([pizza_alvolo['lat'][n], pizza_alvolo['lng'][n]],
                    icon = folium.Icon(color= 'lightblue'),  #, icon = './Data/도미노피자.png'
                    popup=('피자알볼로'+' '+pizza_alvolo['지점명'][n])).add_to(g5)
                
        #오구쌀피자
        for n in pizza_59ssal.index : 
            folium.Marker([pizza_59ssal['lat'][n], pizza_59ssal['lng'][n]],
                    icon = folium.Icon(color= 'beige'),  #, icon = './Data/도미노피자.png'
                    popup=('오구쌀피자'+' '+pizza_59ssal['지점명'][n])).add_to(g6)
                

        #피자에땅
        for n in pizza_ddang.index : 
            folium.Marker([pizza_ddang['lat'][n], pizza_ddang['lng'][n]],
                    icon = folium.Icon(color= 'green'),  #, icon = './Data/도미노피자.png'
                    popup=('피자에땅'+' '+pizza_ddang['지점명'][n])).add_to(g7)
                
                
                
        #피자마루
        for n in pizza_maru.index : 
            folium.Marker([pizza_maru['lat'][n], pizza_maru['lng'][n]],
                    icon = folium.Icon(color= 'lightgreen'),  #, icon = './Data/도미노피자.png'
                    popup=('피자마루'+' '+pizza_maru['지점명'][n])).add_to(g8)
            
                
                
                
                
                



        folium.LayerControl(collapsed=False).add_to(m)
        m.save('./Data/Plugins_9.html')
        m
        map1 = QWebEngineView()

        # must be absolute path
        map1.setUrl(QUrl("C:/Users/user/Documents/Gitspace/PIZZA/Data/Plugins_9.html"))
        leftlayout.addWidget(map1)
        
        

       




if __name__ == "__main__":
    app = QApplication(sys.argv) # name부터 시작하고 클라스 쇼에서 시작 한다.
    mywindow = myWindows() #클라스다 ??
    mywindow.show()
    app.exec_()

