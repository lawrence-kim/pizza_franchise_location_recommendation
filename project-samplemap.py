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
from haversine import haversine

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

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

        self.us = folium.Map(location=[36,127],
                    zoom_start=7)

        m = folium.Map(location=[36, 127],  zoom_start=7)

        # market cluster
        mcg = folium.plugins.MarkerCluster(control=False)
        m.add_child(mcg)

        g1 = folium.plugins.FeatureGroupSubGroup(mcg, 'Pizza Hut')
        m.add_child(g1)
        g2 = folium.plugins.FeatureGroupSubGroup(mcg, 'Pizza School')
        m.add_child(g2)
        g3 = folium.plugins.FeatureGroupSubGroup(mcg, "Domino's")
        m.add_child(g3)
        g5 = folium.plugins.FeatureGroupSubGroup(m, 'K-Means 클러스터')
        m.add_child(g5)


        # insert on the map
        import pandas as pd
        df1 = pd.read_csv("./Data/pizza_hut_address_complete.csv")
        df3 = pd.read_csv("./Data/pizzaschool_populationComplete.csv")
        df2 = pd.read_csv("./Data/dominopizza_complete.csv")
        cluster_df0 = pd.read_csv("./Data/상권cluster별위치.csv")

        import math
        from haversine import haversine

        for n in df1.index:
            folium.Marker([df1['lat'][n], df1['lng'][n]],icon=folium.Icon(color='blue', icon='info-sign')).add_to(g1)

        for n in df2.index:
            folium.Marker([df2['lat'][n], df2['lng'][n]],icon=folium.Icon(color='red', icon='info-sign')).add_to(g2)
            
        for n in df3.index:
            folium.Marker([df3['lat'][n], df3['lng'][n]],icon=folium.Icon(color='orange', icon='info-sign')).add_to(g3)        
        
        area_list = []
        for n in range(len(cluster_df0)):
            point1 = cluster_df0['max_lat'][n], cluster_df0['max_lng'][n]
            point2 = cluster_df0['min_lat'][n], cluster_df0['min_lng'][n]
            distance= haversine(point1, point2) * 1000
            area_list.append(math.pi *(distance/2)**2)
            folium.Circle([cluster_df0['lat'][n],cluster_df0['lng'][n]], radius = distance/2, fill=False, fill_color='#00ff00').add_to(g5)

        folium.LayerControl(collapsed=False).add_to(m)
        m.save(os.path.join('./Data/Plugins_9.html'))
        self.view.load(QtCore.QUrl().fromLocalFile(
            os.path.split(os.path.abspath(__file__))[0]+r"./Data/Plugins_9.html"
        ))

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