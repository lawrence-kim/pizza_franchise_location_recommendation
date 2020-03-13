import numpy as np
import sys
import os
import branca
from branca.element import *
import folium
from folium import plugins
from PyQt5 import QtWebEngineWidgets, QtCore, QtWidgets, QtWebChannel
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication, QWidget, QLineEdit, QLabel, QPushButton, QGridLayout, QDockWidget
import pandas as pd
import folium
import webbrowser
import json
import requests
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *       # 종료하는 것은 widget만으로 안됨. 추가적으로 import 해줘야 함
from PyQt5.QtGui import *

# 부산지역 MAP

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('logo.png'))
        self.setWindowTitle("BUSAN MAP")

        self.setObjectName('Main')
        QtCore.QMetaObject.connectSlotsByName(self)

        self.view = QtWebEngineWidgets.QWebEngineView()
        self.view.setObjectName('MapWidget')

        self.window  = QWidget()
        self.window.setObjectName('MainWidget')
        self.layout = QGridLayout()
        self.window.setLayout(self.layout)
        self.layout.addWidget(self.view)
        self.setCentralWidget(self.window)

        self.channel = QtWebChannel.QWebChannel(self.view.page())
        self.view.page().setWebChannel(self.channel)
        self.channel.registerObject("jshelper", self)

        self.us = folium.Map(location=[35.19,129.05],  zoom_start=11)    
      
        map1 = folium.Map(location=[35.19,129.05],  zoom_start=11)

        g1 = folium.plugins.FeatureGroupSubGroup(map1, 'PIZZASCHOOL', show = False)
        map1.add_child(g1)

        g2 = folium.plugins.FeatureGroupSubGroup(map1, 'DOMINO', show = False)
        map1.add_child(g2)

        g3 = folium.plugins.FeatureGroupSubGroup(map1, 'MR.PIZZA', show = False)
        map1.add_child(g3)

        g4 = folium.plugins.FeatureGroupSubGroup(map1, 'PIZZAHUT', show = False)
        map1.add_child(g4)

        g5 = folium.plugins.FeatureGroupSubGroup(map1, 'PIZZAALVOLO', show = False)
        map1.add_child(g5)

        g6 = folium.plugins.FeatureGroupSubGroup(map1, '59쌀PIZZA', show = False)
        map1.add_child(g6)

        g7 = folium.plugins.FeatureGroupSubGroup(map1, 'PIZZAETANG', show = False)
        map1.add_child(g7)

        g8 = folium.plugins.FeatureGroupSubGroup(map1, 'PIZZAMARU', show = False)
        map1.add_child(g8)

        g9 = folium.plugins.FeatureGroupSubGroup(map1, 'UNIVERSITY', show = False)
        map1.add_child(g9)
                
        # 지도에 insert하기 그리기
        import pandas as pd
        부산피자 = pd.read_csv('./Data/부산피자.csv')
        부산대학교 = pd.read_csv('./Data/부산대학교.csv')

        for row in 부산피자[부산피자['브랜드'] == '피자스쿨'].itertuples() : 
            folium.Marker(location=[row.lat,  row.lng],icon=folium.Icon(color='purple', icon='star'),popup=[row.브랜드]).add_to(g1)
        
        for row in 부산피자[부산피자['브랜드'] == '도미노피자'].itertuples() : 
            folium.Marker(location=[row.lat,  row.lng],icon=folium.Icon(color='blue', icon='star'),popup=[row.브랜드]).add_to(g2)

        for row in 부산피자[부산피자['브랜드'] == '미스터피자'].itertuples() : 
            folium.Marker(location=[row.lat,  row.lng],icon=folium.Icon(color='beige', icon='star'),popup=[row.브랜드]).add_to(g3)

        for row in 부산피자[부산피자['브랜드'] == '피자헛'].itertuples() : 
            folium.Marker(location=[row.lat,  row.lng],icon=folium.Icon(color='red', icon='star'),popup=[row.브랜드]).add_to(g4)

        for row in 부산피자[부산피자['브랜드'] == '피자알볼로'].itertuples() : 
            folium.Marker(location=[row.lat,  row.lng],icon=folium.Icon(color='green', icon='star'),popup=[row.브랜드]).add_to(g5)

        for row in 부산피자[부산피자['브랜드'] == '오구쌀피자'].itertuples() : 
            folium.Marker(location=[row.lat,  row.lng],icon=folium.Icon(color='gray', icon='star'),popup=[row.브랜드]).add_to(g6)

        for row in 부산피자[부산피자['브랜드'] == '피자에땅'].itertuples() : 
            folium.Marker(location=[row.lat,  row.lng],icon=folium.Icon(color='orange', icon='star'),popup=[row.브랜드]).add_to(g7)

        for row in 부산피자[부산피자['브랜드'] == '피자마루'].itertuples() : 
            folium.Marker(location=[row.lat,  row.lng],icon=folium.Icon(color='pink', icon='star'),popup=[row.브랜드]).add_to(g8)

        for row in 부산대학교[부산대학교['분류'] == '대학교'].itertuples() : 
            folium.Marker(location=[row.lat,  row.lng],icon=folium.Icon(color='black', icon='cloud'),popup=[row.학교명]).add_to(g9)

        folium.LayerControl(collapsed=False).add_to(map1)
        map1.save(os.path.join('./Data/Plugins_9.html'))

        self.view.load(QtCore.QUrl().fromLocalFile(
            os.path.split(os.path.abspath(__file__))[0]+r"./Data/Plugins_9.html"))

        self.setGeometry(100,100,1200,900)
        self.show()

    @QtCore.pyqtSlot(str)
    def pathSelected(self, lat):
        print(lat)

if __name__ == '__main__':
    sys.argv.append("--remote-debugging-port=8000")
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())