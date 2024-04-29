# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 22:40:03 2024

@author: dell
"""

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
        max_probability = 0

        unique_values, counts = np.unique(df['Degree'], return_counts=True)

        # Calculate probability (degree divided by the total number of points)
        probability_values = counts / (counts.sum())
        
        # Find the index of maximum probability
        max_prob_index = np.argmax(probability_values)
        

        # Update max_probability if necessary
        max_probability = max(max_probability, probability_values[max_prob_index])

        # Plot the scatter plot with the full range
        plt.scatter(unique_values, np.log(probability_values), marker='o')



# Customize the plot
plt.xlim(0, 400)
plt.ylim(-13, -2)
plt.title('Scatter Plot of Degree Distribution')
plt.xlabel('K (Degree)')
plt.ylabel('Log(P(k))')
plt.legend()
plt.grid(True)
# Display the plot
plt.show()



