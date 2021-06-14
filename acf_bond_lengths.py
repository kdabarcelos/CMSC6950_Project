import matplotlib.pyplot as plt
import numpy as np
import tidynamics
import pandas as pd

#loading bond length between C=O and C-H during 800 to 1500 ns from my MD simulation
dataCH = np.loadtxt("test800-1500ns-CH.txt")
dataCO = np.loadtxt("test800-1500ns-CO.txt")

#Creating dataframe into variables
dfCH = pd.DataFrame(dataCH, columns=["Time","Length"])
dfCO = pd.DataFrame(dataCO, columns=["Time","Length"])

#Applying autocorrelation function (acf) in length of C=O and C-H
acf_CH = tidynamics.acf(dfCH["Length"])
acf_CO = tidynamics.acf(dfCO["Length"])

fig, axs = plt.subplots(2,2,figsize=(7,6))
plt.subplots_adjust(wspace=0.55, hspace=0.4)

axs[0, 0].plot(dfCH["Time"],dfCH["Length"])
axs[0, 0].set_xlim([800,1000])
axs[0, 0].set_title("CH bond length")
axs[0, 0].xaxis.set_major_locator(plt.MaxNLocator(4))
axs[0, 0].yaxis.set_major_locator(plt.MaxNLocator(6))
axs[0, 0].grid()

axs[0, 1].plot(acf_CH, 'tab:orange')
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

axs[1, 1].plot(acf_CO, 'tab:orange')
axs[1, 1].set_title("Autocorrelation of CO")
axs[1, 1].xaxis.set_major_locator(plt.MaxNLocator(6))
axs[1, 1].yaxis.set_major_locator(plt.MaxNLocator(6))
axs[1, 1].grid()

plt.setp(axs[:,0], xlabel='Time (ns)')
plt.setp(axs[:,1], xlabel='Lag')
plt.setp(axs[:,0], ylabel='Length (nm)')
plt.setp(axs[:,1], ylabel='Autocorrelation')
plt.show()
plt.savefig("CO_CH_bond_length_acf.png", dpi = 300)
