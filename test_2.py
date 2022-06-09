import pandas as pd
import glob

# append file into Pandas DataFrame
df = pd.DataFrame()

for i in glob.glob('transaction/*.xlsx'):
	df_read = pd.read_excel(i)
	df = pd.concat([df, df_read], ignore_index=True)

df.to_excel('merge.xlsx', index=False)

# merge data using inner join and defined specific column to merge
df = pd.read_excel('merge.xlsx')
df_master = pd.read_excel('master.xlsx')

df_merge = df.merge(df_master, on='Fruit')

# option you can change column name
df_merge.rename(columns={
	'Fruit': 'Name'
	}, inplace=True)

print(df_merge)