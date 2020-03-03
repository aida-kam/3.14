# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_markers: '{{{,}}}'
#     cell_metadata_filter: -all
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.4'
#       jupytext_version: 1.2.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Lab work 2020-02-20

# [Best up-to-date python tutorial](https://docs.python.org/3.7/tutorial/index.html)

# ## Packages
#
# When starting python document importing of packages usually go first. These packages extend programs with previous work done by us or somebody else.

# For example here we import math package. It has a lot of functions helping with variuos math problems. For example the definition of pi can be accessed by executing `math.pi`

import math

# ## Calculator
# Lets use python as a calculator and do some basic math:

2+2

math.sqrt(4)

3**2

6/2

# ---
# >> **TASK**
# >>
# >> In python REPL (REPL is the language shell, the Python Interactive Shell. The REPL acronym is short for Read, Eval, Print and Loop) write `math.` and then press `TAB`. Pressing tab in ipython will reveal implemented functions in math package. Explore them, try to implement basic math operators (Find sin, cos, log, exponentof number 42).
# >>
# ---


# ## IPython

# IPython gives many useful functions to basic python REPL.
# Very important addition is easy access of functions documentation with `?`. Try to access documentation of basic math functions.

math.sin?

#  Full documentation can be accessed with help

help(math)

# Ability to run bash commands and quickly explore the contents of the current directory is very handy during data analysis
# Just like in bash we can get current directory with:

pwd

# The contents of current directory with:

# # ls -a

# and so on...

# Other useful addition is workspace control. We always can get the previous outputs and inputs by their name.

In[-9]

# As you can see to get the output of the output or input number X one could write In[X] or Out[X]. But it is possible to go from the last elements and reverse the numbering --- last element is Out[-1] second before last Out[-2] and so on

#  If one would like to get first three Inputs:

In[1:5]

# The colon operator slices from number x to y in this case from 1 to 5.
#  
# Remember that python counts from 0 so the first element is at 0

#  These shortcuts can lead to faster and smoother data exploration

# ---
# >> **Task**
# >>
# >> - Test IPython magical functions. `%lsmagic`, `%magic` and `alias`
# >>    - Find out the directory you are in.
# >>    - Navigate to ~/Documents/bioa/ directory.
# >>
# >>
# ---

#  When writing code it is important to write comments to make it easier for you (in a week) or other persons to read and understand it. Comments  in python are written after a hash tag # and they are ignored by python interpreter. When writing in JupyterLab notebook it is better to make comments in markdown cells.

# {{{
# python will ignore this
# pwd
# }}}

# ## Data types

# Lets make a Celsius to Fahrenheit converter. The basic formula for conversion is y = (x × 9/5) + 32
#
# where y is temperature in Fahrenheit and x temperature in Celsius.
#
# Lets find out what is in the temperature in Fahrenheit when temperature in Celsius is 100C.
#
# First we could simply write out the formula like that:

(100 * 9/5) + 32


# For later use we could create a variable in memory that would store the result:

Fahrenheit = (100 * 9/5) + 32
Fahrenheit

# Now variable Fahrenheit stores the results of that operation.
#
# There are a couple variable types in python for number storage. The simplest `int` (Integer) represents real integer numbers.
#
# Our created variable Fahrenheit is a `float` -- it has higher precision then `int` but for that it occupies more space in memory. We can find out the type of the variable by writing

type(Fahrenheit)

# We can also change the type by casting it to other type

int(Fahrenheit)

# Take note that Fahrenheit  variable was not changed you have to assign the output of the operation to change it


Fahrenheit = int(Fahrenheit)
Fahrenheit

# There are 5 core variable types

# Integer

10

#  Float

3.14

# it is possible to use scientific notation with floats

4e2

# Boolean - True and False or 1 and 0

type(True)

# Complex

type(3 + 4j)

# String

message = 'Hello world'
message

#  And 4 compound types for multiple variable storage

# List

[1,2,3]

# Tuple

(1,2)

# Set

{1,2}

# Dictionary

{'key':'value'}

#  We will explore them in more detail later

# In IPython we can get all objects in current workspace by typing:

who

# We can clear all variables in workspace with `reset`

# ---
# >> **TASK**
# >>
# >> - Explore the documentation of reset and find a way to clear only one variable. Clear Fahrenheit but keep the rest.
# >>
# ---

# ## Functions

# If we want to use the same formula more then once it is wise to create a shortcut. It can be done by creating functions.


