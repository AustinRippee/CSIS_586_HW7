import pandas as pd
df = pd.read_csv('ssn.txt', header=None, index_col=None)

#each value in part of the same column
#therefore this is to split each value into it's own column
df = df[0].str.split(' ', expand=True)

#counts the number of values in the row
idk = df['count'] = df.iloc[:, 2:].notnull().sum(axis=1)

#counts the values together based on the value of column 0
grouped = df.groupby(0)['count'].sum()

#sorts the data with highest on top
grouped_sorted = grouped.sort_values(ascending=False)

#gets top value with most number of friends
top_value = grouped_sorted.head(1)

#gets the key and value of the top value
for key, value in top_value.items():
    print(f"The most popular person's ID is {key} with {value} friends.")