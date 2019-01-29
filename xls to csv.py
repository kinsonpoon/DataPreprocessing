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

input_file = "data.xls"
data_xls = pd.read_excel(input_file, 'Sheet1', index_col=None)
data_xls.to_csv('data.csv', encoding='utf-8')