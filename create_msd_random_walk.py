#Task 2 - example 1: analyze a random walk using mean-squared displacement (msd).

#About this script
        #It generates an intermediate file with msd results
        
#Run command-line [python3 script.py output_file_name.txt]
        #Example: $python create_msd_random_walk.py msd_random_walk.txt


import numpy as np
import math
import tidynamics
import pandas as pd
import sys

args = sys.argv[1:]
output = args[0]

#One random walk
def randwalk(x,y):
    '''
    Generate random walk (x,y) coordinates
    '''
    theta=2*math.pi*np.random.rand()
    x+=math.cos(theta);
    y+=math.sin(theta);
    #It will return new (x,y) coordinates
    return (x,y)

def main(output):
    '''
    Create intermediate file 
    '''
    a = np.zeros((1000,2), dtype=np.float64)
    #Starting from origin 
    x, y = 0., 0.
    #1000 step in the walk
    for i in range(1000):
        x,y = randwalk(x,y)
        a[i,:] = x,y
        
    #apply autocorrection funtion (acf) in length
    result = tidynamics.msd(a)
    
    #creating dataframe with coordinates x and y
    df = pd.DataFrame(a, columns=["x", "y"])
    
    #create new column with msd
    df["MSD"] = result

    #saving output with comma delimiter and adding headers
    df.to_csv(output, index=False)

if __name__ == "__main__":
    main(output)
