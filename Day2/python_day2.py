# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 09:36:41 2024

@author: Louise
"""


### Day2_Extract, Transform, Load
####Local files

import pandas as pd


## If the file is in the folder that you are using (local) then call as such:
#df = pd.read_csv("country_data_index.csv")
#df = pd.read_csv("iris.csv")
#print(df)

# Note: If there is a diretory difference such as the directory data_02 then callin ghte file changes to
# df = pd.read_csv("data_02/country_data_index.csv") 


####Calling a file using a URL then use as follows: github etc
#url = https://github.com/Nwu-LBotha/css2024_day1/blob/main/country_data.csv
#df = pd.read_csv(url)
#df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
#print(df)
               


# adding some headings to the data is done as such:
#col_names = ["sep_length", "sep_width","pet_length","pet_width", "class"]
#df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data",header=None, names= col_names)

##Using different data types:
## Very straignt foward, just use the correct extention when calling these files.
##Text files: In this text file the data is sepperated with a ; symbol
# df = pd.read_csv("thisisatextfile.txt", sep=";")
#df = pd.read_csv("Geospatial Data.txt", sep=";")
#print(df)

####Calling a excel file
#df = pd.read_excel("data_02/excelfile.xlsx")
#df = pd.read_excel("residentdoctors.xlsx")

##Calling a Json file    
#df = pd.read_json("data_02/anotherfiletype.json")
#df = pd.read_json("student_data.json")
#print(df)

## Webscaping
##https://www.geeksforgeeks.org/python-web-scraping-tutorial/


##import databases
#import pubchempy as pcp
#from rdkit import Chem
#import pycaret

#Data Transform
#Indexing Columns

#The following csv file has a zero columb and therefore pandas will make that Unnamed: 0
#df = pd.read_csv("country_data_index.csv")
#print(df)

#To correct the Unnames:0, the following code can be used to combat this. Adding the extra bit removes the index 0 value
#df = pd.read_csv("country_data_index.csv", index_col=0)
#print(df)

##How to skip rows. This excel file does not have an equal rows and columns and as such, it gives an error. So the easiest is to skip the unnccessary 5 lines.
#df = pd.read_csv("insurance_data.csv",skiprows=5)
#print(df)

#Adding Column headings to the data is done as such, same as day 1
#col_names = ["dura","pulse","maxPulse", "Calories"]
#df = pd.read_csv("patient_data.csv", header=None, names= col_names)
#print(df)

####Unique Delimiter
#Please see the example of the text file where the values are sepperated with a delimiter (;)
#Moreover, the example has a space in the heading which is not going to give an error but it is also not reccomended to use.
#df = pd.read_csv("Geospatial Data.txt", sep=";")
#print(df)

####Inconsistent Data Types and Names
#In the file, the headers are not consistent, some are all caps while some of them are all lowercase.
#Also the grouping sucks for the ages. We should make this more effecient.
#df = pd.read_excel("residentdoctors.xlsx")
#print(df)
#print(df.info())
#So we have to exctract some of the data which can be used for analysis. This is the age distrubution which cannit be used as mentioned previously.
#The same goed for the maritial status where strings and intergers are mixed.
#The code below creates a new column called lower age. Check regular expressions for what is in the ("\d" which searhces for a special sequence, Returns a match where the string contains digits (numbers from 0-9)). see https://www.w3schools.com/python/python_regex.asp
#df['LOWER_AGE'] = df['AGEDIST'].str.extract('(\d+)-')
#If you check the info then the new column is still a object (extracted as a string). AS such we need to change this as an interger
#The next code converts this to an  into using the build in code astype
#df['LOWER_AGE'] = df['LOWER_AGE'].astype(int)

##Working with Dates
##Dates are usually interpreted as strings or text in csv files.
##Moreover, date formats are also dependend on the country. Since US is backwards they just mess up the date
#df = pd.read_csv("time_series_data.csv")
#print(df)
#print(df.info())

#lets remove the index column
#df = pd.read_csv("time_series_data.csv",index_col=0)
#print(df)

#The date is seen as an object aka string. So need to change that
#Create a new column and chuck the content in there. Then convert the format.
#df['Date'] = pd.to_datetime(df['Date'])
#df['Date'] = pd.to_datetime(df['Date'], format= '%d -%m -%Y' )
#print(df)
#print(df.info()) #Shows dateFormat now.

#Lets extract more things.
#df['Year'] = pd.to_datetime(df['Date'])
#df['Year'] = df['Date'].dt.year
#df['Month'] = pd.to_datetime(df['Date'])
#df['Month'] = df['Date'].dt.month
#df['Day'] = pd.to_datetime(df['Date'])
#df['Day'] = df['Date'].dt.day

##Shorter method
#df['Year'] = df['Date'].dt.year
#df['Month'] = df['Date'].dt.month
#df['Day'] = df['Date'].dt.day
#print(df)

####NANs and Wrong Formats####
#These files have NAN values which will give issues
#df = pd.read_csv("patient_data_dates.csv",index_col=0)
#Removes index column. If it has not been previously removed.
#df.drop(['Index'],inplace=True,axis=1)

#If you want to skip the data which has a NAN. Just drop it.
#df.drop(index=26,inplace=True)

#Allows you to see all rows
#pd.set_option('display.max_rows',None)

#Another way is to fill these types of data using a built in function.
# Use the average of the columns and fill in.
# Fillna? see the following https://www.w3schools.com/python/pandas/ref_df_fillna.asp
# When inplace=True, it means that the changes made by the fillna operation will be applied directly to the original DataFrame (df in this case), and it will not return a new DataFrame.
#average_calories = df["Calories"].mean()
#df["Calories"].fillna(average_calories, inplace=True)

#Also fix the date which is also fucked

#The next code gives an error so adding the format as mixed will fix this issue.
#df['Date'] = pd.to_datetime(df['Date'], format='mixed')

#df.dropna(subset=['Date'], inplace = True)
#Drop the NaT field in the Date column

#Or just drop all the empty rows NaN. Also removes the entire row.
#You will also need to reset the index with df.reset_index(drop=True) as if you remove a row, the row numbers will not be consecutive:
#df.dropna(inplace = True)
#df = df.reset_index(drop=True)

#Wrong Data – Replace and Remove Rows
#Sometimes there is a typing error in the dataset which can be fixed
#So you can replace them. Such in the example where 450 is clearly an error. So 45 might be the correct value
#The df.loc function replaces row 7 under the heading Duration with 45
#df.loc[7,'Duration'] = 45
#OR df['Duration'] = df['Duration'].replace([450],45)

## or just remove the row which is not always accaptable in a number of dataFrames. However, it depends on the size of the dataframe.large number of data will not work as well when editing one by one
## df,drop(7,inplace=True)

##Removing duplicates
##Sometimes data is riddeled with a duplicates. 
##Use the function df.drop_duplicates to remove them
#df.drop_duplicates(inplace=True)

#print(df)
#print(df.info())


#The code as done by CHPC 
"""
import pandas as pd

