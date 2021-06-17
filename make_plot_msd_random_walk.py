#Task 2 - example 1: analyze a random walk (1000 steps) using mean-squared displacement (msd)

#About this script
        #It creates one 1x2 subplot with random walk coordinates and its MSD
        #It is necessary to run create_msd_random_walk.py first before plotting to obtain the intermediate file with msd values

#Run command-line [python3 script.py msd_input_file.txt output_figure_name.png]
        #Example: $python3 make_plot_msd_random_walk.py msd_test.txt msd_plot.png

#importing modules used
import matplotlib.pyplot as plt
import pandas as pd
import sys

#arguments to the command-line
args = sys.argv[1:]
input = args[0]
output = args[1]

#defining the main funtion for plotting figure
def main(input, output):
    '''
    Read text files from create_msd_random_walk.py and plot 1x2 figure of random walk coordinates and its MSD
    '''
    #reading/importing input file
    df = pd.read_csv(input)

    N=1000
    msd = df["MSD"]
    msd = msd[1:N//2]
    
    time = np.arrange(N)[1:N//2]
    #subplot 1x2, and size with wspace
    fig, axs = plt.subplots(1,2,figsize=(10,5))
    plt.subplots_adjust(wspace=0.30)

    #setting X, Y from df for the first subplot with tile, locators, and grid
    axs[0].plot(df["x"],df["y"])
    axs[0].set_title("2D Random Walk Coordinates")
    axs[0].xaxis.set_major_locator(plt.MaxNLocator(7))
    axs[0].yaxis.set_major_locator(plt.MaxNLocator(7))
    axs[0].grid()

    #setting MSD from df for the second subplot with tile, locators, and grid
    axs[1].plot(time, msd, "tab:orange")
    axs[1].plot(time, 2*time, "tab:green")
    axs[1].legend(["Random walk (num.)", "Random walk (theo.)"])
    axs[1].set_title("Random Walk Mean-squared Displacement")
    axs[1].xaxis.set_major_locator(plt.MaxNLocator(7))
    axs[1].yaxis.set_major_locator(plt.MaxNLocator(7))
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
