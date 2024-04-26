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

#Grafico de torta
labels = 'Caballos', 'Cerdos', 'Perros', 'Vacas'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
shadow=True, startangle=90)
plt.axis('equal')
plt.show()