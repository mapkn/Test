# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 16:56:48 2017

@author: patemi
"""

import numpy as np
import pandas as pd
import math
import numpy.matlib


# Creates and empty Data Frame
df_test_K_b=pd.DataFrame()


# Nedd to initialise the array as 2-dimensional if we want to transpose
a=np.array([[1,5];[2,10]])
#b=np.transpose(a)

# Create data frame for the data we want to add
data_add=pd.DataFrame(a, columns=['Bucket','K_b'], index=['Bucket'])

df_test_K_b=df_test_K_b.append(data_add)


#Give data types
print(df_test_K_b.dtypes)

#Gives statistics
print(df_test_K_b.describe())
