import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

data=[[0.1, 0.5, 0.1, 0.7, 0.2],
        [0.3, 0.1, 0.4, 0.2, 0.8],
        [0.2, 0.6, 0.5, 0.1, 0.6],
        [0.1, 0.6, 0.2, 0.1, 0.3],
        [0.7, 0.1, 0.7, 0.4, 0.3]]

#print(data)

def calculate_directions(d, embed):
    directions=[]
    if(embed=='fcc'):
        n=2*d + pow(2, d)
        for p in range(1, n+1):
            angle = 2*np.pi*(p-1) / n
            directions.append([np.array([np.cos(angle), np.sin(angle)])])
        return directions
            
        
    if(embed=='cnn'):
        n=2*d
        for p in range(1, n+1):
            angle = 2*np.pi*(p-1) / n
            directions.append([np.array([np.cos(angle), np.sin(angle)])])
        return directions
            
    else:
        return 0;

embed="fcc"
direction=calculate_directions(2, embed)
print(direction)
    