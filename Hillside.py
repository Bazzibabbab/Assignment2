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
import slope
#import pathlib
#import csv
#import tkinter
#import requests
#import bs4
#import pandas

# Variables required

dem = []
demslope=[]
row = 0
column = 0
cell_count = 0
r = 0
c = 0

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
    cell_count = row * column
    dem.append(rowlist)
File.close()    # close files

# Calculate Slope of DEM

for line in dem:
#    print(line)
    for inst in line:  # Repeat for number of cells in DEM
#        print(inst)
#        print('r=', r)
#        print('c=', c)
        if r > 0 and r < row-1 and c < column-1 and c > 0:
#            print('ctr=', dem[r][c])
            demslope.append(slope.Cell(dem[r-1][c-1], dem[r-1][c], dem[r-1][c+1], dem[r][c-1], inst, dem[r][c+1], dem[r+1][c-1], dem[r+1][c], dem[r+1][c+1]))    # Pass 3x3 grid about cell to calculate slope
        c += 1
    r += 1
    c = 0

# Display the DEM
'''
matplotlib.pyplot.xlim(0, row) # Set the extent of the Y axis
matplotlib.pyplot.ylim(0, column) # Set the extent of the X axis
display = matplotlib.pyplot.imshow(DEM)
matplotlib.pyplot.show(display)
'''
print('end')
