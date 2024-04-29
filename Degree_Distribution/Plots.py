# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 18:18:17 2024

@author: dell
"""

# degree_distribution_plotter.py

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit


class DegreeDistributionPlotter:
    def __init__(self, file_path, legend, degree_range=None):
        self.file_path = file_path
        self.legend = legend
        self.degree_range = degree_range
        self.df = self.load_data()

    def load_data(self):
        return pd.read_csv(self.file_path, delimiter=',')
    
    def plot_image(image, title):
        
        plt.figure(figsize=(8, 8))
        plt.imshow(image, cmap='gray')  # Assuming grayscale image, change cmap as needed
        plt.title(title)
        plt.axis('off')
        plt.show()

    def plot_degree_distribution(self):
        max_probability = 0
        plt.figure(figsize=(16, 12))

        unique_values, counts = np.unique(self.df['Degree'], return_counts=True)

        # Calculate probability (degree divided by the total number of points)
        probability_values = counts / (counts.sum())
        
        # Find the index of maximum probability
        max_prob_index = np.argmax(probability_values)
        

        # Update max_probability if necessary
        max_probability = max(max_probability, probability_values[max_prob_index])

        # Plot the scatter plot with the full range
        plt.scatter(unique_values, np.log(probability_values), label=f'{self.legend}', marker='o', color='red')

        # Customize the plot
        plt.xlim(0, 400)
        plt.ylim(-13, -2)
        
        plt.title('Scatter_plot_Degree_distribution', fontsize=35, color='black', weight='bold', pad=25)
        plt.xlabel('K (Degree) ', fontsize=30, color='black', fontweight='bold', labelpad=25)
        plt.ylabel('Log (P(k)) ', fontsize=30, color='black',fontweight='bold', labelpad=25)
        plt.grid(True)
        plt.legend(prop={'size':25})
        
        plt.xticks(color='black', fontsize=25)
        plt.yticks(color='black', fontsize=25)
        
        
        plt.show()
        
        return max_probability, max_prob_index

    def plot_linear_fit(self, degree_range=None):
        if degree_range is None:
            degree_range = (self.df['Degree'].min(), self.df['Degree'].max())

        plt.figure(figsize=(12, 8))
        unique_values, counts = np.unique(self.df['Degree'], return_counts=True)

      
        # Calculate probability (degree divided by the total number of points)
        probability_values = counts / (counts.sum())
        
        valid_indices=probability_values > 0
        valid_unique_values = unique_values[valid_indices]

        # Select probability values within the specified degree range
        degree_range_indices = (valid_unique_values >= degree_range[0]) & (valid_unique_values <= degree_range[1])
        x_straight = valid_unique_values[degree_range_indices]
        y_straight = np.log(probability_values[degree_range_indices])
        
        # Fit a straight line using numpy's polyfit
        coeffs = np.polyfit(x_straight, y_straight, 1)
        slope = coeffs[0]


        # Plot the scatter plot with the specified range
        plt.scatter(x_straight, y_straight, marker='o')

        # Plot the straight line fit
        plt.plot(x_straight, np.polyval(coeffs, x_straight), label=f'{self.legend} - Slope: {slope:.5f}', linestyle='solid')

        # Customize the plot
        plt.xlim(35, 130)
        plt.ylim(-10, -2)
        plt.title('Linear Plot of Degree Distribution')
        plt.xlabel('K (Degree)')
        plt.ylabel('Log(P(k))')
        plt.legend()
        plt.grid(True)
        plt.text(x_straight.mean(), np.log(probability_values.max()), f'Degree Range: [{x_straight.min()}, {x_straight.max()}]', ha='center')
        # Display the plot
        plt.show()
        
        return slope

    
