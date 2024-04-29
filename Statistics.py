# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 17:50:09 2024

@author: dell
"""
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import kurtosis, skew

from Degree_Distribution.Degree_distribution import DegreeDistribution
degree_mean=[]
degree_variance=[]
degree_skewness=[]
degree_kurtosis=[]
time_values=[]

folder_path='combined_degree'
count=0
# Iterate through all image files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):  # Assuming all images are JPEGs, adjust if needed
        # Read the image
        path = os.path.join(folder_path, filename)
        df = pd.read_csv(path, delimiter=',')

        # Extract the 'Degree' column
        degree_values = df['Degree']
        degree_mean.append(round(np.mean(degree_values), 5))
        degree_kurtosis.append(round(kurtosis(degree_values), 5))
        degree_skewness.append(round(skew(degree_values), 5))
        degree_variance.append(round(np.var(degree_values), 5))
        time_values.append(count)
        count=count+1


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

plot(degree_mean, time_values, 'Mean_degree_Vs_Time', 'Mean_degree')
plot(degree_variance, time_values, 'Variance_degree_Vs_Time', 'Variance_degree')
plot(degree_skewness, time_values, 'Skewness_degree_Vs_Time', 'Skewness_degree')
plot(degree_kurtosis, time_values, 'Kurtosis_degree_Vs_Time', 'Kurtosis_degree')


