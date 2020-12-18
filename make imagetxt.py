# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 14:31:02 2020

@author: Adithia Jo
"""


import os
import numpy 
import glob
import cv2

root_path_testing = "obj"           ## path yang mau direnam

f = open("images.txt", "a")


for filename in os.listdir(root_path_testing):  
    f.write("/mydrive/images/"+ filename +"\n")
f.close()