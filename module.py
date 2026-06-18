#MATH MODULE
'''
import math 

print(math.pi)
print(math.sqrt(49))
print(math.pow(2,3))

from math import sqrt
print(sqrt(25))


#RANDOM MODULE

import random
print(random.randint(1,20))

import string
random_letter=random.choice(string.ascii_letters)
print(random_letter)

small_letter=random.choice(string.ascii_lowercase)
print(small_letter)

capital_letter=random.choice(string.ascii_uppercase)
print(capital_letter)

list=[1,2,3]
print(random.choice(list))

# TRY OUT MULTIPLE RANDOM GENERATION
# TRY OUT SECRET MODULE eg->otp generation

import datetime
print(datetime.datetime.now())
print(datetime.date.today())
print(datetime.date.today()-datetime.timedelta(1))

#try out random dates in between specific dates


import sys
print(sys.platform)
print(sys.version)

import os 
print(os.getcwd())
print(os.listdir())

#ALIASING TEMPORARY NAME

import datetime as dt
print(dt.datetime.now())

#THIRD PARTY LIBRARY

import requests
url=requests.get('https://jsonplaceholder.typicode.com/users/2')
print(url.json())'''


