import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


df = pd.DataFrame({ "x": [1,2,3,4,5], "y": [6,7,8,9,0]})
plt.plot(df["x"], df["y"])
plt.title("Título con pandas")
plt.show()


# x = np.linspace(0,5, 11)
# y = x ** 2


# plt.plot(x, y)
# plt.title('a')
# plt.grid(True)
# plt.show() 