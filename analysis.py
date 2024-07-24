import functions as f
import pandas as pd

# test purposes
import importlib
importlib.reload(f)

# load data
df1 = f.load('data/zomato.csv')


df1.head()

df1.shape # 7527, 21

df1.loc[df1["Average Cost for two"] > 100000, ["Average Cost for two", "Restaurant Name", "City", "Locality", "Currency"]].sort_values('Average Cost for two', ascending=False)

def dataframe():

    price25kk = df1.loc[df1["Average Cost for two"] > 10000000]
    
    return df1.drop(price25kk.index)
    

# df1.dtypes # streamlit está printando essas duas linhas 

# df1[df1.isna()].count()     #
# df1[df1.isnull()].count()   # no NULL/NaN data :)

# object data type
# cols_obj = [col for col in df1.columns if df1[col].dtype == object]

# average cost for two and coordinates (long, lat)
# avg_coord = df1[['Average Cost for two', 'Longitude', 'Latitude']]