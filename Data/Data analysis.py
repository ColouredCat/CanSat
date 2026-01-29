import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"log.csv")

df = df[["x", "y", "z", "temp", "pressure"]]

df["TurbulenceX"] = df["x"].rolling(20).std()
df["TurbulenceY"] = df["y"].rolling(20).std()
df["TurbulenceZ"] = df["z"].rolling(20).std()

df["TurbulenceX"] = (df["TurbulenceX"] - df["TurbulenceX"].mean()) / df["TurbulenceX"].std()
df["TurbulenceY"] = (df["TurbulenceY"] - df["TurbulenceY"].mean()) / df["TurbulenceY"].std()
df["TurbulenceZ"] = (df["TurbulenceZ"] - df["TurbulenceZ"].mean()) / df["TurbulenceZ"].std()


plt.plot(df["TurbulenceX"], label = "x")
plt.plot(df["TurbulenceY"], label = "y")
plt.plot(df["TurbulenceZ"], label = "z")
plt.legend()
plt.show()

