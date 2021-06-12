import matplotlib.pyplot as plt
import numpy as np
import tidynamics

# Generate random numbers of +1 or -1
steps = -1 + 2*np.random.randint(0, 2, size=1000)
# Add the steps to obtain the position
position = np.cumsum(steps)

plt.figure()
plt.plot(position)
plt.xlabel('time')
plt.title('Position as a function of time for a random walk')

plt.figure()
plt.plot(tidynamics.msd(position))
plt.xlabel('lag')
plt.title('Mean-square displacement for the random walk')
plt.show()
plt.savefig("Test1_fig2.png")

