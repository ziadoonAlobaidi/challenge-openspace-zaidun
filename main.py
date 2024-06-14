# from table import Table, Seat
# from openspace import Openspace
import pandas as pd
a = 6
b = 4

df_names = pd.read_excel('./utils/Example Excel Template.xlsx')

names = df_names.iloc[1:25, 0]

a2 = []

for x in names:
    a2.append(x)
print(a2)



