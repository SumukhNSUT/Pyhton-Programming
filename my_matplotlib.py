# import numpy as np
# from matplotlib import pyplot as plt

# x = np.arange(0, 5)
# y = x

# plt.plot(x, y)
# plt.show()

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 11)
y1 = x + 1
y2 = x + 5
plt.title("Matplotlib demo")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.plot(x, y1, label="student 1")
plt.plot(x, y2, label="student 2")
plt.legend(loc=2)

plt.show()
