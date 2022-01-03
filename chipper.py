import os
import glob
import numpy
import random
import cv2


"""The goal of this script is to read in random images from a directory into cv2, allow the user to click
in the middle of a vehicle, have cv2 create a bounding box of 22x22 pixels around that point, and extract
that image chip into a new folder which will be used for training a cnn.

top_2016 imagery chips should be 22x22 (or maybe 25x25) pixels to fit most personal vehicles. 

top_2016 imagery has a spatial resolution of .5 meters

"""


#print('\nNamed with wildcard *:')
#files = glob.glob('G:/top_images/top15-50cm_48397_nc-cir/*.jp2')
#random.shuffle(files)

#for i in files:
#    im = cv2.imread(i)
#    #cv2.imshow('test', im)

im = cv2.imread('G:/top_images/top15-50cm_48397_nc-cir/cropped_tiles/cropped_tiles.115.tif', 0)

#cv2.imshow('image', im)
#cv2.waitKey(0)


im.