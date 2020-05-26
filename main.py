import numpy as np
import matplotlib.pyplot as plt


step = np.array([x > 1 for x in range(100)])
impulse = np.array([x == 2 for x in range(100)])
impulse[0] = 1


def history_diff(inp):
    if len(inp) == 1:
        return inp[0]

    out = np.zeros(len(inp)-1)
    for i in range(len(out)):
        out[i] = (inp[i+1] - inp[i]) / T

    return history_diff(out)


T = 0.01

a = np.array([1, 75e-2])
b = np.array([1, 5e-1])

ys = np.zeros(100)


for i in range(2, len(ys)):
    b_window = step[i-len(b):i]
    grad = np.array([history_diff(ys[i-x:i]) for x in range(1, len(a))])
    ys[i] = a[1:].dot(grad)
    ys[i] = ys[i] + b_window.dot(b)

plt.plot([x for x in range(2, 100)], ys[2:])
plt.show()
