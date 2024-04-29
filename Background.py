# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:18:35 2024

@author: dell
"""
import matplotlib.pyplot as plt
from scipy.ndimage import generic_filter
import cv2
import numpy as np
import os
plt.figure(figsize=(12,8))

folder_path='cropped_frames-20240312T171045Z-001/cropped_frames'
count=0
time_values=[]
Grain_pixel=[]
def identify_grain_boundary(neighbourhood):
    # Example logic: Check if there is a significant intensity difference in the neighborhood
    # You might need to adjust this logic based on your specific requirements
    unique_colors = len(set(neighbourhood))
    if unique_colors > 8:  # Example threshold for significant intensity difference
        return 0  # Pixel is classified as part of grain boundary
    else:
        return 1  # Pixel is not part of grain boundary
count=0
for filename in os.listdir(folder_path):
    if filename.endswith(".jpg"):  # Assuming all images are JPEGs, adjust if needed
        # Read the image
        plt.figure(figsize=(12,8))
        path = os.path.join(folder_path, filename)
        image=cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        plt.imshow(image, cmap='gray')
        result=generic_filter(image,identify_grain_boundary, (3,3))
        plt.imshow(result, cmap='gray')
        gb_size=np.size(result)-np.count_nonzero(result)
        Grain_pixel.append(gb_size/np.size(result))
        time_values.append(count)
        count=count+1

def plot(values, time_values, title, y):
    # Plotting mean values against time
    plt.figure(figsize=(12, 10))
    plt.plot(time_values, values, marker='o', linestyle='-', color='b')

    # Customize the plot
    plt.title(title)
    plt.xlabel('Time(s)')
    plt.ylabel(y)
    plt.grid(True)

    # Show the plot
    plt.show()

plot(Grain_pixel, time_values, 'Fraction_of_GB_pixels_Vs_Time', 'Fraction_GB')
# Display the result
#plt.imshow(data_0, cmap='gray')
#plt.imshow(result, cmap='gray')
