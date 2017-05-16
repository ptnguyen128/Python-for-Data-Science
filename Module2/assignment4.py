import pandas as pd
import numpy as np

# TODO: Load up the table, and extract the dataset
# out of it. If you're having issues with this, look
# carefully at the sample code provided in the reading
#
# .. your code here ..
html = pd.read_html('http://espn.go.com/nhl/statistics/player/_/stat/points/sort/points/year/2015/seasontype/2',header=1)
df = pd.DataFrame(html[0])
# TODO: Rename the columns so that they match the
# column definitions provided to you on the website
#
# .. your code here ..


# TODO: Get rid of any row that has at least 4 NANs in it
#
# .. your code here ..
df = df.dropna(thresh=13)

# TODO: At this point, look through your dataset by printing
# it. There probably still are some erroneous rows in there.
# What indexing command(s) can you use to select all rows
# EXCEPT those rows?
#
# .. your code here ..
print df
df = df[~(df['PLAYER']=='PLAYER')]

# TODO: Get rid of the 'RK' column
#
# .. your code here ..
df = df.drop('RK',1)

# TODO: Ensure there are no holes in your index by resetting
# it. By the way, don't store the original index
#
# .. your code here ..
df = df.reset_index(drop=True)


# TODO: Check the data type of all columns, and ensure those
# that should be numeric are numeric
df.dtypes
df = df.apply(lambda df: pd.to_numeric(df, errors='coerce')

# TODO: Your dataframe is now ready! Use the appropriate 
# commands to answer the questions on the course lab page.

len(df.PCT.unique())
df.GP[15]+df.GP[16]