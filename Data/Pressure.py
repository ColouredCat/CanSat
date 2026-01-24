import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"pressure.csv")

df = df[["pressure"]]
df["altitude"] = 44330*((1-df["pressure"]/1013.5)*(1/5.225))



plt.plot(df["altitude"], label = "altitude")
plt.legend()
plt.show()