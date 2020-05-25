import numpy as np
import matplotlib.pyplot as plt


a = np.array([1, 75e-8]) * 10000
b = np.array([0.5, 5e-7])

ys = np.zeros(10)

ys[0] = b[0]
ys[1] = a[0] * ys[0]

for i in range(2, 10):
    window = ys[i-2:i][::-1]
    ys[i] = (a.dot(window) - a[0]*window[0]) / a[0]


plt.plot([x for x in range(10)], ys)
plt.show()
