import numpy as np
import matplotlib.pyplot as plt

T = 0.00001

a = np.array([1, 75e-2])
b = np.array([1, 5e-1])

ys = np.zeros(2000)

ys[0] = b[0]
ys[1] = a[0] * ys[0]

for i in range(2, 2000):
    window = ys[i-2:i][::-1]
    ys[i] = (a.dot(window) - a[0]*window[0]) / a[0]


# plt.plot([x for x in range(100)], ys[:100])
# plt.show()


def discrete_d(var, point, deg=1):

    idx = int(point / T)
    if idx < deg:
        return 0

    out = np.zeros(var.shape)
    for i in range(1, var.shape[0]):
        out[i] = (var[i] - var[i-1]) / T
    if deg == 1:
        return out[idx]
    return discrete_d(out, point, deg=deg-1)


# y = np.array([(x)**2 for x in np.arange(0, 2, T)])

# print(discrete_d(y, 0.5, deg=1))  # should output 1
# print(discrete_d(y, 1, deg=2))  # should output 2
# print(discrete_d(y, 1, deg=3))  # should output 0
# # np.arange(0, 10, T).shape


y = np.array([(x)**4 for x in np.arange(0, 2, T)])


print(discrete_d(y, 0.5, deg=1))  # should output 0.5
print(discrete_d(y, 0.5, deg=2))  # should output 3
print(discrete_d(y, 0.5, deg=3))  # should output 12
print(discrete_d(y, 0.5, deg=4))  # should output 24
print(discrete_d(y, 0.5, deg=5))  # should output 0
# np.arange(0, 10, T).shape
