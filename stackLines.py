import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def fnx(): return np.random.randint(3, 10, 10)


y = np.row_stack((fnx(), fnx(), fnx()))
# this call to 'cumsum' (cumulative sum), passing in your y data,
# is necessary to avoid having to manually order the datasets
x = np.arange(10)

print(y.shape)
y_stack = np.cumsum(y, axis=0)   # a 3x10 array

fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.fill_between(x, 0, y_stack[0, :], facecolor="#CC6666", alpha=.7, label='yeeyee')
ax1.fill_between(x, y_stack[0, :], y_stack[1, :], facecolor="#1DACD6", alpha=.7)
ax1.fill_between(x, y_stack[1, :], y_stack[2, :], facecolor="#6E5160")

plt.show()
