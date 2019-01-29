# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 14:34:41 2019

@author: kinsonp
"""
string=''
tar=''
for i in range(24):
    if(i<10):
        tar='0'+str(i)
    else:
        tar=str(i)
    string=string+"'"+tar+"'"+","
print(string)