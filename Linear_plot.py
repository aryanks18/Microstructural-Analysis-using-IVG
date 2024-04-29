# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 22:46:51 2024

@author: dell
"""
import os
import re  # Import the regular expression module
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


from Degree_Distribution.Plots import DegreeDistributionPlotter



from Degree_Distribution.Plots import DegreeDistributionPlotter

folder_path='combined_degree'
count=0
time_values=[]
slopes=[]
degree_range=(40,120)
for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):  # Assuming all images are JPEGs, adjust if needed
        # Read the image
        path = os.path.join(folder_path, filename)
        time_seconds = re.search(r'(\d+)', filename).group(1)  # Extract digits from filename
        time_seconds = int(time_seconds) 
        legend = f'Time ({time_seconds} s)'
        # Create an instance of DegreeDistributionPlotter
        plotter = DegreeDistributionPlotter(path, legend=legend)
        slopes.append(plotter.plot_linear_fit(degree_range))

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

plot(slopes, time_values, 'Slopes_vs_Time (s)', 'Slope')
