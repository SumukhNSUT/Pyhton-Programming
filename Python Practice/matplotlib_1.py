# import numpy as np
# from matplotlib import pyplot as plt

# # Sample data
# x = [1, 2, 3, 4, 5]
# y = [2, 3, 5, 7, 11]

# # Create a plot
# plt.plot(x, y)

# # Add labels and title
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Simple Plot')

# # Display the plot
# plt.show()

import numpy as np
import matplotlib.pyplot as plt
# Compute the x and y coordinates for points on a sine curve
x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)
plt.title("sine wave form")
# Plot the points using matplotlib
plt.plot(x, y)
plt.show()
