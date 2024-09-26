import pandas as pd
import string

df = pd.read_csv('./data/demo1.csv')

# Create a translator to remove non-alphanumeric characters and specific whitespace characters
translator = str.maketrans('', '', string.punctuation)

# Remove remaining non-alphanumeric characters
df['post_text'] = df['post_text'].apply(lambda x: ''.join(e for e in x if e.isalnum() or e.isspace()))

df['post_text'] = df['post_text'].apply(lambda x: x.lower())

# Apply the translator to the 'post_text' column
df['post_text'] = df['post_text'].apply(lambda x: x.translate(translator))

# # Identify the lines that mark the end of the desired data
# def is_marker_line(row):
#     row_str = str(row.values)
#     return set(row_str) in [set('-'), set('_')]

# # Find the index of the first occurrence of a marker line
# for index, row in df.iterrows():
#     if is_marker_line(row):
#         break
# # Remove all lines after the marker line
# df = df.head(index)

df['link'] = df['link']
df[['link', 'post_text']].to_csv('./data/daucau.csv', index=False)