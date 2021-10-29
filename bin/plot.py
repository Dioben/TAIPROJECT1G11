import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("result.txt", sep=" ", header=None)
df.columns=["Text Name","Order","Smoothing","Entropy"]

smallsmoothing = df.loc[df["Smoothing"]<0.2]

mediumsmoothing = df.loc[(df["Smoothing"]>=0.1)&(df["Smoothing"]<2)]

bigsmoothing = df.loc[df["Smoothing"]>0.9]

smallplot = smallsmoothing.plot(x="Smoothing",y="[Order]")
plt.show()