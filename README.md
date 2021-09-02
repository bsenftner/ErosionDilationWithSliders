# ErosionDilationWithSliders.py

A simple Python OpenCV program demonstrating Erosion and Dilation

It provides 4 slidebars, each modifying the operation performed on 1 of 4 source images. 
Changing the source image really helps illustrate the two Erosion and Dilation operations. 

Slidebar 1 ("Type") has 2 positions, position 0 makes the image operation erosion and position 1 makes the image operation dilation.

Slidebar 2 ("Src") has 4 positions, each corresponding to a different source image to be eroded or dilated, according to slider 1's position.

Slidebar 3 ("Kernel") has 3 positions, corresponding to a 3x3, a 5x5 or a 7x7 oval kernel

Slidebar 4 ("Iterations") has 11 positions corresponding to the number of iterations the erode or dilate will perform, 0 means do nothing

This requires OpenCV with Python to be installed on the system. 
Just cd into the ScriptFiles directory and execute:

	python ErosionDilationWithSliders.py

Use the ESC key to quit. 


