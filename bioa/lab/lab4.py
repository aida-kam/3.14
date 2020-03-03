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

# # Lab work 2020-02-27
#
# Import packages

import math
from time import sleep
import matplotlib.pyplot as plt


# ---
# >> **TASK**
# >>
# >> Examine all types of operators, create a few example calculations with all of them
# >>
# ---
#
# ## Basic operators
#
# Basic operators help as with calculations
#
#
#
# sum +
#
# difference -
#
# multiplication *
#
# power to **
#
# division producing floats /
#
# division producing integers //
#
# reminder of division %

2 + 2

2 - 2

2 * 2

2**3

2 / 3

2 // 3

2 % 3

35 % 10


# ## Logical operators
#
# These operators allow as to compare values and form sentences
#
# less <
#
# more >
#
# equal ==
#
# not equal !=
#
# less or equal <=
#
# checks if both are true `and`
#
# checks if one of choices is true `or`
#
# reverses result `not`
#

a = True
b = False

print(a and b)

print(a or b)

print(not a)

# ## IF statement
#
# The most important element in creating logic. If (if) something is true do an action if something else is true (elif) do different action otherwise (else) do this action
# else and elif are not necessary

if 5 > 6:
    print(1)

# Change x to some other number and explore how program behaves

x = 0
if x < 0:
    x = 0
    print("Negative changed to zero")
elif x == 0:
    print("Zero")
elif x == 1:
    print("Single")
else:
    print("More")

# if else statements form  program logic. Lets create function to convert fahrenheit and inches to metric system


def convert_to_SI(value, type="temp"):
    if type == "temp":
        celsius = (value - 32) * 5 / 9
        kelvin = celsius + 273.15
        return round(celsius), round(kelvin)
    elif type == "dist":
        meters = value * 0.0245
        return meters
    else:
        print("Type is not defined")


convert_to_SI(40)

convert_to_SI(40,'dist')

convert_to_SI(40,'temp')

# ---
# >> **TASK**
# >>
# >> Make new function `convert_to_SI2(value,type,measurement)`. Function should give either celsius or kelvin temperature depending on measurement variable. Following statements should not give error
# >>
# ---





convert_to_SI2(10, "temp", "celsius")

convert_to_SI2(10, "dist", "celsius")


# # FOR
#
# For statement is essential in data analysis. `for` allows as to iterate over elements

for x in [1, 2, 3]:
    print(x)

# Create new lists (imagine how many lines the same logic would require without for)

values_in_fahrenheit = [0, 44, 56, 788]
values_in_celsius = []
values_in_kelvin = []
for value in values_in_fahrenheit:
    cel, kel = convert_to_SI(value)
    values_in_celsius.append(cel)
    values_in_kelvin.append(kel)


values_in_kelvin

values_in_celsius


# ## RANGE
#
# Instead of writing numbers out ranges can be created with function `range`
#
# range([start], stop[, step])

for i in range(4):
    print(i)


a_range = range(-10, -100, -30)
a_range

#  To convert range to list

a_list = list(range(4))
a_list

# i is assigned at the beginning of every loop

for i in range(4):
    print(i)
    i = 10
    print(i)


def progress(percent=0, width=30):
    left = width * percent // 100
    right = width - left
    print(
        "\r[",
        "#" * left,
        " " * right,
        "]",
        f" {percent:.0f}%",
        sep="",
        end="",
        flush=True,
    )


for i in range(101):
    progress(i)
    sleep(0.1)

# ---
# >> **TASK**
# >>
# >> Explore the loop in previous script. Make it run faster from 0 to 100 without changing sleep time
# >>
# ---







# ### For with dictionaries

data = {"-18": "255", "7": "280"}
for k, v in data.items():
    print(f"Celsius: {k}, Kelvin {v}")

# ### enumerate
#
# For with enumerate is much easier to read and get elements we want from arrays
#
# enumerate(iterable, start=0)

a = ["a", "b", "c"]
for i, v in enumerate(a):
    print(i, v)

for i in range(len(a)):
    print(i, a[i])


str = "Python"
for idx, ch in enumerate(str):
    print(f"index is {idx} and character is {ch}")

#  Enumerate is very useful when we have to take elements from other structures with the same index for example if we have data array:

