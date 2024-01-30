# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 08:57:40 2024

@author: Louise
"""


print("my first Python file")
# kommentaar 

age = [30,40,30,49,22,35,22,46,29,25,39]

print(min(age))
print(max(age))
print(len(age))
print(sum(age))

average = sum(age)/len(age)
print(average)

#C2 = "M"
#C3 = "M"
#C4 = "F"

genderlist = ["M","M","F","M","F","F","F","M","M","F","M"]
print(genderlist[0])
print(genderlist[1])
print(genderlist[2])
print(genderlist[-1])


#country list
country = ['South Africa', "Botswanna", "South Africa",  "South Africa", "Kenya", "Mozambique","Lesoto","Kenya","Kenya","Egypt","Susdan"]
print(country)
print(country[0])
print(country[5])

# Data Storage with lists
my_list = [42, -2021, 6.283, "tau","node"]
print(my_list)
print(my_list[:])

my_list.append("pi")
print(my_list)

my_list.insert(1,"Pi2")
print(my_list)

my_list.remove("pi")
my_list.remove("Pi2")
my_list.remove("tau")
print(my_list)
print(len(my_list))

print(my_list[0:3])


# Dictonaries

d = {'key1' : 'value1', 'key2' : 'value2'}
person = {'name': 'John Doe', 'age' : 30, 'address' : '123 Main St.'} 
print(person['name']) 
print(person.get('age'))
person['phone'] = '555-555-5555'
print(person['phone'])




