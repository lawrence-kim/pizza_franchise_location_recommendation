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
from sklearn.tree import DecisionTreeClassifier 
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

    def setupUI(self):
        # windows Frame
        self.setWindowTitle("map")
        self.setGeometry(700,250,1200,700)
        
        # radio
        self.radio1 = QRadioButton("on", self)
        self.radio2 = QRadioButton("off", self)        
        self.radio2.setChecked(True)        
        self.lineEdit = QLineEdit("", self)
        self.pushButton1 = QPushButton("execute")
        self.pushButton1.clicked.connect(self.pushButton1Clicked)
        self.label3 = QLabel("District : ")
        
        #global lineEdit1
        self.lineEdit1 = QLineEdit()
        self.pushButton = QPushButton("show map")
        self.pushButton.clicked.connect(self.checkBox)
        
  
        #Left Layout
        global leftlayout
        leftlayout = QVBoxLayout()
        #Right Layout        
        rightlayout = QVBoxLayout()
        self.label1 = QLabel("Number of clusters")
        self.label2 = QLabel("n_clusters :")
        rightlayout.addWidget(self.label1)
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
            
        cluster_df0 = pd.read_csv("./Data/상권cluster별위치2.csv")
        c_d_r = ''.join(c_d.split())
        pizza_hut_input=pizza_hut[pizza_hut['city_district'].str.contains(c_d_r)]
        pizza_school_input=pizza_school[pizza_school['city_district'].str.contains(c_d_r)]
        domino_input=domino[domino['city_district'].str.contains(c_d_r)]
                
        state_geo = './Data/TL_SCCO_SIG_WGS84.json'
        state_apart = './Data/korea_apart_decoded2.csv'
        state_data = pd.read_csv(state_apart, encoding = 'utf-8')

        # Initializing the map:
        c_d_lat=pizza_school_input['lat']
        c_d_lat=c_d_lat[c_d_lat.index[0]]          
        c_d_lng=pizza_school_input['lng']
        c_d_lng=c_d_lng[c_d_lng.index[0]]
        m = folium.Map(location=[c_d_lat, c_d_lng],  zoom_start=12)
        m.choropleth(
        geo_data=state_geo,
        name='housing price',
        data=state_data,
        columns=['Code', '평당 매매가'],
        key_on='feature.properties.SIG_CD',
        fill_color='YlGn',
        fill_opacity=0.7,
        line_opacity=0.5,
        legend_name='평당가격'
        )        

        mcg = folium.plugins.MarkerCluster(control=False)
        m.add_child(mcg)         
        g0 = plugins.FeatureGroupSubGroup(m, 'k-means cluster')
        m.add_child(g0)
        g1 = plugins.FeatureGroupSubGroup(m, "Domino's")
        m.add_child(g1)
        g2 = plugins.FeatureGroupSubGroup(m, 'Pizza Hut')
        m.add_child(g2)
        g4 = plugins.FeatureGroupSubGroup(m, 'Pizza School')
        m.add_child(g4)
                                   
        #Circle        
        area_list = []
        for n in range(len(cluster_df0)):
                    point1 = cluster_df0['max_lat'][n], cluster_df0['max_lng'][n]
                    point2 = cluster_df0['min_lat'][n], cluster_df0['min_lng'][n]
                    distance= haversine(point1, point2) * 1000
                    area_list.append(math.pi *(distance/2)**2)
                    folium.Circle([cluster_df0['lat'][n],cluster_df0['lng'][n]], radius = distance/2, fill=False, fill_color='#00ff00').add_to(g0)
                    
  
        # Domino's
        for n in domino_input.index : 
            folium.Marker([domino_input['lat'][n], domino_input['lng'][n]],
                    icon = folium.Icon(color= 'blue'),  #, icon = './Data/도미노피자.png'
                    popup=('도미노피자'+' '+domino_input['store'][n])).add_to(g1)
        # Pizza Hut
        for n in pizza_hut_input.index : 
            folium.Marker([pizza_hut_input['lat'][n], pizza_hut_input['lng'][n]],
                        icon = folium.Icon(color= 'red'),  #, icon = './Data/도미노피자.png'
                        popup=('피자헛'+' '+pizza_hut_input['store'][n])).add_to(g2)      

        folium.LayerControl(collapsed=False).add_to(m)
        m.save('./Data/Plugins_9.html')
        map1 = QWebEngineView()

        # must be absolute path
        map1.setUrl(QUrl("C:/Users/user/Documents/Gitspace/PIZZA/Data/Plugins_9.html"))
        leftlayout.addWidget(map1)
        
        

       




if __name__ == "__main__":
    app = QApplication(sys.argv) 
    mywindow = myWindows() 
    mywindow.show()
    app.exec_()

