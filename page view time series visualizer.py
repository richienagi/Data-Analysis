#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 19:18:59 2021

@author: richie
FreeCodeCamp Data Analysis with Python Projects - Page View Time Series Visualizer
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# df = pd.read_csv('fcc-forum-pageviews.csv') 
# df = df.set_index('date')

df_copy = pd.read_csv('fcc-forum-pageviews.csv',parse_dates=['date'],index_col=['date']) 

#cleaneddf = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]
cleaneddf_copy = df_copy[(df_copy['value'] >= df_copy['value'].quantile(0.025)) & (df_copy['value'] <= df_copy['value'].quantile(0.975))]

sns.lineplot(x='date',y='value',data=cleaneddf_copy)
plt.xlabel('Date')
plt.ylabel('Page Views')
plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

groupedMonth = cleaneddf_copy.groupby(pd.Grouper(freq='M')).mean()
groupedMonth = groupedMonth.reset_index()
groupedMonth['year'] = pd.DatetimeIndex(groupedMonth['date']).year
groupedMonth['month'] = groupedMonth['date'].dt.month_name()
monthOrder = ['January','February','March','April','May','June','July','August','September','October','November','December']
plt.figure()
sns.barplot(x='year',y='value',data=groupedMonth,hue='month',hue_order=monthOrder)
plt.xlabel('Years')
plt.ylabel('Average Page Views')
plt.legend(loc='upper left')

monthOrderBox = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
boxPlotdf = cleaneddf_copy
boxPlotdf = boxPlotdf.reset_index()
boxPlotdf['month'] = boxPlotdf['date'].dt.month_name().str.slice(stop=3)
boxPlotdf['year'] = pd.DatetimeIndex(boxPlotdf['date']).year
plt.figure()
fig,axes = plt.subplots(1,2)
sns.boxplot(ax=axes[0],x='year',y='value',data=boxPlotdf)
sns.boxplot(ax=axes[1],x='month',y='value',data=boxPlotdf,order=monthOrderBox)
axes[0].set_xlabel('Year')
axes[0].set_ylabel('Page Views')
axes[1].set_xlabel('Month')
axes[1].set_ylabel('Page Views')
axes[0].set_title('Year-wise Box Plot (Trend)')
axes[1].set_title('Month-wise Box Plot (Seasonality)')

