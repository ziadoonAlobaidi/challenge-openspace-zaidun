from utils.openspace import Openspace

from utils.table import Table, Seat
import pandas as pd

n_tables = 6
n_seats = 4

df = pd.read_excel('./utils/Example Excel Template.xlsx')

colleagues_list = df['Colleagues'].tolist()

#print(colleagues_list)

space= Openspace(n_tables,n_seats)

print(space.organize(colleagues_list))


