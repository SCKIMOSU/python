import numpy as np
import matplotlib.pyplot as plt

x = np.random.lognormal(0, 1, 10000)
plt.hist(x, bins=50, color='g')
