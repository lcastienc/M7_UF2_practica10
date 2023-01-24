import pandas as pd

test = pd.read_csv("test.csv")
#print(test)

#pillar valores concretos

selecId = test.columns(3)
print(selecId)