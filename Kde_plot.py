# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 18:45:24 2024

@author: dell
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import kurtosis, skew


folder_path = 'combined_degree'
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed

# Define a color palette with enough colors for all the files
colors = sns.color_palette("hsv", len(os.listdir(folder_path)))

for i, filename in enumerate(os.listdir(folder_path)):
    if filename.endswith(".csv"):
        # Read the CSV file
        path = os.path.join(folder_path, filename)
        df = pd.read_csv(path, delimiter=',')

        # Extract the 'Degree' column
        degree_values = df['Degree']

        # Plot the KDE curve for each file with a different color
        sns.kdeplot(degree_values, label=filename, color=colors[i])

# Set the x-limit and y-limit
plt.xlim(0, 400)
plt.ylim(0, 0.030)

# Add labels and title
plt.xlabel('k (Degree)')
plt.ylabel('Probability Density')
plt.title('Probability Distribution of Degree Values')

# Show the plot
plt.show()
