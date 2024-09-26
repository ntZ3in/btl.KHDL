import pandas as pd

df = pd.read_csv('./data/demo1.csv')
df['word_count'] = df['post_text'].apply(lambda x: len(x.split()))
df['link'] = df['link']
df[['link', 'post_text', 'word_count']].to_csv('./data/word_count.csv', index=False)