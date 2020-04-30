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
import os
import pathlib
import csv
import tkinter
import requests
import bs4

# Variables required


# Operating system info
sys = os.name
workdir = 'C:\\MSc\\Module3\\Python Code\\src\\unpacked\\adm\\Assignment2'

# Main

# Read in data file into Lists

File = open(os.path.join(workdir, 'snow.slope'))    # Open file
for Line in File.readlines():
    print(Line)
inFile.close()    # close files
