#Task 1 - example 1: analyze the CO bond stretching motion using its time autocorrelation function (acf) from its time series of a MD simulation.

#About this script
	#It generates an intermediate file with acf results from bond length
	#It works for two-column file (i.e, .txt, .svg, etc) wherein first column is time and second is length
	
#Run command-line [python3 script.py input_file.txt output_file_name.txt]
	#Example: $python3 create_acf.py test800-1500ns-CH.txt CH_acf.txt

#Where the input data are from?
        #The resulting data has been obtained from a MD simulation from 0 to 1500 ns
        #to demonstrate CH and CO stretching motion over time from a certain Tyrosine aminoacid.
        #Both files test800-1500ns-CH.xvg and test800-1500ns-CO.xvg show the length between C-H and C=O bonds, respecively.
        #The time in nanosecond (ns) from period of 800-1500 ns to ensure data analysis in the protein equilibrium.

#importing modules used
import numpy as np 
import tidynamics 
import pandas as pd 
import sys

#assigning arguments into input/out for the command-line
args = sys.argv[1:]
input = args[0]
output = args[1]

#defining main funtion
def main(input, output):
    '''
    Create intermediate file with time, bond length, and acf data from length
    '''
    #load input file and create data frame with time and length
    input_data = np.loadtxt(input)
    df = pd.DataFrame(input_data, columns=["Time", "Length"])
    #apply autocorrection funtion (acf) in length
    result = tidynamics.acf(df["Length"])
    #create new column with acf
    df["AutoCorr"] = result
    #saving output with comma delimiter and headers
    df.to_csv(output, index=False)

if __name__ == "__main__":
    main(input,output)