def celsius_to_farenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return round(fahrenheit)


# Here we created a function that will convert temperature given in Celsius to Fahrenheit. In addition it will round the value with the built-in python method `round`.
#
# Functions are defined with keyword `def` and have a basic form:


def functionName(inputVariable):
    #  somethingis done here
    return something

# Remember python is sensitive to indentation!

# Now if we want to get the temperature in Fahrenheit of 100 Celsius we simply write


celsius_to_farenheit(100)

# Lets say we want to calculate temperature for 100 110 and 200 Celsius and store it in one variable. For this task we have lists. Lists are created with square brackets [] and can have mixed type inputs inside. Lists are mutable (it is possible to change them) and ordered (the order items are added is important)

ListA = [celsius_to_farenheit(100), celsius_to_farenheit(110), celsius_to_farenheit(200)]
ListA

# To get the size of the list:

len(ListA)


#  Lists are one of the most useful storages in python. They have many methods to work with. You can get all methods by pressing TAB in ipython after writing variable name and a dot .

ListA.

# ### The methods:

# Append - adds element to list

ListA.append(2)
ListA

# To sort elements in the list

ListA.sort()
ListA

# Extend -- appends iterable elements (for now think of them as lists and specific iterable functions)

ListA.extend([1, 2, 3])
ListA

#  If we append the list [10,11,12], the whole list is added to the end while with extend we iterate over the list and add elements by one

ListA.append([10, 11, 12])
ListA


# count returns number of occurrences of given value in the list

ListA.count(2)

# To insert object (number 2) before index 1

ListA.insert(1, 2)
ListA

# to reverse value order in the list

ListA.reverse()
ListA

# Pop removes and returns an item from the list at given index (default = last)

ListA.pop(2)
ListA

# After pop displays/returns the number it is removed from the list

# Copy - returns a shallow copy of the list.

ListB = ListA.copy()

ListA.append(2)
ListA

ListB

#  If we simply create copy by assignment

ListC = ListA
ListC

ListA.append(88)
ListA

ListC

#  we observe that both ListA and ListC changes as ListC is not a separate copy but just a pointer

# Index -- returns first index of the given value

ListA.index(3)

# Remove -- removes first occurrence of the value

ListA.remove(88)
ListA

# clear - clears all items from list

ListA.clear()
ListA


#  You can get elements in the list by their index

ListB[0]

ListB[3]

ListB[-1]

#  Or by slicing the indexes

ListB[0:2]

#  Lists implement some math operators like:

ListB * 2

ListB + ListB

#  Lists can have lists inside lists (nested lists)

ListC = [ListB, ListB]

# To access first list in ListB:

ListC[0]

# To access second item in first list in ListB:

ListC[0][1]


# ---
# >> **TASK**
# >>
# >> - Get numbers 78, 55, 0, 45 from the list `TestList`
# >>
# ---

TestList = [1, [79, 77, 78], 0, [2, [45, 65], 55], 4]








# Now lets change our function so it would return back Fahrenheit and Kelvin values


def celsius_to_farenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius - 273.15
    return round(fahrenheit), round(kelvin)


output = celsius_to_farenheit(42)
output

#  Variable `output` is called tuple. It is immutable

output[1] = 3

# The most useful tuple property for us right now will be unpacking

fah, kel = output
kel

fah


#  we could do the unpacking at the moment of function execution

fah, kel = celsius_to_farenheit(42)


#  Tuples work faster then lists, are immutable (you can not accidentally change the value) and are often used to form dictionaries

# To store all the information in a more organized way we can use a dictionary

#  Dictionary is defined by key and value pair `{key: value}`. Keys must be unique and immutable (tuple, integer, string float, boolean). Values in the dictionary are accessed by the unique key. Values are not restricted.

temperature = {}
cel = 34
fah, kel = celsius_to_farenheit(cel)
temperature[cel] = fah, kel

cel = 4
fah, kel = celsius_to_farenheit(cel)
temperature[cel] = fah, kel

cel = -9
fah, kel = celsius_to_farenheit(cel)
temperature[cel] = fah, kel

temperature

temperature[4]

#  To get all the items in the dictionary use items method

temperature.items()

# To get the keys

temperature.keys()

#  Values given the key can be accessed with get method

temperature.get(4)

#  There are many ways to create dictionaries:

# using curly brackets

dictA = {'key1':'value1','key2':'value2'}
dictA.keys()

dictA['key1']

# using dict keyward

