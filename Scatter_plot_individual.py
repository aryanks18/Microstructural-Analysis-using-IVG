# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 19:15:34 2024

@author: dell
"""
import os
import re  # Import the regular expression module
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
 


max_index=[]
max_prob=[]
from Degree_Distribution.Plots import DegreeDistributionPlotter

folder_path='combined_degree'
count=0
time_values=[]
for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):  # Assuming all images are JPEGs, adjust if needed
        # Read the image
        path = os.path.join(folder_path, filename)
        time_seconds = re.search(r'(\d+)', filename).group(1)  # Extract digits from filename
        time_seconds = int(time_seconds) 
        legend = f'Time ({time_seconds} s)'
        # Create an instance of DegreeDistributionPlotter
        plotter = DegreeDistributionPlotter(path, legend=legend)

        # Plot the degree distribution
        prob, index = plotter.plot_degree_distribution()
        max_index.append(index)
        max_prob.append(prob)
        time_values.append(count)
        count=count+1

print(max_index)
print(max_prob)

def plot(values, time_values, title, y):
    # Plotting mean values against time
    plt.figure(figsize=(16, 12))
    plt.plot(time_values, values, marker='o', linestyle='-', color='r')

    # Customize the plot
    plt.title(title, fontsize=35, color='black', weight='bold', pad=25)
    plt.xlabel('Time(s)', fontsize=30, color='black', fontweight='bold', labelpad=25)
    plt.ylabel(y, fontsize=30, color='black',fontweight='bold', labelpad=25)
    plt.grid(True)
    plt.legend(prop={'size':25})
    
    plt.xticks(color='black', fontsize=25)
    plt.yticks(color='black', fontsize=25)

    # Show the plot
    plt.show()

plot(max_index, time_values, 'Most_freq_degree_Vs_Time', 'Most_freq_degree')
plot(max_prob, time_values, 'Prob_most_freq_degree_Vs_Time', 'Prob_most_freq_degree')

print(max(max_index))
# Plot the linear fit with specified range (optional)
#degree_range = (65, 190)  # Specify the desired degree range
#plotter.plot_linear_fit(degree_range)