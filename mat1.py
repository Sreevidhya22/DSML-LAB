import matplotlib.pyplot as plt
import numpy as np
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("2 LINES PLOTTED GRAPH")
x1=[1, 2, 3, 4]
y1=[2, 4, 6, 8]
x2=[2, 4, 5, 7]
y2=[1, 3, 2, 5]
plt.plot(x1, y1, marker='o', linestyle=':', color='red',mec='green',mfc='green',label="LINE 1")
plt.plot(x2, y2, marker='o', linestyle='solid', color='black',mec='blue',mfc='blue',label="LINE 2")
plt.legend()
plt.show()
