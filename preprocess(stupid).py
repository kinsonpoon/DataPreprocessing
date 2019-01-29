# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 10:43:06 2019

@author: kinsonp
"""

import os.path
import numpy as np
import matplotlib.pyplot as plt
import scipy as spy
import pandas as pd

input_file = "data.csv"
fillinfile="empty.csv"
df = pd.read_csv(input_file, header = 0)
df_fill=pd.read_csv(fillinfile, header = 0)
target=['日期', '測項']
detail=['AMB_TEMP', 'WIND_DIREC', 'WIND_SPEED', 'RAINFALL', 'RH', 'PM2.5','PM10']
hr=['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
features=df.keys()
#num_features=len(df.keys())
print("features:",features)
#print("num_features:",num_features)
d=pd.date_range(start='1/1/2015', end='31/12/2015', freq='D')
d=d.strftime("%Y/%m/%d")
#print(d)
for num in d:
    for dklm in detail:
        x=(df.loc[(df['日期'] == num)&(df['測項'] == dklm)])
    
        for y in hr:
            string=''
            for char in str(num):
                if(char!='/'):
                    string+=char
            string=string+y
            string=int(string)
            print(string)
            try:
                df_fill.loc[(df_fill['Date']==string), dklm] = int(x[y])
            except:
                continue

#
#date = pd.date_range(start='1/1/2015', end='31/12/2015', freq='H')
#index=index.strftime("%x%H")






#date=date.strftime("%Y%m%d%H")
#print(type(date[0]))

#print(df_fill.loc[(df_fill['Date']==int(date[0]))])
#df_fill.loc[(df_fill['Date']==date[0]), 'AMB_TEMP'] = 10
#print(df_fill)
print(df_fill)
df_fill.to_csv("output.csv", encoding='utf-8', index=True)   
print("converted to csv:)")
