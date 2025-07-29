import matplotlib.pyplot as plt
import numpy as np

languages = ['Java','Python','PHP','JavaScript','C#','C++']
popularity = [22.2, 17.6, 8.8, 8.0, 7.7, 6.7]

plt.pie(popularity, labels=languages)
plt.title("Popularity of Programming Languages")
plt.show()
