import numpy as np
from matplotlib import pyplot as plt

x = np.arange(1, 11)
y = 2*x + 5

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of y = 2x + 5')
plt.grid(True)
plt.show()