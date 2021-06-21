#Task 2 (ACF example 2): analyze seasonal keyword trends, such as 'gym', 'weight', 'diet', 'money', and 'travel' using its time autocorrelation fun>

#About this script
        #It creates one 2x2 plot with autocorrelation funtion (acf)
        #It is necessary to run download_keywords_acf.py first before plotting to obtain the intermediate files

#Run command example [python3 script.py input_file.txt output_figure_name.png]
        #$python3 download_keywords_acf.py kw_acf.txt kw_acf.png

#importing modules used
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys

#arguments to the command-line
args = sys.argv[1:]
input = args[0]
output = args[1]

#defining the main funtion for plotting figure
def main(input, output):
    '''
    Read keyword intermediate file created by download_keywords_acf.py and plot figure of each keyword popularity and its ACF
    '''
    #reading/importing input file
    df = pd.read_csv(input)

    #subplot 1x2, and size with wspace
    fig, axs = plt.subplots(1,2,figsize=(10,5))
    plt.subplots_adjust(wspace=0.30)

    #setting X, Y from df for the first subplot with tile, locators, and grid
    axs[0].plot(df["x"],df["y"])
    axs[0].set_title("2D Random Walk Coordinates")
    axs[0].plot(start[0,0],start[0,1],c="black",marker="o",markersize=7,markeredgewidth=2.5)
    axs[0].plot(end[0,0],end[0,1],c="red",marker="x",markersize=10,markeredgewidth=2.5)
    axs[0].legend(["Path", "Start", "End"])
    axs[0].xaxis.set_major_locator(plt.MaxNLocator(7))
    axs[0].yaxis.set_major_locator(plt.MaxNLocator(7))
    axs[0].grid()

    #setting MSD from df for the second subplot with tile, locators, and grid in log scale
    axs[1].plot(time, msd, "tab:orange")
    axs[1].plot(time, 2*time, "tab:green")
    axs[1].legend(["Random walk (num.)", "Random walk (theo.)"])
    axs[1].set_title("Random Walk Mean-squared Displacement")
    axs[1].set_xscale("log")
    axs[1].set_yscale("log")
    axs[1].grid()

    #setting up the labels  and saving fig
    plt.setp(axs[0], xlabel="Coordinate X")
    plt.setp(axs[0], ylabel="Coordinate Y")
    plt.setp(axs[1], xlabel="Timesteps")
    plt.setp(axs[1], ylabel="Mean-squared Displacement")
    plt.show()
    plt.savefig(output, dpi = 300)

if __name__ == "__main__":
    main(input, output)


