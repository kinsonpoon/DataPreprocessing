# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 11:19:30 2019

@author: kinsonp
"""

import datetime
import pandas as pd
import numpy as np
index = pd.date_range(start='1/1/2015', end='31/12/2015', freq='H')
#index=index.strftime("%x%H")
index=index.strftime("%Y%m%d%H")
columns = ['AMB_TEMP', 'WIND_DIREC', 'WIND_SPEED', 'RAINFALL', 'RH', 'PM2.5','PM10']
df = pd.DataFrame(index=index, columns=columns)
df = df.fillna(0)
df.index.name = 'Date'
print(df)
df.to_csv("empty.csv", encoding='utf-8', index=True)   
print("converted to csv:)")