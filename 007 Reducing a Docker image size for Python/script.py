import pandas as pd 

df=pd.read_csv('data/data.csv')
print("Data Preview")
print(df.head())

print("\nStatistical Summary: ")
print(df.describe())

print(f"\nTotal rows: {len(df)}")
print(f"Average Salary: ${df['Salary'].mean():,.2f}")
