# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 16:19:08 2020

@author: bkeight
"""

# Libraries required

import random
import operator
import matplotlib
import matplotlib.pyplot
import matplotlib.animation 
import agentframework
import os
import pathlib
import csv
import tkinter
import requests
import bs4

# Variables required

# Main

# Read data from webpage

r = requests.get('https://www.geog.leeds.ac.uk/courses/computing/study/core-python-odl2/assessment2/snow.slope')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})

# Read in data file into Lists
'''
f = open('./in.txt', newline='')    # Open file
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)    # Read file in with CSV library
for row in reader:    # A list of rows
    rowlist = []    # Create blank list
    for value in row:    # A list of value
        rowlist.append(value)   # Append each value read to new list
    environment.append(rowlist)     # Append list to new list
f.close()    # Don't close until you are done with the reader;
# data is read on request.
'''