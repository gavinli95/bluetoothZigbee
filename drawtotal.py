import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sio
import pandas as pd
import seaborn as sns


def cleanMat(_data, _averages):
    [row, col] = _data.shape
    result = np.zeros([row, col])
    for m in range(0, row):
        for n in range(0, col):
            if _data[m][n] < _averages[m][n]:
                result[m][n] = -110
            else:
                result[m][n] = _data[m][n]
    return result


root_idle = "./2/"
root_busy = "./4/"

saveroot = "./1pic/"

items = []
busy = []
idle = []

for i in range(1, 101):
    filename = ""
    if i % 2 == 0:
        filename = root_idle + "idle_" + str(i) + ".mat"
        mat = sio.loadmat(filename)
        data = mat.get("data")
        averages = np.average(data, axis=1)
        #average = max(averages)
        #data[data <= average] = -110
        #data = np.max(data, axis=0)
        averages = np.tile(averages.T, (1600, 1)).T
        cleanmat = cleanMat(data, averages)
        cleanmat = np.max(cleanmat, axis=0)
        idle.append(cleanmat)
    else:
        filename = root_busy + "busy_" + str(i) + ".mat"
        mat = sio.loadmat(filename)
        data = mat.get("data")
        averages = np.average(data, axis=1)
        #average = max(averages)
        #data[data <= average] = -110
        #data = np.max(data, axis=0)
        averages = np.tile(averages.T, (1600, 1)).T
        cleanmat = cleanMat(data, averages)
        cleanmat = np.max(cleanmat, axis=0)
        busy.append(cleanmat)
items = busy + idle
print(np.array(items).shape)

df = pd.DataFrame(busy)
sns.heatmap(df, cmap="Blues", xticklabels=False, yticklabels=False)
plt.show()

df = pd.DataFrame(idle)
sns.heatmap(df, cmap="Blues", xticklabels=False, yticklabels=False)
plt.show()

df = pd.DataFrame(items)
sns.heatmap(df, cmap="Blues", xticklabels=False, yticklabels=False)
plt.show()
