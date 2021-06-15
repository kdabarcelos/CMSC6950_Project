#Task 2 - example 1: analyze a random walk (1000 steps) using mean-squared displacement (msd).

#About this script
        #It generates an intermediate file with (x,y) coordinates and its msd results

#Run command-line [python3 script.py output_file_name.txt]
        #Example: $python create_msd_random_walk.py msd_random_walk.txt

#importing modules used
import numpy as np
import math
import tidynamics
import pandas as pd
import sys

#arguments to the command-line
args = sys.argv[1:]
output = args[0]

#defining random walk funtion
def randomwalk(x,y):
    '''
    Generate 2D random walk as (x,y) coordinates
    '''
    theta=2*math.pi*np.random.rand()
    x+=math.cos(theta);
    y+=math.sin(theta);
    #funtion returns new random (x,y) coordinates
    return (x,y)

#defining main funtion
def main(output):
    '''
    Create intermediate file with (x,y) coordinates, and MSD in 1000 steps
    '''
    a = np.zeros((1000,2), dtype=np.float64)
    #starting from origin
    x, y = 0., 0.
    #1000 step in the walk
    for i in range(1000):
        x,y = randomwalk(x,y)
        a[i,:] = x,y

    #creating dataframe with coordinates x and y
    df = pd.DataFrame(a, columns=["x", "y"])

    #applying msd from tidynamics
    result = tidynamics.msd(a)

    #creating new column with msd
    df["MSD"] = result

    #saving output with comma delimiter
    df.to_csv(output, index=False)

if __name__ == "__main__":
    main(output)
