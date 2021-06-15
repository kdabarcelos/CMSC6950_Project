import matplotlib.pyplot as plt
import pandas as pd
import sys

args = sys.argv[1:]
input = args[0]
output = args[1]

def main(input, output):
    '''
    Read text files from create_msd_random_walk.py and plot 1x2 figure of random walk coordinates and its MSD
    '''
    
    df = pd.read_csv(input)
    
    fig, axs = plt.subplots(1,2,figsize=(10,5))
    plt.subplots_adjust(wspace=0.40)

    axs[0].plot(df["x"],df["y"])
    axs[0].set_title("2D Random Walk Coordinates")
    axs[0].xaxis.set_major_locator(plt.MaxNLocator(7))
    axs[0].yaxis.set_major_locator(plt.MaxNLocator(7))
    axs[0].grid()

    axs[1].plot(df["MSD"], 'tab:orange')
    axs[1].set_title("MSD of random walk")
    axs[1].xaxis.set_major_locator(plt.MaxNLocator(7))
    axs[1].yaxis.set_major_locator(plt.MaxNLocator(7))
    axs[1].grid()
 
    plt.setp(axs[0], xlabel='Coordinate X')
    plt.setp(axs[0], ylabel='Coordinate Y')
    plt.setp(axs[1], xlabel='Mean Square Displacement of the random walk')
    plt.setp(axs[1], ylabel='Timesteps')
    plt.show()
    plt.savefig(output, dpi = 300)

if __name__ == "__main__":
    main(input, output)
