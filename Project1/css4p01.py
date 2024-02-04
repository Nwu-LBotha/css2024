# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 20:55:11 2024

@author: Louise
"""

import pandas as pd

df = pd.read_csv("movie_dataset.csv")
#df.info()
df.describe()

#Question1
##What is the highest rated movie in the dataset?

max_rating = df['Rating'].idxmax()

# Extract the movie name corresponding to the highest rating
highest_rating = df.loc[max_rating, 'Title']
#print(highest_rating)
#The Dark Knight

#Question2
##What is the average revenue of all movies in the dataset? 
## Note, since the answer will be effected by how you dealt 
## with missing values a range has been provided. 

#averageRev = df["Revenue (Millions)"].mean()  ##Also works.
df.dropna(subset=["Revenue (Millions)"])
df.reset_index(drop=True)
#print(df["Revenue (Millions)"].mean())
# Between 70 and 100 Million

#Question 3
## What is the average revenue of movies from 2015 to 2017 in the dataset?
## Note, since the answer will be effected by how you dealt with missing values 
## a range has been provided. 

movies_2015_2017 = df[(df['Year'] == 2015) | (df['Year'] == 2017)]
movies_2015_2017.dropna(subset=["Revenue (Millions)"])
movies_2015_2017.reset_index(drop=True)
#print(movies_2015_2017["Revenue (Millions)"].mean())
#Between 50 and 80 Million

#Question 4
# No of movies released in 2016

movies_2016 = df[(df['Year'] == 2016)]
Nomovies_2016 = len(movies_2016)
#print(Nomovies_2016)
#297



# Question 4
# How many movies were directed by Christopher Nolan? 

nolan = df[df['Director'] == 'Christopher Nolan']
count_Nolan = len(nolan)
#print(count_Nolan)
#5

# Question 5
#How many movies in the dataset have a rating of at least 8.0?
Rating_8 = df[df['Rating'] >= 8.0]
My_8_rating = len(Rating_8)
#print(My_8_rating)
#78


#Question 7
#What is the median rating of movies directed by Christopher Nolan?

nolan_median = nolan['Rating'].median()
#print(nolan_median)
#8.6

#Question 8
#Find the year with the highest average rating?

yearly_average = df.groupby('Year')['Rating'].mean()
#print(yearly_average)

higest_avg_rating = yearly_average.idxmax()
#print(higest_avg_rating)
#2007

#Question 9
#What is the percentage increase in number of movies made between 2006 and 2016

movies_2006 = df[df['Year'] == 2006]
movies_2016 = df[df['Year'] == 2016]

no_movies_2006 = len(movies_2006)
no_movies_2016 = len(movies_2016)

percentage_increase = ((no_movies_2016 - no_movies_2006) / (no_movies_2006) * 100)
#print(percentage_increase)
#575

#Question 10
##"""Find the most common actor in all the movies?
##Note, the "Actors" column has multiple actors names. 
##You must find a way to search for the most common actor in all the movies."""

all_the_actors = df.groupby('Actors')
#for actors_list in df['Actors']
# Dont know, Guessed Matthew McConaughey

#print(all_the_actors)

#Question 11
##"""How many unique genres are there in the dataset?
##Note, the "Genre" column has multiple genres per movie.
## You must find a way to identify them individually."""
 
 
genre_splitted = df['Genre'].str.split(',', expand=True)
num_unique_genres = len(set(genre_splitted))
print(num_unique_genres)

#15

#Question 12
##"""Do a correlation of the numerical features, what insights can you 
##deduce? Mention at least 5 insights.
##And what advice can you give directors to produce better movies?"""

print(df.describe())


movies_2007 = df[(df['Year'] == 2007)]
Nomovies_2007 = len(movies_2007)
print(Nomovies_2007)

movies_2008 = df[(df['Year'] == 2008)]
Nomovies_2008 = len(movies_2008)
print(Nomovies_2007)

movies_2009 = df[(df['Year'] == 2009)]
Nomovies_2009 = len(movies_2009)
print(Nomovies_2009)

movies_2010 = df[(df['Year'] == 2010)]
Nomovies_2010 = len(movies_2010)
print(Nomovies_2010)

movies_2011 = df[(df['Year'] == 2011)]
Nomovies_2011 = len(movies_2011)
print(Nomovies_2011)

#Question 13
##"""Once you have completed the Quiz questions, 
##create a public GitHub repository and upload a single python 
##file called "css4p01.py" to it. Share the url ink for 
##the your python file below. The code must show all the code used to 
##load, analyse and clean the data, as well how you answered the Quiz 
##questions. Make reasonable assumptions.""" 
