import pandas as pd
data=pd.read_csv("Data.csv")

k=data["Min point"][0]
k=k.strip("(").strip(")")
print(k)
