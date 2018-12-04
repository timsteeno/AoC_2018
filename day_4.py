import pandas as pd

df = pd.read_csv(filepath_or_buffer='day4_input.txt',
                 header=None,
                 sep="] ",
                 engine='python')
df.columns = ['date', 'action']

print(df.head())
