import math
import sys
import matplotlib.pyplot as plt
import numpy as np

def sinus_cosinus():
    x = np.arange(0, 4* np.pi, 0.1)
    y = np.sin(x)
    z = np.cos(x)
    plt.plot(x,y,x,z)
    plt.show()
sinus_cosinus()
def 

