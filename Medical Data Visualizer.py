#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 19:05:42 2021

@author: richie
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('medical_examination.csv')
df['overweight'] = np.where(df['weight']/((df['height']/100)**2) > 25,1,0)

#df_copy = df.copy()
conditions_cholesterol = [df['cholesterol'] == 1, df['cholesterol'] > 1]
conditions_gluc = [df['gluc'] == 1, df['gluc'] > 1]
choices = [0,1]

df['cholesterol'] = np.select(conditions_cholesterol,choices,df['cholesterol'])
df['gluc'] = np.select(conditions_gluc,choices,df['gluc'])

# df_copy['cholesterol'] = df_copy['cholesterol'].apply(lambda x:0 if x == 1 else 1)
# df_copy['gluc'] = df_copy['gluc'].apply(lambda x:0 if x == 1 else 1)

dataSubset = df[['active','alco','cholesterol','gluc','overweight','smoke','cardio']]
dataSubset2 = dataSubset.copy()
longFormat = pd.melt(dataSubset,id_vars='cardio')
longFormat2 = pd.melt(dataSubset2,id_vars=['cardio'])
fig = sns.catplot(x='variable',col='cardio',data=longFormat,kind='count',hue='value')

longFormat2['total'] = 1
longFormat2 = longFormat2.groupby(['cardio','variable','value'],as_index=False).count()
plt.figure()
sns.catplot(x='variable',y='total',col='cardio',data=longFormat2,kind='bar',hue='value')
# cleaneddf = df.drop(df[df['ap_lo'] > df['ap_hi']].index)
# cleaneddf = cleaneddf.drop(cleaneddf[cleaneddf['height'] < cleaneddf['height'].quantile(0.025)].index)
# cleaneddf = cleaneddf.drop(cleaneddf[cleaneddf['height'] > cleaneddf['height'].quantile(0.975)].index)
# cleaneddf = cleaneddf.drop(cleaneddf[cleaneddf['weight'] < cleaneddf['weight'].quantile(0.025)].index)
# cleaneddf = cleaneddf.drop(cleaneddf[cleaneddf['weight'] > cleaneddf['weight'].quantile(0.975)].index)

plt.figure()
cleaneddf = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]
mask = np.triu(cleaneddf.corr())
sns.heatmap(cleaneddf.corr(method='pearson'),mask=mask,annot=True,fmt='.1f')
