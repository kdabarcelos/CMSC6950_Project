import numpy as np 
import tidynamics 
import pandas as pd 
import sys

args = sys.argv[1:]
input = args[0]
output = args[1]

def main(input, output):
    #"Describe function"
    input_data = np.loadtxt(input)
    df = pd.DataFrame(input_data, columns=["Time", "Length"])
    result = tidynamics.acf(df["Length"])
    np.savetxt(output, result)

if __name__ == "__main__":
    main(input,output)

