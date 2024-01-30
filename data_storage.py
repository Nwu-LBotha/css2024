# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:41:24 2024

@author: Louise
"""

# Data storing in pyth
#1. Using lists ()
#2. Using dictionaries {}
#3. Dataframes - spicific to pandas

import pandas as pd


"""
# No 1 the lists
age = [39,25,29,46,22,35,22,49,30,40,30]
sizeA= len(age)
gender = ['F', 'M','F', 'M','M','M','M','M','M','M','F']
country = ['Japan','Singapore','Germany','Japan','Norway','Denmark','Germany','Japan','China','China','China']

print(age[0])
print('average is', sum(age)/sizeA)
print(country[:])

age.insert(0,29)
print(age[:])

""" 
"""
# No 2 dictonaries

dictonaries = {'cat' : 'Bastard', 'dog' : 'loyal', 'bird' : 'loud', 'horse' : 'big'} 

print(dictonaries['dog'])

"""

# Dataframes

import pandas as pd

cars = { 'make' : ['polo', 'toyota', 'hyndai', 'suzuki'], 'year' : [2007, 2002, 2020, 1995],'color' : ['blue', 'black', 'red', 'white'] }
df = pd.DataFrame(cars)
print(df['color'])
print(df.describe())

df.drop(columns['color'], inplace=True)