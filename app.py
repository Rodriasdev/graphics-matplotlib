import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from random import sample 


df = pd.DataFrame({ "x": [1,2,3,4,5], "y": [6,7,8,9,0]})
plt.plot(df["x"], df["y"])
plt.title("Título con pandas")
plt.grid(True)

#Grafico de barras
data = sample(range(1, 1000), 100)
plt.hist(data,bins = 10)
plt.title("Histograma")
plt.show()
