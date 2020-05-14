# Assignment2
Programming for Spatial Analysts: Core Skills  Assessment 2

This is a practical assignment as part of the Leeds University "Programming for Geographical Information Analysis".
The Assignment brief is:
Imagine you are an extreme sports holiday company. You've been given raster data of the heights for a hilly area, and you want to find the most extreme gradients on which to set up snowboard runs. The raster data will be text numbers of metres above sea level.
Write a program which does the following.

1.	Pulls in the hillslope heights from a file.
2.	Calculates the maximum slope in all the raster cells.

    To do this use the "D8" algorithm.
    This calculates the slope between a cell and its eight neighbours, using their height and distance from the cell (this will be one for     four of the neighbours, and the square root of two for the other four). The maximum slope is then the greatest of these values. If you get two maximum slopes for a given cell you need to be careful your program doesn't break! You'll also need to think about what to do at the map edges.
    
3.	Builds a data set that has the slope gradients in it rather than the heights.
4.	Displays the heights and the gradients as images.
5.	Saves the gradients to a file in a similar format to the heights.
