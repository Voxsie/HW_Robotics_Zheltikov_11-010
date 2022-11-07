import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy.stats import gaussian_kde
from sklearn.neighbors import KernelDensity

j = 500000
count = 1000
values = []
dist_frac = 0.1

for i in range(0,count):
 x1 = np.random.normal(-5, 2, int(j*(1-dist_frac)))
 x2 = np.random.normal(5, 3, int(j*dist_frac))
 x = np.concatenate((x1, x2))
 values.append(x.mean())

plt.title("Density of {} samples".format(count))

sns.kdeplot(values)
sns.distplot(values)

plt.legend(['sample mean', 'histogram'])

plt.show()