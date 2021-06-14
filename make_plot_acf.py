import matplotlib.pyplot as plt
import pandas as pd
import sys

args = sys.argv[1:]
input1 = args[0]
input2 = args[1]
output = args[2]

def main(input1, input2, output):
    '''
    X
    '''
    dfCH = pd.read_csv(input1)
    dfCO = pd.read_csv(input2)

    fig, axs = plt.subplots(2,2,figsize=(7,6))
    plt.subplots_adjust(wspace=0.55, hspace=0.4)

    axs[0, 0].plot(dfCH["Time"],dfCH["Length"])
    axs[0, 0].set_xlim([800,1000])
    axs[0, 0].set_title("CH bond length")
    axs[0, 0].xaxis.set_major_locator(plt.MaxNLocator(4))
    axs[0, 0].yaxis.set_major_locator(plt.MaxNLocator(6))
    axs[0, 0].grid()

    axs[0, 1].plot(dfCH["AutoCorr"], 'tab:orange')
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

    axs[1, 1].plot(dfCO["AutoCorr"], 'tab:orange')
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
