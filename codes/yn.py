import numpy as np
import matplotlib.pyplot as plt
import scipy

n = np.linspace(0, 19, 20)
y = np.loadtxt('y.dat', dtype='double')

plt.stem(n, y)
plt.title('Filter Output')
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()
plt.show()