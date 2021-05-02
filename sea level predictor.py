#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 18:13:45 2021

@author: richie

FreeCodeCamp Data Analysis with Python Projects - Sea Level Predictor
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from  scipy import stats

df = pd.read_csv('epa-sea-level.csv')
xaxis = np.array(df['Year'])
yaxis = np.array(df['CSIRO Adjusted Sea Level'])
fig,ax = plt.subplots()
plt.scatter(xaxis,yaxis,label='scatter data')
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
res = stats.linregress(xaxis,yaxis)
resfrom2000 = stats.linregress(xaxis[120:],yaxis[120:])
xaxisfit = np.arange(1880,2051,1)
plt.plot(xaxisfit, res.intercept + res.slope*xaxisfit, 'r', label='fitted line 1')
plt.plot(xaxisfit[120:], resfrom2000.intercept + resfrom2000.slope*xaxisfit[120:], 'g', label='fitted line 2')
plt.xticks(np.arange(1850,2080,25))
plt.legend()

