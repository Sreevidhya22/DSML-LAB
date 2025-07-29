import matplotlib.pyplot as plt
import numpy as np
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8.0, 7.7, 6.7]
colors = ['red', 'blue', 'green', 'orange', 'black', 'yellow']
plt.barh(languages, popularity, color=colors)
plt.xlabel('Popularity (%)')
plt.title('Programming Language Popularity')
plt.show()

