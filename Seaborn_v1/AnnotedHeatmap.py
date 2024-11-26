import seaborn as sns; 
import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(10,12)

sns.heatmap(data, annot=True, linewidths=1.5, linecolor='gray')
plt.show()