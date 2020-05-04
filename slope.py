# -*- coding: utf-8 -*-
"""
Created on Mon May  4 15:24:33 2020
 [dz/dx] = ((c + 2f + i) - (a + 2d + g) / (8 * x_cellsize)
          = ((50 + 60 + 10) - (50 + 60 + 8)) / (8 * 5)
          = (120 - 118) / 40
          = 0.05
The rate of change in the y direction for cell e is:

  [dz/dy] = ((g + 2h + i) - (a + 2b + c)) / (8 * y_cellsize)
          = ((8 + 20 + 10) - (50 + 90 + 50)) / (8 * 5)
          = (38 - 190 ) / 40
          = -3.8
Taking the rate of change in the x and y direction, the slope for the center cell e is calculated using

  rise_run = √ ([dz/dx]2 + [dz/dy]2)
           = √ ((0.05)2 + (-3.8)2)
           = √ (0.0025 + 14.44)
           = 3.80032
  slope_degrees = ATAN (rise_run) * 57.29578
                = ATAN (3.80032) * 57.29578
                = 1.31349 * 57.29578
                = 75.25762
@author: bkeight
"""

class Cell():
    
    def __init__(self, a, b, c, d, ctr, f, g, h, i):
        print('middle=', ctr)
        deltax = ((c + 2*f + i) - (a + 2*d + g) / 8)
        print(deltax)
        