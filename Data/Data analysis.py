import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"log.csv")

df = df[["x", "y", "z", "temp", "pressure"]]

df["TurbulenceX"] = df["x"].rolling(20).std()
df["TurbulenceY"] = df["y"].rolling(20).std()
df["TurbulenceZ"] = df["z"].rolling(20).std()


plt.plot(df["TurbulenceX"], label = "x")
plt.plot(df["TurbulenceY"], label = "y")
plt.plot(df["TurbulenceZ"], label = "z")
plt.legend()
plt.show()