dictA = dict(key1 = 'value1', key2='value2')
dictA

# using lists of tuples

dictA = dict([('key1','value1'),('key2','value2')])
dictA


#  The last type is SET. It is a mutable collection of unique unordered values.
#  
# Using sets we can perform variuos logical operations. For example if we have a list of numbers

s = [1,1,1,2,3,5,5]

# converting it to set will leave only unique values

ss = set(s)
ss


# The methods of sets:

rr = set([2,4,6,5])

rr.difference(ss)  # difference between sets

rr.intersection(ss)  # returns common elements

rr.issubset(ss)  # checks if one set is a subset of other

rr.union(ss)  # unites both sets

rr.add('k')  # adds elements
rr

rr.clear()  # removes all elements
rr

# check set help for more methods

help(set)


# ---
# >> **TASK**
# >>
# >> - Explore dictionary, set and tuple methods
# >>
# ---


# ## Printing

#  Finally we want to display the temperature values with some text explaining them. Variable storing text in python is called a string. Strings are defined inside quotation marks.

stringA = "This is string A"
stringA

stringB = 'This is string B'
stringB

# Like lists strings have methods and operations. But stings are immutable and every time we do something with them new objects are created in memory.

# To change all letters to lower case use:

stringA.lower()

# to change all letters to uppercase

stringA.upper()

# + and * combines strings

stringA + stringB

stringA * 2

# But it is better to use join method. It accepts a list of strings and joins them with a separator. In this case we give empty space as a separator ' '.

' '.join([stringA, stringB])

# Split strings into parts with split method

stringA.split()

# ---
# >> **TASK**
# >>
# >> - Explore string methods
# >> [full list of methods](https://docs.python.org/3.7/library/stdtypes.html#string-methods)
# >>
# ---

# ## Printing

# Built in function `print` formats strings and other variables into text and displays it

print(stringA)

print(stringA, stringB)

# Old way to perform string formatting:

"Celsius, %s. Fahrenheit %s." % (cel, fah)  # % operator

"Celsius, {0}. Fahrenheit{1}.".format(cel, fah)  # str.format method

# It is possible to combine everything with print

print('Temperature in Celsius', cel, 'Fahrenheit ', fah, sep=' ', end='\n', flush=False)

# From version 3.6  python supports the fString and rString strings which are easiest to use.

#  fStrings replaces curly brackets into variable values:

f'Temperature in Celsius {cel}'

# rString prints everything ignoring the special characters

r'Temperature in Celsius {cel}'

#  For all types of formating these special characters can help to present text:
#
# |special char|displayed|
# |-----------|----------|
# |\t|tab|
# |\n|new line|
# |\r|Enter, return|
# |\b|back|
# |\\|backslash \|
# |\'|quotation mark|
# |\"|double quotation mark|

print(f'Temperature\nCelsius {cel}\t Fahrenheit {fah}')




from time import sleep
def progress(percent=0, width=30):
    left = width * percent // 100
    right = width - left
    print('\r[', '#' * left, ' ' * right, ']',
          f' {percent:.0f}%',
          sep='', end='', flush=True)


# we will learn flow control next time
for i in range(101):
    progress(i)
    sleep(0.1)

# ---
# >> **TASK**
# >>
# >> - Change progress function to get the display shown below
# >>
# ---


# {{{ {"active": ""}
# [  # ] 5%
# [  # ] 6%
# [  # ] 7%
# [  # ] 8%
# [  # ] 9%
# [  # ] 10%
# [  # ] 11%
# [  # ] 12%
# }}}



# ## Plotting

# Finally we need some basic plotting to plot the values we will get. Python has a lot of libraries for this purpose and we will learn the most important ones step by step.
# For now we will use the core library matplotlib

#  First we have to import it

import matplotlib.pyplot as plt

# Then we create a figure <plt.figure>,
# add plots <plot(x,y)>,
# and labels

plt.figure(figsize=(20,3)) # creates figure of preferred size
plt.plot(list(temperature.keys()),'r+') # convert keys to list and plot in red color as + signs
plt.plot(list(temperature.values()),'o') # convert values to list and plot as o signs
plt.legend(['Celsius','Fahrenheit','kelvin']) # add legend with values
plt.title("Temperatures") # Add title
plt.ylabel("Degrees") # Add y label
plt.xlabel("Measurements") # Add x label

# ---
# >> **TASK**
# >>
# >> - Make a plot of a list [1,2,3,4]
# >>
# ---


