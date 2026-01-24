import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"temp.csv")

df = df[["temp"]]
df.dropna(inplace = True)

plt.plot(df["temp"], label = "temp")

plt.legend()
plt.show()