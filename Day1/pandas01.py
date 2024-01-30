# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 09:54:23 2024

@author: Louise
"""


import pandas as pd

#file = pandas.read_csv("country_data.csv")
#file = pandas.read_csv("iris.csv")
#file = pandas.read_csv("housing_data.csv")

##The fucked file - fix by skiping the first five rows
#file = pandas.read_csv("insurance_data.csv",skiprows=5)
#file2 = pandas.read_csv("insurance_data.csv")
# The insurance_data excel is foobar and gives a range of errors.



col_name = ['A','B','C']
file = pd.read_csv("housing_data.csv", names = col_name)
print(file)

#df = pd.DataFrame(col_name)


# append data frame to CSV file
#df.to_csv('housing_data.csv', mode='a', index=False, header=False)
 
# print message
#print("Data appended successfully.")
#print(df)

#print(df.info())

#print(df.describe())


"""
import pandas as pd

# creating the dataframe

data = {'age' : [30, 40, 30, 49, 22, 35, 22, 46, 29, 25, 39], 'gender' : ["M", "M", "F", "M", "F", "F", "F", "M", "M", "F", "M" ], 'country' : ['RSA', 'Bot', 'RSA', 'RSA', 'Ken', 'Moz', 'les', 'Ken', 'Ken', 'Egypt', 'Sud' ]}

df = pd.DataFrame(data)

#Accessing specific columns
print(df)
print(df['age'])
print(df['gender'])


#Basic statistics
print(df['age'].min())
print(df['age'].max())
print(df['age'].mean())

#Filtereing data
print(df[df ['age'] > 30])

# Slicing rows and columns
#Select rows 1 to 3
print(df[1:4])

#Adding a new column
df['new_col'] = [1,2,3,4,5,6,7,8,9,10,11]
print(df)

#Removing a column
df.drop(columns=['new_col'], inplace=True)
print(df)
"""

"""
import pandas

file = pandas.read_csv("speel.csv")
print(file.info())
print(file.describe())
print(file)

print(file['Formula'])
print(file['molecular weight'].min())
print(file['molecular weight'].max())

""" 




