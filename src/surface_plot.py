from mpl_toolkits import mplot3d
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("result.txt", sep=" ", header=None)
df.columns=["Text_name","Order","Smoothing","Entropy"]

x = [i["Order"] for _, i in df.groupby('Order', as_index=False).first().iterrows()]
# y = [i["Smoothing"] for _, i in df.groupby('Smoothing', as_index=False).first().iterrows()]
smoothing = [
    [0.0001,0.001,0.01],
    [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9],
    [1,2,3,4,5,6,7,8,9,10],
    [0.0001,0.001,0.01,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,2,3,4,5,6,7,8,9,10]]

text_groups = df.groupby('Text_name', as_index=False)
for _, i in text_groups.first().iterrows():
    for name in i["Text_name"].split("\n"):
        for y in smoothing:
            data = text_groups.get_group(name)

            def z_function(x, y):
                r = [[-1 for __ in range(len(x[0]))] for _ in range(len(x))]
                for i in range(len(x)):
                    for ii in range(len(x[0])):
                        r[i][ii] = data.loc[(data["Order"] == x[i][ii]) & (data["Smoothing"] == y[i][ii])]["Entropy"].iloc[0]
                return np.array(r)

            X, Y = np.meshgrid(x, y)
            Z = z_function(X, Y)

            fig = plt.figure()
            ax = plt.axes(projection="3d")
            ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                            cmap='winter', edgecolor='none')
            ax.set_xlabel('order')
            ax.set_ylabel('smoothing')
            ax.set_zlabel('entropy')
            ax.set_title(name)

            plt.show()