import matplotlib.pyplot as plt
import numpy as np
maths_marks = [88, 92, 80, 100, 80, 60, 100, 80, 34]
science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20]
plt.scatter(maths_marks, science_marks, color='red')
plt.xlabel('Maths Marks')
plt.ylabel('Science Marks')
plt.title('Scatter Plot: Maths vs Science Marks')
plt.grid(True)
plt.show()

