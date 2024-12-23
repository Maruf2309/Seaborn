import seaborn as sns; import matplotlib.pyplot as plt
data = sns.load_dataset("iris").drop(columns=["species"])
sns.clustermap(data, cmap='plasma')
plt.show()