# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 18:59:31 2024

@author: dell
"""

import os
import re  # Import the regular expression module
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import kurtosis, skew


folder_path = 'combined_degree'
for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):
        # Extract the time (in seconds) from the filename
        time_seconds = re.search(r'(\d+)', filename).group(1)  # Extract digits from filename
        time_seconds = int(time_seconds)  # Convert to integer
        
        # Read the CSV file
        path = os.path.join(folder_path, filename)
        df = pd.read_csv(path, delimiter=',')
        
        # Extract the 'Degree' column
        degree_values = df['Degree']
        
        # Calculate statistics
        degree_mean = round(np.mean(degree_values), 5)
        degree_kurtosis = round(kurtosis(degree_values), 5)
        degree_skewness = round(skew(degree_values), 5)
        degree_variance = round(np.var(degree_values), 5)
        
        # Plot the KDE curve
        kde_plot = sns.kdeplot(degree_values)
        
        # Set x and y limits
        plt.xlim(0, 400)
        plt.ylim(0, 0.030)
        
        # Add labels and title
        plt.xlabel('k (Degree)')
        plt.ylabel('Probability Density')
        plt.title(f'Probability Distribution of Degree Values (Time: {time_seconds} seconds)')
        
        # Add legends
        plt.legend([f'Mean Degree: {degree_mean}\nKurtosis: {degree_kurtosis}\nSkewness: {degree_skewness}\nVariance: {degree_variance}'])
        
        # Show the plot
        plt.show()
