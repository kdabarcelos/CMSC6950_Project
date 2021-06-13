import numpy as np
import tidynamics
import matplotlib.pyplot as plt

input = np.loadtxt("random_steps_sample_0.txt.gz")

result = tidynamics.acf(input)

plt.figure()
plt.plot(input)
plt.xlabel('time')
plt.title('data')
plt.show()
plt.savefig("Test3_random_steps_sample.png", dpi = 300)

plt.figure()
plt.plot(result)
plt.xlabel('time')
plt.title('data')
plt.show()
plt.savefig("Tes3_random_steps_acf.png")

np.savetxt("random_steps_values.txt",input)
