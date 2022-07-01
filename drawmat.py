import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sio
import pandas as pd
import seaborn as sns

root = "./4/"
prefix = "busy_"

i = 1
while i <= 199:
    filepath = root + prefix + str(i) + ".mat"
    mat = sio.loadmat(filepath)
    data = mat.get("data")
    data = np.array(data)
    df = pd.DataFrame(data)
    sns.heatmap(df, cmap="Blues", vmax=-50, vmin=-110, xticklabels=False, yticklabels=False)
    plt.savefig(root + str(i) + ".png")
    plt.show()
    i += 2
