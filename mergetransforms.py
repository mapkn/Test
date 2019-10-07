# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 18:03:29 2017

@author: patemi
"""

#https://stackoverflow.com/questions/53645882/pandas-merging-101

import pandas as pd

# Initial df
df = pd.read_excel("sales_transactions.xlsx")


# Using Group By and Merge

print(df.groupby('order')["ext price"].sum())

order_total = df.groupby('order')["ext price"].sum().rename("Order_Total").reset_index()

# merge df with order_total
df_1 = df.merge(order_total)
df_1["Percent_of_Order"] = df_1["ext price"] / df_1["Order_Total"]

print(df_1)



# Using Transform

print(df.groupby('order')["ext price"].transform('sum'))

df["Order_Total"] = df.groupby('order')["ext price"].transform('sum')
df["Percent_of_Order"] = df["ext price"] / df["Order_Total"]

print(df)


df3=df['account'].dot(df['account']).dot(df['account'])

df3=df['account'].dot(df['account']).dot(df['account'])
#