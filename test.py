# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 16:03:43 2024

@author: dell


from Visibility_Graph.Visibility_graph import VisibilityGraph
import numpy as np
import cv2
import pandas as pd

data_0=data=cv2.imread('frame_0000.jpg', cv2.IMREAD_GRAYSCALE)
#data = np.array(data)

visibility_graph = VisibilityGraph(data)
res = visibility_graph.create_visibility_graph_2d()

degree_sequence = dict(res.degree())
degree_counts = pd.Series(list(degree_sequence.values())).value_counts().reset_index()
degree_counts.columns = ['Degree', 'Frequency']
degree_counts.to_csv('degree_0000', index=False)

df = pd.DataFrame(res.degree(), columns=['Node', 'Degree'])
result_df = pd.merge(df, degree_counts, on='Degree', how='left')
result_df.to_csv('degree_combine_0000', index=False)


visibility_graph.save_degree_counts('degree_counts_0.csv')

visibility_graph.save_combined_degree_info('combined_degree_info_0.csv')

visibility_graph.degree_histogram('Degree_distribution')

# -*- coding: utf-8 -*-

Created on Sun Mar 10 16:03:43 2024

@author: dell


from Degree_Distribution.Degree_distribution import DegreeDistribution

# Example usage for a single file
file_path = 'degree_combine_0000'  # Replace 'your_file_path.csv' with the actual file path
degree_distribution = DegreeDistribution(file_path)
degree_distribution.calculate_statistics()
degree_distribution.plot_distribution()

# Access the calculated statistics
mean_degree, kurtosis_value, skewness, variance_value = degree_distribution.get_statistics()
print("Mean Degree:", mean_degree)
print("Kurtosis:", kurtosis_value)
print("Skewness:", skewness)
print("Variance:", variance_value)



from Degree_Distribution.Plots import DegreeDistributionPlotter


# Example file path and legend
#file_path = 'combined_degree_info_0.csv'  # Replace with your file path
legend = 'Legend'  # Replace with your legend

# Create an instance of DegreeDistributionPlotter
plotter = DegreeDistributionPlotter(file_path, legend)

# Plot the degree distribution
max_index, max_prob = plotter.plot_degree_distribution()

print(max_index)
print(max_prob)

# Plot the linear fit with specified range (optional)
degree_range = (65, 190)  # Specify the desired degree range
plotter.plot_linear_fit(degree_range)
"""
