import pandas as pd
import pyvi
from pyvi import ViTokenizer

# Load the CSV file
df = pd.read_csv('./data/daucau.csv')

# Tokenize the post_text column using PyVi
tokenized_posts = df['post_text'].apply(lambda x: ViTokenizer.tokenize(x))

# Create a new DataFrame with the tokenized posts
tokenized_df = pd.DataFrame({'tokenized_post': tokenized_posts})

# Save the tokenized data to a new CSV file
tokenized_df.to_csv('./data/tokenized_output.csv', index=False)