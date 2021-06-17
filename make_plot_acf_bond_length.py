#Task 1 - example 1: analyze the CO bond stretching motion using its time autocorrelation function (acf) from its time series of a MD simulation.

#About this script
        #It creates one 2x2 plot with length versus time of C=O and C-H bond lengths, and their autocorrelation funtion (acf)
	#It is necessary to run create_acf.py first before plotting to obtain the intermediate files with acf values of C=O and C-H bond lengths

#Run command example [python3 script.py input_file1.txt input_file2.txt output_figure_name.png]
        #$python3 make_plot_acf.py CO_acf.txt CH_acf.txt CO_CH_lengths_acf.png

#importing modules used
import matplotlib.pyplot as plt
import pandas as pd
import sys

#assigning arguments into input1/input2/output for the command-line
args = sys.argv[1:]
input1 = args[0]
input2 = args[1]
output = args[2]

#defining the main funtion for plotting figure
def main(input1, input2, output):
    '''
    Read text files from create_acf.py and plot 2x2 length (and its average) versus time, and acf versus lag
    '''
    #reading/importing input file
    dfCH = pd.read_csv(input1)
    dfCO = pd.read_csv(input2)

    fig, axs = plt.subplots(2,2,figsize=(7,6))
    plt.subplots_adjust(wspace=0.55, hspace=0.4)

    axs[0, 0].plot(dfCH["Time"],dfCH["Length"], color="green")
    axs[0, 0].set_xlim([800,1000])
    axs[0, 0].set_title("CH bond length")
    axs[0, 0].xaxis.set_major_locator(plt.MaxNLocator(4))
    axs[0, 0].yaxis.set_major_locator(plt.MaxNLocator(6))
    axs[0, 0].grid()

    axs[0, 1].stem(dfCH["AutoCorr"][::250], linefmt="C2--",markerfmt="C2d")
    axs[0, 1].set_ylim([0.0089,0.009030])
    axs[0, 1].set_title("Autocorrelation of CH")
    axs[0, 1].xaxis.set_major_locator(plt.MaxNLocator(6))
    axs[0, 1].yaxis.set_major_locator(plt.MaxNLocator(6))
    axs[0, 1].grid()
 
    axs[1, 0].plot(dfCO["Time"],dfCO["Length"])
    axs[1, 0].set_xlim([800,1000])
    axs[1, 0].set_title("CO bond length")
    axs[1, 0].xaxis.set_major_locator(plt.MaxNLocator(4))
    axs[1, 0].yaxis.set_major_locator(plt.MaxNLocator(6))
    axs[1, 0].grid()

    axs[1, 1].stem(dfCO["AutoCorr"][::250], linefmt="C0--",markerfmt="C0d")
    axs[1, 1].set_ylim([0.01509,0.01526])
    axs[1, 1].set_title("Autocorrelation of CO")
    axs[1, 1].xaxis.set_major_locator(plt.MaxNLocator(6))
    axs[1, 1].yaxis.set_major_locator(plt.MaxNLocator(6))
    axs[1, 1].grid()

    plt.setp(axs[:,0], xlabel='Time (ns)')
    plt.setp(axs[:,1], xlabel='Lag')
    plt.setp(axs[:,0], ylabel='Length (nm)')
    plt.setp(axs[:,1], ylabel='Autocorrelation')
    plt.show()
    plt.savefig(output, dpi = 300)

if __name__ == "__main__":
    main(input1, input2, output)
