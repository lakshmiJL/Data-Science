import pandas as pd

data = pd.read_csv("L4/titanic.csv")

data.iloc[0:3, 3] = "Pulkit Chawla"
print(data["Name"])
