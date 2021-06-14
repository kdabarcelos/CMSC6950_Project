#About this script
	#It works for two-column file (i.e, .txt, .svg, etc) wherein first column is time and second is length
	#It generates an intermediate file with acf results 

#Run command example [python3 script.py input_file.txt output_file_name.txt]
	#$python3 create_acf.py test800-1500ns-CH.txt CH_acf.txt

#Where the data are from?
        #The resulting data has been obtained from a MD simulation from 0 to 1500 ns
        #to demonstrate CH and CO stretching motion over time from a certain Tyrosine aminoacid.
        #Both files test800-1500ns-CH.xvg and test800-1500ns-CO.xvg show the length between C-H and C=O bonds, respecively.
        #The time in nanosecond (ns) from period of 800-1500 ns to ensure data analysis in the protein equilibrium.


import numpy as np 
import tidynamics 
import pandas as pd 
import sys

args = sys.argv[1:]
input = args[0]
output = args[1]

def main(input, output):
    '''
    Create intermediate file with acf data from bond length
    '''
    input_data = np.loadtxt(input)
    df = pd.DataFrame(input_data, columns=["Time", "Length"])
    result = tidynamics.acf(df["Length"])
    np.savetxt(output, result)

if __name__ == "__main__":
    main(input,output)

