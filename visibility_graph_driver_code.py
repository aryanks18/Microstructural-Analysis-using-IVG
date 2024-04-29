# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 16:52:23 2024

@author: dell
"""


import os
import cv2
from Visibility_Graph.Visibility_graph import VisibilityGraph
import numpy as np
import pandas as pd
# Assuming you already have the VisibilityGraph class defined

def process_images_in_folder(folder_path, output_folder):
    # Iterate through all image files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg"):  # Assuming all images are JPEGs, adjust if needed
            # Read the image
            image_path = os.path.join(folder_path, filename)
            data = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            
            # Create the visibility graph
            visibility_graph = VisibilityGraph(data)
            res = visibility_graph.create_visibility_graph_2d()

            # Save degree counts
            degree_counts_file = os.path.join(output_folder, f'degree_counts_{filename[:-4]}.csv')
            visibility_graph.save_degree_counts(degree_counts_file)

            # Save combined degree info
            combined_degree_info_file = os.path.join(output_folder, f'combined_degree_info_{filename[:-4]}.csv')
            visibility_graph.save_combined_degree_info(combined_degree_info_file)

            # Plot degree histogram
            degree_histogram_name = f'Degree_distribution_{filename[:-4]}'
            visibility_graph.degree_histogram(degree_histogram_name)

# Example usage
input_folder='cropped_frames-20240312T171045Z-001/cropped_frames'  # Folder containing the original images
output_folder = 'cropped'  # Folder to save the results
process_images_in_folder(input_folder, output_folder)
