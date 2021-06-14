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


