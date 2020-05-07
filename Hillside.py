# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 16:19:08 2020

@author: bkeight
"""

# Libraries required

import matplotlib
import matplotlib.pyplot
import matplotlib.animation 
import os
import math

# Variables required

dem = []        # Blank list to receive DEM into
demslope=[]     # Blank list to copy DEM slope data into
row = 0         # Initialise variable for row counting
column = 0      # Initialise variable for column counting
cell_count = 0  # Initialise variable to hold count of cells in DEM
r = 0           # Possibly replace with row
c = 0           # Possibly replace with column

# Operating system info
# Look at OS and setting directory delimiter so code works on multiple platforms
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
#    print('line')
    rowlist=[]
    for inst in line:  # Repeat for number of cells in DEM
        if r > 0 and r < row-1 and c < column-1 and c > 0:
#            print('ctr=', dem[r][c])
            rowlist.append(int(calculate(dem[r-1][c-1], dem[r-1][c], dem[r-1][c+1], 
                                      dem[r][c-1], inst, dem[r][c+1],
                                      dem[r+1][c-1], dem[r+1][c], dem[r+1][c+1])))    # Pass 3x3 grid about cell to calculate slope
        else:
            rowlist.append(0)
        c += 1
    demslope.append(rowlist)
    r += 1
    c = 0

def calculate(a, b, c, d, ctr, f, g, h, i):
    # Calculate delta x of central cell
#        print('middle=', ctr)
    deltax = ((c + 2*f + i) - (a + 2*d + g)) / 8
#        print(deltax)
        # Calculate delta y of central cell
    deltay = ((g + 2*h + i) - (a + 2*b + c)) / 8
#        print(deltay)
    slope_rate = math.sqrt((deltax**2)+(deltay**2))
#    print(slope_rate)
    slope_deg = math.atan(slope_rate) * (180/math.pi)
#    print(slope_deg)
    return(slope_deg)


# Display the DEM
matplotlib.pyplot.xlim(0, row) # Set the extent of the Y axis
matplotlib.pyplot.ylim(0, column) # Set the extent of the X axis
#dem_img = matplotlib.pyplot.imshow(dem)
#matplotlib.pyplot.show(dem_img)
slope_img = matplotlib.pyplot.imshow(demslope)
matplotlib.pyplot.show(slope_img)
print('end')
