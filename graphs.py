# Import pandas
import pandas as pd

# Load the CSV data into DataFrames
super_bowls = pd.read_csv('databases/super_bowls.csv')
tv = pd.read_csv('databases/tv.csv')
halftime_musicians = pd.read_csv('databases/halftime_musicians.csv')

# print the first five rows of each DataFrame
print(super_bowls.head())
print(tv.head())
print(halftime_musicians.head())