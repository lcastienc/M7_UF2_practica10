#Importamos pandas
import pandas as pd

test = pd.read_csv("test.csv")
#print(test)

#pillar valores concretos

selecId = test[test['id']]
print(selecId)