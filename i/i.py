import math
import sys
import matplotlib.pyplot as plt
import numpy as np

def sinus_cosinus(x):
    return math.sin(x), math.cos(x)
    x = np.arange(0, 4* np.pi, 0.1)
    y = np.sin(x)
    plt.plot(x,y)
plt.show()

