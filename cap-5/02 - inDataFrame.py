import pandas as pd


df=pd.read_csv('c:/Users/54112/Desktop/Big Data with Python/Big-Data/cap-5/data/titanic.csv')

print(df)

print(df.columns)
print(df.dtypes)

print(df.loc[0,'Fare'])
print(df.loc[:3,'Sex':'Fare'])
print(df.describe())
print(df.describe(include='all'))