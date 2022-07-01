import matplotlib.pyplot as plt
import numpy
import numpy as np
import scipy.io as sio
import pandas as pd
import seaborn as sns

root = "./data/"

noise_file = "./clean/1.mat"

noise_mat = sio.loadmat(noise_file)
noise = np.array(noise_mat.get("data"))

averages = np.average(noise, axis=1)
print(averages)
avg = max(averages)
total = np.zeros(noise.shape)

for i in range(1, 52):
    filename = root + str(i) + ".mat"
    mat = sio.loadmat(filename)
    data = mat.get("data")
    data = np.array(data)
    data[data < avg] = -110
    total += data
total = total / 51
total = numpy.sum(total, axis=0) / 16
df = pd.DataFrame(total)
df = df.T
print(df.shape)
xticks = []
for i in range(0, 1600):
    if i == 399 or i == 899:
        xticks.append(str(i+1))
    else:
        xticks.append(' ')
#sns.set(rc={'figure.figsize':(16, 1)})
sns.heatmap(df, cmap="Blues", xticklabels=xticks,
            yticklabels=False, cbar_kws=dict(use_gridspec=False, location="right"))
picture_name = root + "added.png"
plt.savefig(picture_name)
plt.show()


