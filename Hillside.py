# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 16:19:08 2020

@author: bkeight
"""

# Libraries required

#import random
#import operator
import matplotlib
import matplotlib.pyplot
import matplotlib.animation 
import os
#import pathlib
#import csv
#import tkinter
#import requests
#import bs4
#import pandas

# Variables required

DEM = []
row = 0
column = 0

# Operating system info
# sys = os.name
workdir = 'C:\\MSc\\Module3\\Python Code\\src\\unpacked\\adm\\Assignment2'
workfile = 'snow.slope'
workarea = os.path.join(workdir, workfile)

# Main

# Check file exists and read in data file into Lists

if os.path.isfile(workarea):
    print('Working')
else:
    print('File not found, exiting')
    exit()

File = open(workarea)    # Open file

# Create a DEM List

for Line in File.readlines():
    rowlist = []    # Create blank list
    for value in Line.split():    # A list of value
        rowlist.append(int(value))
    column += 1
    row = len(rowlist)
    DEM.append(rowlist)
File.close()    # close files

# Display the DEM

matplotlib.pyplot.xlim(0, row) # Set the extent of the Y axis
matplotlib.pyplot.ylim(0, column) # Set the extent of the X axis
display = matplotlib.pyplot.imshow(DEM)
matplotlib.pyplot.show(display)
print('end')
