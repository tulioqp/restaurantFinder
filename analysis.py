import functions as f
import pandas as pd


# 0. load data
df = f.load('data/zomato.csv')

# 1. data visualization
df.head()
df.shape                      # 7527, 21
# df1.dtypes                  # streamlit displays these infos, must comment
# df1[df1.isna()].count()     #
# df1[df1.isnull()].count()   # no NULL/NaN data :)


# 2. outliers
df.loc[df["Average Cost for two"] > 100000, ["Average Cost for two", "Restaurant Name", "City", "Locality", "Currency"]].sort_values('Average Cost for two', ascending=False)

filter = df['Average Cost for two'] > 10000000

df1 = f.cleanDataFrame(filter, df) # 1 row removed, 25kk dollar price 



# ----------------------

def DataFrame():
    '''
    function to return the final DataFrame to main.py
    '''

    return df1

# ----------------------
    

