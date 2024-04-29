# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 17:35:16 2024

@author: dell
"""

# degree_distribution.py

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import kurtosis, skew

class DegreeDistribution:
    def __init__(self, file_path):
        self.file_path = file_path
        self.mean_degree = None
        self.kurtosis_value = None
        self.skewness = None
        self.variance_value = None

    def calculate_statistics(self):
        # Read the CSV file into a DataFrame with the correct delimiter
        df = pd.read_csv(self.file_path, delimiter=',')

        # Extract the 'Degree' column
        degree_values = df['Degree']
        self.mean_degree = round(np.mean(degree_values), 5)
        self.kurtosis_value = round(kurtosis(degree_values), 5)
        self.skewness = round(skew(degree_values), 5)
        self.variance_value = round(np.var(degree_values), 5)

    def plot_distribution(self):
        # Read the CSV file into a DataFrame with the correct delimiter
        df = pd.read_csv(self.file_path, delimiter=',')

        # Extract the 'Degree' column
        degree_values = df['Degree']

        # Plot the KDE curve
        kde_plot = sns.kdeplot(degree_values)

        # Add labels and title
        plt.xlabel('k (Degree)')
        plt.ylabel('Probability Density')
        plt.title('Probability Distribution of Degree Values')

        # Add legends
        plt.legend([f'Mean Degree: {self.mean_degree}\nKurtosis: {self.kurtosis_value}\nSkewness: {self.skewness}\nVariance: {self.variance_value}'])

        # Show the plot
        plt.show()

    def get_statistics(self):
        return self.mean_degree, self.kurtosis_value, self.skewness, self.variance_value
