# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 13:57:41 2017

@author: patemi
"""

import pandas as pd
import dateutil
 
# Load data from csv file
data = pd.DataFrame.from_csv('phone_data.csv')
# Convert date from string to date times
data['date'] = data['date'].apply(dateutil.parser.parse, dayfirst=True)

# How many rows the dataset
print(data['item'].count())

 
# What was the longest phone call / data entry?
print(data['duration'].max())

 
# How many seconds of phone calls are recorded in total?
print(data['duration'][data['item'] == 'call'].sum())

 
# How many entries are there for each month?
print(data['month'].value_counts())

# Number of non-null unique network entries
print(data['network'].nunique())


print(data.groupby(['month']).groups.keys())


print(len(data.groupby(['month']).groups['2014-11']))




print(data[(data['item']=='call') & (data['network']=='Tesco')])
