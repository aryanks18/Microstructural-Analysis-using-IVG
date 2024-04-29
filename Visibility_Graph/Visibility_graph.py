# visibility_graph.py

import networkx as nx
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class VisibilityGraph:
    def __init__(self, data):
        self.data = data
        self.num_rows, self.num_columns = data.shape
        self.G = nx.Graph()
        self.data = data.astype(np.float64)  # Convert data to float64

    def calculate_slope(self, x1, y1, x2, y2):
        dx, dy = x2 - x1, y2 - y1
        numerator = self.data[x2, y2] - self.data[x1, y1]
        denominator = np.hypot(dx, dy)
        # Check for division by zero
        if denominator == 0:
            slope = 0
        else:
            slope = numerator / denominator
        return slope

    def is_visible(self, x1, y1, x2, y2, visible_cells):
        slope = self.calculate_slope(x1, y1, x2, y2)
        for x, y in visible_cells:
            slope1 = self.calculate_slope(x1, y1, x, y)
            if slope < slope1:
                return False
        return True

    def create_visibility_graph_2d(self):
        for i in range(self.num_rows):
            for j in range(self.num_columns):
                directions = [(0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, 1), (-1, -1)]

                for dx, dy in directions:
                    p, q = i + dx, j + dy
                    visible_cells = set()

                    while 0 <= p < self.num_rows and 0 <= q < self.num_columns:
                        if self.G.has_edge((i, j), (p, q)):
                            visible_cells.add((p, q))

                        elif self.is_visible(i, j, p, q, visible_cells):
                            self.G.add_edge((i, j), (p, q))
                            visible_cells.add((p, q))

                        p, q = p + dx, q + dy
                print(i,j)
        return self.G
    def save_degree_counts(self, file_name):
        degree_sequence = dict(self.G.degree())
        degree_counts = pd.Series(list(degree_sequence.values())).value_counts().reset_index()
        degree_counts.columns = ['Degree', 'Frequency']
        degree_counts.to_csv(file_name, index=False)

    def save_combined_degree_info(self, file_name):
        degree_sequence = dict(self.G.degree())
        degree_counts = pd.Series(list(degree_sequence.values())).value_counts().reset_index()
        degree_counts.columns = ['Degree', 'Frequency']
        df = pd.DataFrame(self.G.degree(), columns=['Node', 'Degree'])
        result_df = pd.merge(df, degree_counts, on='Degree', how='left')
        result_df.to_csv(file_name, index=False)
        
    def degree_histogram(self, name):
        # Get the degree histogram
        degrees = dict(self.G.degree())
        degree_sequence = list(degrees.values())
        histogram = nx.degree_histogram(self.G)

        # Plot the histogram
        plt.bar(range(len(histogram)), histogram, width=0.8, color='b')
        plt.xlabel('Degree')
        plt.ylabel('Frequency')
        plt.title(name)
        plt.show()





















