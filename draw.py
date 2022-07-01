import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sio
import pandas as pd
import seaborn as sns

root = "./4/busy_"
savepath = "./4pic/"

noise_file = "./clean/1.mat"

noise_mat = sio.loadmat(noise_file)
noise = np.array(noise_mat.get("data"))

averages = np.average(noise, axis=1)
print(averages)

avg = max(averages)

busy = []

for i in range(1, 191):
    if i % 2 == 1:
        filename = root + str(i) + ".mat"
        mat = sio.loadmat(filename)
        data = mat.get("data")
        data = np.array(data)
        data[data < avg] = -110
        shrinkmat = np.max(data, axis=0)
        busy.append(shrinkmat)
        #df = pd.DataFrame(data)
        #sns.heatmap(df, cmap="Blues", vmax=-50, vmin=-110, xticklabels=False, yticklabels=True)

        #picture_name = savepath + str(i) + "_preprocessed.png"
        #plt.savefig(picture_name)
        #plt.show()

xticks = []
for i in range(0, 1600):
    if i == 399 or i == 899:
        xticks.append(str(i+1))
    else:
        xticks.append('')

busy = np.array(busy)
df = pd.DataFrame(busy)
sns.heatmap(df, cmap="Blues", vmax=-50, vmin=-110, xticklabels=xticks, yticklabels=False)\
    .set(title="Ok Google Activated")
plt.savefig("busy.png")
plt.show()
