
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd


rng = np.random.RandomState(0)

x = np.linspace(0,10,500)
y = np.cumsum(rng.randn(500,6),0)
sns.set()
sns.set_style("ticks")

plt.plot(x,y)
plt.legend('ABCDEF', ncol=3,loc = 'upper left')
plt.xlabel('X')
plt.ylabel('Y')

data = np.random.multivariate_normal([0, 0], [[5, 2], [2, 2]], size=1000)
data = pd.DataFrame(data, columns=['x','y'])

plt.figure()

# Normalized Histogram plot
for col in 'xy':
    plt.hist(data[col], density=True,alpha=0.5)

# KDE plot
plt.figure()

for col in 'xy':
    sns.kdeplot(data[col], shade=True)

# Dist plot - combination of KDE and Hist plots

sns.distplot(data['x'])
sns.distplot(data['y'])

plt.figure()

#sns.kdeplot("x","y",data)

plt.figure()

sns.jointplot("x","y",data, kind ='hex')

plt.figure()

B = np.random.rand(10,10)

#data2 = data.pivot("x","y")
sns.heatmap(data, center =0)