df = pd.read_csv('data_02/patient_data_dates.csv')

pd.set_option('display.max_rows',None)

print(df)

# Drop Index Column:

df.drop(['Index'],inplace=True,axis=1)

print(df)

# Fill NaNs or empty fields in Calorie Column

x = df["Calories"].mean()

df["Calories"].fillna(x, inplace = True)

print(df)

# Convert Wrong Date Format in Date Column

df['Date'] = pd.to_datetime(df['Date'])

# Drop NaT field in Date Column

df.dropna(subset=['Date'], inplace = True)

print(df)

# Remove any rows that have NaNs or empty fields
# Here only the row 1 for the MaxPulse column as the rest have been resolved
df.dropna(inplace = True)

# Reset index
df = df.reset_index(drop=True)

print(df)

# Remove duplicates found in line 10 and 11
df.drop_duplicates(inplace = True)

df = df.reset_index(drop=True)

print(df)

"""

##Applying Data transformations
##etc aggregations, appending, merging, and filtering. 
## aggregate data = transform collected data such as percentages, averages etc
## append and merge = update and merge data
## filter and manipulate data = 


#df = pd.read_csv('iris.csv')

#lets extract the headers
#col_names = df.columns.tolist()
#print(col_names)
#Going to square the values using two examples
#df['sepal_length']  = df['sepal_length']**2
#df['sepal_length_sq'] = df['sepal_length'].apply(lambda x: x**2)

#Group the data
# Pandas groupby is used for grouping the data according to the categories and applying a function to the categories.
#grouped = df.groupby('class')

#mean_squared_values = grouped['sepal_length_sq'].mean()
#sum_squared_values = grouped['sepal_length_sq'].sum()
#count_squared_values = grouped['sepal_length_sq'].count()

## append and merge = update and merge data
#df1 = pd.read_csv('person_split1.csv')
#df2 = pd.read_csv('person_split2.csv')

# Concatenate the dataframes
#df = pd.concat([df1, df2], ignore_index=True)

##Now the columns are different. Concatanate wont work so use merge instead

#df1 = pd.read_csv('person_education.csv')
#df2 = pd.read_csv('person_work.csv')

#They are merged based on their id's
#Pandas example uses an inner join. https://www.geeksforgeeks.org/different-types-of-joins-in-pandas/
#Inner join is the most common type of join you’ll be working with. It returns a Dataframe with only those rows that have common characteristics.

#df_merge = pd.merge(df1,df2,on='id')

#Remove the redudant iris stuff out.
#df['class'] = df['class'].str.replace('Iris-','')

# outerjoin.
#An outer join returns all the rows from both dataframes. If there is no match for a row in either dataframe, the missing values will be filled with NaNs. Left and Right Joins are possible too.
#df_merge_outer = pd.merge(df1, df2, on='id', how='outer')

##Filtering Data
#df = pd.read_csv('country_data_index.csv')
#print(df[df['Age']<30])

df = pd.read_csv('iris.csv')
df['class'] = df['class'].str.replace('Iris-','')

#print(df[df['sepal_length']>5])

#more permanent method
df = df[df['sepal_length']>5]
df = df[df['class'] == 'virginica']

## Export the data to csv, excel or whatever
df.to_csv("iris_data_cleaned.csv")

##Without the Pandas indexed column
df.to_csv("iris_data_cleaned_noIndex.csv", index=False)

##Excel
df.to_excel("iris_data_cleaned.xlsx", index=False, sheet_name='Sheet1')

##JSON
df.to_json("iris_data_cleaned.json", orient='records')






