# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 15:43:42 2021

@author: liu
"""

import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np
import datetime
from pytides.tide import Tide
import os
#%%
directory = "C:\\Users\\liu.H2I\\Desktop\\neptune\\SFA\\"
os.chdir(directory)
df = pd.read_csv("wl_r_harmonic.csv",parse_dates = [0],dayfirst=True)
df['Date']= pd.to_datetime(df['Date'], format='%d/%m/%Y\t%H:%M', errors='raise')
df=df.astype({'WL':float})
Date = df['Date']
WL= df['WL']

tide = Tide.decompose(WL,Date)
constituent = [c.name for c in tide.model['constituent']]
table = DataFrame(tide.model, index=constituent).drop('constituent', axis=1)
model = tide.at(Date)
residual = WL - model

# #%%
plt.plot(Date,WL, color='blue', linewidth=0.5,label="obs")
plt.plot(Date,model, color='lime', linewidth=0.5,label="model")
plt.plot(Date,residual, color='magenta', linewidth=0.5,label="residual")
plt.xlabel("Time")
plt.xlim([datetime.datetime(2018, 1, 1), datetime.datetime(2019, 1, 1)])
#plt.ylim([-1.5,1])
plt.ylabel("Water level (m)")
plt.title("")
plt.legend(loc='upper right')
plt.xticks(rotation=45)
plt.rcParams.update({'font.size': 15})
figure = plt.gcf() # get current figure
figure.set_size_inches(18, 6)
plt.savefig("wl.png", bbox_inches='tight',dpi=300)

