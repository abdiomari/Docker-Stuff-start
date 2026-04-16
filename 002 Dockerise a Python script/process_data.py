import pandas as pd 

# read the csv file 
df = pd.read_csv('data/data.csv')

print("\n---- Data Preview ----")
print(df.head())

print("\n---- Statistical Summary ----")
print(df.describe())

print("\n---- Average Salary ----")
print(f"Average Salary: ${df['Salary'].mean():,.2f}")