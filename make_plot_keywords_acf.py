#Task 2 (ACF example 2): analyze seasonal keyword trends, such as 'gym', 'weight', 'diet', 'money', and 'travel' using its time autocorrelation fun>

#About this script
        #It creates one 2x2 plot with autocorrelation funtion (acf)
        #It is necessary to run download_keywords_acf.py first before plotting to obtain the intermediate files

#Run command example [python3 script.py input_file.txt output_figure_name.png]
        #$python3 make_plot_keywords.py kw_acf.txt kw_acf.png

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
    df = pd.read_csv(input,parse_dates=["date"],index_col=["date"])

    fig, axs = plt.subplots(2,1,figsize=(10,8))
    plt.subplots_adjust(wspace=0.20, hspace=0.4)

    #setting X, Y from df for the first subplot with tile, locators, and grid
    axs[0].plot(df.index,df.diet,'k')
    axs[0].plot(df.index,df.gym,'r')
    axs[0].plot(df.index,df.weight,'b')
    axs[0].plot(df.index,df.travel,'g')
    axs[0].plot(df.index,df.money,'y')
    axs[0].legend(['Diet', 'Gym','Weight','Travel','Money'])
    axs[0].set_title("New Year's Google Search of Keywords during 2004-2020 in Canada")
    axs[0].yaxis.set_major_locator(plt.MaxNLocator(7))
    axs[0].grid()

    #setting MSD from df for the second subplot with tile, locators, and grid
    axs[1].plot(range(len(df.diet)),df.diet_autocorr,'k')
    axs[1].set_title("ACF of Periodic Keywords Popularity")
    axs[1].plot(range(len(df.gym)),df.gym_autocorr,'r')
    axs[1].plot(range(len(df.weight)),df.weight_autocorr,'b')
    axs[1].plot(range(len(df.travel)),df.travel_autocorr,'g')
    axs[1].plot(range(len(df.money)),df.money_autocorr,'y')
    axs[1].xaxis.set_major_locator(plt.MaxNLocator(9))
    axs[1].yaxis.set_major_locator(plt.MaxNLocator(7))
    axs[1].grid()

    #setting up the labels  and saving fig
    plt.setp(axs[0], xlabel='Year')
    plt.setp(axs[0], ylabel='Popularity')
    plt.setp(axs[1], xlabel='Lag')
    plt.setp(axs[1], ylabel='Autocorrelation')
    plt.show()
    plt.savefig(output, dpi = 300)

if __name__ == "__main__":
    main(input, output)


