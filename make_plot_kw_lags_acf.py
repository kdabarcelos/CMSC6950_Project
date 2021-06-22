#Task 2 (ACF example 2): analyze seasonal keyword trends, such as 'gym', 'weight', 'diet', 'money', and 'travel' using its time autocorrelation fun>
#About this script
        #It creates one 2x2 plot with autocorrelation funtion (acf)
        #It is necessary to run download_keywords_acf.py first before plotting to obtain the intermediate files

#Run command example [python3 script.py input_file.txt output_figure_name.png]
        #$python3 make_plot_kw_lags_acf.py kw_acf.txt lags_acf.png

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
    Read keyword intermediate file created by download_keywords_acf.py and plot lags plot of a time series against a lag of itself
    '''
    #reading/importing input file
    df = pd.read_csv(input)

    from pandas.plotting import lag_plot
    plt.rcParams.update({'ytick.left' : False, 'axes.titlepad':10})
    kw_list = ['diet', 'gym','weight','travel','money']     

    
    fig, axs = plt.subplots(1,5,figsize=(15,5))
    plt.subplots_adjust(wspace=0.5, hspace=0.2)

    plt.subplot(151)
    lag_plot(df.diet, c='k')
    plt.title('Lag diet')

    plt.subplot(152)
    lag_plot(df.gym, c='r')
    plt.title('Lag gym')

    plt.subplot(153)
    lag_plot(df.weight, c='b')
    plt.title('Lag weight')

    plt.subplot(154)
    lag_plot(df.travel, c='g')
    plt.title('Lag travel')

    plt.subplot(155)
    lag_plot(df.money, c='y')
    plt.title('Lag money')

    plt.show()
    plt.savefig(output, dpi = 300)

if __name__ == "__main__":
    main(input, output)
