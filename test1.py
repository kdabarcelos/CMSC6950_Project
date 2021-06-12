import matplotlib.pyplot as plt
import numpy as np
import tidynamics

data = -1+2*np.random.random(size=1000)

plt.figure()
plt.plot(data)
plt.xlabel('time')
plt.title('data')

plt.figure()
plt.plot(tidynamics.acf(data))
plt.xlabel('lag')
plt.title('autocorrelation function of data')
plt.show()
plt.savefig("Test1_fig1.png")
