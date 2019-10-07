# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 09:23:41 2018

@author: patemi
"""

# https://chrisalbon.com/python/data_wrangling/pandas_dropping_column_and_rows/

import pandas as pd
import os.path
import numpy as np

path = '\\\\apw-grskfs01\\GVAR2\\Global Risk Management'
file = 'Test.csv'

################################

##Creating a new DF

#http://pbpython.com/pandas-list-dict.html

#################################

# Create new DF...using a dictionary
data = {'name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy', 'Jake'], 
        'year': [2011, 2012, 2013, 2014, 2015, 2016], 
        'reports': [4, 24, 31, 2, 3,5]}
df = pd.DataFrame(data, index = ['Cochice', 'Pima', 'Santa Cruz', 'Maricopa', 'Yuma', 'PPP'])


# Creates an empty Data Frame
df_test_K_b=pd.DataFrame()

# Create new DF from list(s)
sales = [('account', [' Jones LLC', 'Alpha Co', 'Blue Inc']),
         ('Jan', [150, 200, 50]),
         ('Feb', [200, 210, 90]),
         ('Mar', [140, 215, 95]),
         ]
dfsales = pd.DataFrame.from_items(sales)


yy=dfsales['account'].str.strip()




# Copy a dataframe
dfCopy=df.copy()

##########################################
# Adding Column to existing DF

##############################################

#Adding a column to an existing dataframe
df['subject']=pd.Series(np.random.randn(6), index=df.index)



##########################################
# Adding Row (s) to existing DF

##############################################

a=np.array([[1,5]])

# Create data frame for the data we want to add
data_add=pd.DataFrame(a, columns=['Bucket','K_b'], index=['Bucket'])

# Append data
df_test_K_b=df_test_K_b.append(data_add)


a=np.array([[2,6]])
data_add=pd.DataFrame(a, columns=['Bucket','K_b'], index=['Bucket'])
df_test_K_b=df_test_K_b.append(data_add)


##########################################
# Unique items in a given column

names=df['name'].unique().tolist()

##############################################



# Multiply elements of df by 2
df=df*2


#dfsales


#Top 5 rows of the DF
print(dfCopy.head())


# Take away a number from each element of a DF column
dfY=(df.reports-1999)

# Take away a number from each element of a DF column ad return the index of the sorted values
dfYIndex=(df.reports-1999).argsort()



# Set a different column as index
#df=df.set_index('reports')

# Drop a row
df.drop(['Cochice', 'Pima'])

# Drop a column
df.drop('reports', axis=1)

# Drop a row by row number
df.drop(df.index[2])
df.drop(df.index[[2,3]])

# Information about the DataFrame
#print(df.info())



#################### Create new Dataframe column with elementwise multiplication of existing ones

df[['reports','year']]=df[['reports','year']].astype(float)

df['reports*year']=df['reports']*df['year']

########################################################

# Adding a new column with the same value in all rows
df['new col']=5

# Adding a new column using insert
df.insert(0,'another col',4)


# Filter by column name
df2=df.filter(regex='rep')

# Filter by column names
#print(df.filter(items=['name','year']))

# Filter columns containing 'ear'
#print(df.filter(like='ear',axis=1))


# print the dataframe index
print(df.index)

# print only specified columns
print(df[['year','name']])


# Return the column names containing given string
cols = [col for col in df.columns if 'ear' in col]


# Number of columns in a dataframe
num_cols=len(df.columns)


print(df.describe())


# cast dataframe to boolean
dfb=df.astype(bool)




# Save the DF data to a CSV file
dfb.to_csv(path_or_buf=os.path.join(path,file))



yy=df.nlargest(2,['year','reports'])




########### Loc vs iLoc ######################


#https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/

#iloc uses the Python stdlib indexing scheme, where the first element of the range is included and the last one excluded. 
#So 0:10 will select entries 0,...,9. loc, meanwhile, indexes inclusively. So 0:10 will select entries 0,...,10.


# iLoc for index/integer based reference
# Loc for logical reference (boolean)

#DataFrame.loc
#Access a group of rows and columns by label(s) or a boolean array.

# iloc
print(df.iloc[0])
print(df.iloc[0].year)




# Square brackets to return as dataframe
yyy=df['name'].iloc[[0]].item()



# Dataframe column data types
#print(df.dtypes)

##bb=df['name'].iloc[0].str

#bb=df[['name']].iloc[[0]]

#bb=df[['name']].iloc[[0]].astype(str)

#bb=df['name'].iloc[0].to_string

# Convert all columns to strings
df=df.astype(str)
#print(df.dtypes)


# Get an item as string
ff=df[df.name=='MollyMolly'].name.item()


# Filter based on column 'name' contents - equivalent to SQL WHERE...LIKE.....plus OR
df3=df[(df.name.str.contains('ake')) |(df.name=='JasonJason')]


#Filter based on column 'name' contents - equivalent to SQL WHERE 
df4=df[df.name=='JasonJason']



##################################

#Iterating through DataFrames

# https://erikrood.com/Python_References/iterate_rows_pandas.html
# using iterrows to iterate through dataframes
for index, row in df.iterrows():
    print (row["name"], row.year)


# using itertuples to iterate through dataframes
for row in df.itertuples(index=True, name='Pandas'):
    print (getattr(row, "name"), getattr(row, "year"))

#################################################


# Finding null (empty) elements in a dataframe
print(pd.isnull(df['name']))



########################################

#Using Loc


df_rand = pd.DataFrame(np.random.randint(0,100,size=(100, 5)), columns=list('ABCDE'))

print(df_rand['A']>50)
print(df_rand['B']>50)
print(df_rand.loc[(df_rand['A']>50) & (df_rand['B']>50),['A']])

i=(df_rand['A']>50) & (df_rand['B']>50)

df2=df_rand.loc[(df_rand['A']>50) & (df_rand['B']>50),['A']]


#print(df_rand.loc[df_rand['A']>50 & df_rand['B']>50,['A']])


################# Fill na/Nan's with something

#df_input_mapped['Market Cap Bucket'].fillna('SmallCap', inplace=True)



####### Renaming a column
df4=df4.rename(columns = {'name':'NAme'})



# Get the column names from dataframe
print(list(df4.columns.values))


# Sorting the values in a dataframe column - inplace = False
df=df.sort_values(by='subject', inplace=False)

# Sorting the values in a dataframe column - inplace = True
df.sort_values(by='subject', inplace=True)

