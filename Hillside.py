# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 16:19:08 2020

@author 201387513

This program reads in a file called snow.slope and calcultes the slope from the DEM within it.
The resulting DEM and Slope images are displayed through a Tk window

"""

#
# Libraries required
#

import matplotlib
import matplotlib.pyplot as plt
import os
import math
import tkinter as tk

#
# Variables required
#

dem = []        # Blank list to receive DEM into
demslope=[]     # Blank list to copy DEM slope data into
row = 0         # Initialise variable for row counting
column = 0      # Initialise variable for column counting
cell_count = 0  # Initialise variable to hold count of cells in DEM
r = 0           # Possibly replace with row
c = 0           # Possibly replace with column
matplotlib.use('TkAgg') # Change the backend of matplotlib
fig = plt.figure(figsize=(7, 7))

# Operating system info
# Look at OS and setting directory delimiter so code works on multiple platforms

workdir = 'C:\\MSc\\Module3\\Python Code\\src\\unpacked\\adm\\Assignment2'
infile = os.path.join(workdir, 'snow.slope')
outfile = os.path.join(workdir, 'slope.txt')

#
# Functions used in code
#

# Calculates the Slope Rate and Slope Degrees of a cell using
# slope_degrees = ATAN ( √ ([dz/dx]2 + [dz/dy]2) ) * 180/pi

def calculate(a, b, c, d, ctr, f, g, h, i):
    deltax = ((c + 2*f + i) - (a + 2*d + g)) / 8    # Calculata deltaX
    deltay = ((g + 2*h + i) - (a + 2*b + c)) / 8    # Calculate deltaY
    slope_rate = math.sqrt((deltax**2)+(deltay**2)) # Calculate Slope rate from deltaX & deltaY
    slope_deg = math.atan(slope_rate) * (180/math.pi)   # Calculate slope degree from Slope rate
    return(slope_deg)   # Return value

#
# Button calls for Tk interface
#
    
# Creates a button that will display an DEM image of the input file
    
def disp_dem():
    image = plt.imshow(dem)
    canvas.draw()

# Creates a button that will dsiplay the resulting slope data as an image

def disp_slope():
    image = plt.imshow(demslope)
    canvas.draw()

#
# Main
#
# This is the main body of the program which will define the working path and input file.
# The file is read into an array using lists. This is then used to feed into the "calculate" function
# The resulting data is feedback into a new list array to produce a slope file.
# A Tk interface is used to display either of the images.    
#
    
# Check file exists and read in data file into Lists

if os.path.isfile(infile):
    print('Working')
else:
    print('File not found, exiting')
    exit()

File = open(infile, "r")    # Open file

#
# Read in each line one at a time from the input file and extract each value from it and add to
# the end of a list. Append each new row to a list array to create a DEM. Release the file on
# completion
# 

for Line in File.readlines():   # Repeat for each line in file
    rowlist = []    # Create blank list
    for value in Line.split():    # Repeat for each value in line
        rowlist.append(int(value))  # Append current value to list
    row += 1 # Increment the count of rows in DEM
    column = len(rowlist)  # Return the number of cells in x axis
    cell_count = row * column # Return the pixcel size of DEM
    dem.append(rowlist) # Append the list to the new DEM
File.close()    # close files

#
# Calculate Slope of DEM
# To calculate slpoe of a cell the surrounding 8 cells need to be utilised.
# The boundary cells can not be utilised as they are mising some of the 8 required.
# Therefore the boundary cells are ignored and set to zero in the output file
# The 9 cells are passed to the Calculate function for processing and the result is
# is returned and added to a new list array. The resultant slope data is written to
# a new file.
#


Output = open(outfile, "w") # Open file ready to be overwritten
for line in dem:    # for each line in the input file
    rowlist=[]      # initialise the list 
    for inst in line:  # Repeat for number of cells in DEM
        if r > 0 and r < row-1 and c < column-1 and c > 0:  # if the cell is not an edge cell
            rowlist.append(int(calculate(dem[r-1][c-1], dem[r-1][c], dem[r-1][c+1], 
                                      dem[r][c-1], inst, dem[r][c+1],
                                      dem[r+1][c-1], dem[r+1][c], dem[r+1][c+1])))    # Pass 3x3 grid about cell to calculate slope
        else:
            rowlist.append(0)   # Fill the boundry cell with a zero
        c += 1  # increment the column count
    demslope.append(rowlist)    # append the completed row to the new list
    Output.write("%s\n" % rowlist)   # Write the row contents to the output file
    r += 1  # increment the row count
    c = 0   # reset the column count

Output.close()  # close the output file after all data has been added

#
# Display the DEM
# Using the tk gui module to create and display a window that will have 3 options
# Display original DEM
# Display new slope image
# Quit
#

root = tk.Tk() # Create a new window
root.wm_title("To the Max! (...imum Gradient...)")  # give the new window a name
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)  # set the canvas up
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)  # set how the canvas will look
menu_bar = tk.Menu(root)   # Create a pulldown menu class
root.config(menu=menu_bar)  # Use the option menu_bar to create the new menu
model_menu = tk.Menu(menu_bar) # Creates the menu
menu_bar.add_cascade(label="Slope Info", menu=model_menu) # Creates a cascade menu
model_menu.add_command(label="Display DEM", command=disp_dem) # Creates the option to display the DEM
model_menu.add_command(label="Display Slope", command=disp_slope) # Creates the option to display the Slope info
model_menu.add_command(label="Exit",command=root.destroy)   # Creates the option to exit the program

tk.mainloop()   # wait for user interaction in tk

