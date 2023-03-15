from csv import reader

import numpy as np

if __name__ == "__main__":
    # Path of the dataset

    data = np.loadtxt('colliders.csv', delimiter=',', dtype='float', skiprows=2)

    # Let's print the first 5 datapoints
    for row in data[:6]:
        print(row, end="\n")