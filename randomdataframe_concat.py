# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 09:01:39 2017

@author: patemi
"""

import pandas as pd
import numpy as np
import frtbsa


# Random dataframe
np.random.seed(5)
df = pd.DataFrame(np.random.randint(100, size=(100, 6)), 
                  columns=list('ABCDEF'), 
                  index=['R{}'.format(i) for i in range(100)])
print(df.head())

# Columns C to E inclusive
print(df.loc[:,'C':'E'])



# Columns C only
x=df[['C']].ix[:10,:]


# Random numpy array (correlations)
y=np.random.rand(10,10)


# M1 is a numpy array
M1=np.full([10,10],0.2)

# I1 is a numpy matrix
#I1=np.matlib.identity(10)

# Operation on an array and matrix will result in a matrix
#M2=np.subtract(M1,0.2*I1)    

# Numpy matrix
#m=np.add(I1,M2)


#zz=frtbsa.RC_curvature(x,m,x)



df = pd.DataFrame([["2014", "q1"], ["2015", "q3"]],columns=('Year', 'Quarter'))

print(df)


df['Period'] = df.Year.str.cat(df.Quarter)

print(df)



df = pd.DataFrame([[2014, 1],[2015, 3]],columns=('Year', 'Quarter'))

print(df)


df['Period'] = df.Year.astype(str).str.cat(df.Quarter.astype(str), sep='q')

print(df)


# Element -wise subtraction in a datafame column

df['Minus']=df['Year'].subtract(df['Quarter'])
df['Plus']=df['Year'].add(df['Quarter'])