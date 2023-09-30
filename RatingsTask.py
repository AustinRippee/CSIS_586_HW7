import pandas as pd
df = pd.read_csv('ratings.csv', names=['userID', 'movieID', 'rating', 'timestamp'])

#filters only by whole numbers
df = df[df['rating'] % 1 == 0]

#gets rid of the decimals by converting to an integer
df['rating'] = df['rating'].apply(int)

#groups all the ratings
rating_count = df.groupby('rating')['movieID'].count().reset_index()

#sets column names
rating_count.columns=['Rating', '# of Ratings']

print(rating_count)