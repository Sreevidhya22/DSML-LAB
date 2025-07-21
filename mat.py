import numpy as np
import matplotlib.pyplot as plt
x=np.array([1,2,6,18])
y=np.array([3,10,12,20])
plt.title("Draw line")
plt.plot(x,y,color="red",linestyle="dotted",marker="o",mfc="green",mec="green")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()