data = [1, 2, 3]

#  and name list

names = ["A", "B", "C"]

for idx, ch in enumerate(names):
    print(f"data {data[idx]} belongs to name {names[idx]}")


#  ### zip function helps us to combine different lists

for q, a in zip(values_in_fahrenheit, values_in_celsius):
    print(f"Temperature in celsius {a} equals {q} in fahrenheit")

#  What will happen if elements are not of equal size?

for q, a in zip(values_in_fahrenheit, values_in_celsius[1:2]):
    print(f"Temperature in celsius {a} equals {q} in fahrenheit")

# ### reverse lets to count from other end

for i in reversed(range(1, 10, 2)):
    print(i)

#  ## while
#
# While allows to create loops of infinite size until condition is reached

a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a + b

import random

x = 0
while x < 0.9:
    x = random.random()
    print(x)


#  ## break and continue
#
# For finer control break and continue lets as skip some iterations

for n in range(2, 10):
    print(f"n {n}", flush=True)
    for x in range(2, n):
        print(f"x {x}", flush=True)
        if n % x == 0:
            print(n, "equals", x, "*", n // x)
            break
    else:  # for loop condition else is evaluated if no break was encountered
        print(n, "is a prime number")

# ---
# >> **TASK**
# >>
# >> Explore prime detection function. Inserting print statements inside logic might help to understand the program
# >>
# ---


#  ## pass
#
# pass does nothing, but sometimes thats what you what on certain conditions

for i in range(4):
    pass

# # Bitwise operators
#
# AND &
#
# OR |
#
# NOT ~
#
# XOR ^
#
# right shift >>
#
# left shift <<

# ## AND
#  x & y
#  Does a "bitwise and". Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0.

1 & 2

3 & 9


# ## OR
#
#  x | y
#  Does a "bitwise or". Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1.


1 | 3

# ## NOT
#  ~ x
#  Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1. This is the same as -x - 1.

~3

# ## XOR

#  x ^ y
#  Does a "bitwise exclusive or". Each bit of the output is the same as the corresponding bit in x if that bit in y is 0, and it's the complement of the bit in x if that bit in y is 1.
#  Used in checksums


3 ^ 2

3 ^ 14

#  ## Left shift

#  x >> y
#  Returns x with the bits shifted to the right by y places. This is the same as dividing x by 2**y.

8 >> 1

# ## Right shift

#  x << y\
#  Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). This is the same as multiplying x by 2**y.

4 << 1


# ---
# >> **TASK**
# >>
# >> Write a program that prints the numbers from 1 to 100. But for multiples of three print “op” instead of the number and for the multiples of five print “pa”. For numbers which are multiples of both three and five print “op pa pa”."
# >>
# >>
# ---















# ---
# >> **TASK**
# >>
# >> Write a program that generates sinusoid wave by the formula y = sin(2*pi * t * f), where y is final wave, f is frequency of the wave and t is time.
# >>
# >> - first create time points array, then iterate other it and calculate values according to formula (t is in seconds so values should be small for higher frequencies >1 and integers for lower frequencies)
# >>
# >> - plot with function plt.plot(t,y)
# >>
# ---









t











































#  Answers


# def convert_to_SI2(value, type="temp", measurement="celsius"):
#     if type == "temp" and measurement == "celsius":
#         celsius = (value - 32) * 5 / 9
#         return round(celsius)
#     elif type == "temp" and measurement == "kelvin":
#         kelvin = celsius + 273.15
#         return round(kelvin)
#     elif type == "dist":
#         meters = value * 0.0245
#         return meters
#     else:
#         print("Type is not defined")


#


# def progress(percent=0, width=30):
#     left = width * percent // 100
#     right = width - left
#     print(
#         "\r[",
#         "#" * left,
#         " " * right,
#         "]",
#         f" {percent:.0f}%",
#         sep="",
#         end="",
#         flush=True,
#     )

# for i in range(0, 101, 2):
#     progress(i)
#     sleep(0.1)

#

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)





# y = []
# t = list(range(0,1000))
# f = 0.01 # Hz
# for x in t:
#     #x=x/1000
#     y.append(math.sin(2*math.pi*x*f))
#     
#     
# plt.plot(t,y)


