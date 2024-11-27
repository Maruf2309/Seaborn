import seaborn as sns; import matplotlib.pyplot as plt

# 3. Bar plot
data = sns.load_dataset("tips")
sns.barplot(x='day', y='total_bill', data=data, ci="sd")
plt.show()