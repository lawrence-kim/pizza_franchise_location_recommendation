Pizza Franchise Location Recommendation
=========
Hypothesis
----------
The city of Seoul has 22,836 commercial areas according to official Seoul City Statistics. Through KNN clustering that reduced the number of commercial areas into smaller clusters, we believe the relative size of each cluster will present the approximate deliverable market size of a pizza franchise. We have plotted all the stores of the biggest four franchises which are shown with the clusters. This information will be a good indicator for a person who is planning on opening a new franchise store in Seoul. We assume the best location will be near clusters where there are few existing pins and the size of the cluster itself is big.

Method
----------
* Source: Pizza Hut Korea, Domino’s Korea, Pizza School, Mr. Pizza, Seoul City Statistics
* ML model: K-means cluster  

Libraries
-------
Please install following libraries: sys, Pyqt5, Matplotlib, Numpy, Pandas, Seaborn, Platform, Sklearn, Os, Subprocess, Urllib, Json, Bs4, Locale, time, requests, haversine, folium, webbrowser, branca, math, beautifulsooup, pymysql

<pre>
<code>
$ pip install [above library]
</code>
</pre>  


Getting Started
-----------

After downloading pizza_franchise_location_recommendation repository, please type below on command prompt or shell  
<pre>
<code>
$ [sudo] python3 project-main.py  
</code>
</pre>  



GUI samples
-------
### Main page  
<img width="251" alt="pizza_main" src="https://user-images.githubusercontent.com/57359849/76918350-7f532900-6909-11ea-9ecd-36351f547070.PNG">  

### Introduction  
<img width="501" alt="pizza_introduction" src="https://user-images.githubusercontent.com/57359849/76918349-7f532900-6909-11ea-8447-e0e07aed16fb.PNG">  
brief explanation about the top three franchises in Korea  

### Data    
<img width="651" alt="pizza_data" src="https://user-images.githubusercontent.com/57359849/76918348-7eba9280-6909-11ea-96cc-e56b30ed3d97.PNG">  
number counts of Domino's, Pizza Hut, and Pizza School sorted by state-district  

### Chart   
<img width="801" alt="pizza_chart" src="https://user-images.githubusercontent.com/57359849/76918346-7e21fc00-6909-11ea-9d43-e5dbe223706a.PNG">  
number counts of Pizza School sorted by state  

### Brand Recommendation  
<img width="379" alt="pizza_brandrecommendation" src="https://user-images.githubusercontent.com/57359849/76918345-7cf0cf00-6909-11ea-8dae-172421889ca0.PNG">  
Pizza Hut is recommended With the input location Seoul Gannam district and initial investment of 1 Billion KRW.  

### Sample Map  
<img width="601" alt="pizza_samplemap" src="https://user-images.githubusercontent.com/57359849/76918352-7febbf80-6909-11ea-8a59-1d8a9e218843.PNG">  
The sample map of 800 commercial area clusters with options to pin Pizza Hut, Pizza School, Domino's, and/or k-means clusters.  

### Selected Map  
<img width="601" alt="pizza_selectedmap" src="https://user-images.githubusercontent.com/57359849/76918357-80845600-6909-11ea-9bc4-05b5db02feef.PNG">  
You can also choose number of clusters and the district for better visualization. This will be a good indicator for pizza franchise opener to decide the right location.  


