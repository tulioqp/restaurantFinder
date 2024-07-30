import pandas as pd
import streamlit as st


def load(path):
    '''
    function to read csv data. input: string path; return: df (pd.DataFrame)
    '''

    df = pd.read_csv(path)

    return df
# ----------------------

def cleanDataFrame(filter : pd.DataFrame, df: pd.DataFrame):
    '''
    function to clean the dataframe. input: filter (pd.DataFrame) and the original df (pd.DataFrame); return df (pd.DataFrame) without filtered rows
    '''
    
    remove = df.loc[filter]
    
    return df.drop(remove.index)

# ----------------------

def citySelection(df : pd.DataFrame):
    '''
    function to select a city. input: df (pd.DataFrame); return: df_costs (pd.DataFrame) with avg costs for two, coordinates and restaurants for the chosen city
    '''

    # streamlit selectbox
    city = st.selectbox('Select City', df['City'].unique(), placeholder="Choose an Option", index=None)

    # avg cost for two, coordinates and restaurant name for the chosen city
    if city:
        df_costs = df.loc[(df['City'] == city) & (df['Average Cost for two'] > 0), ['Average Cost for two', 'Latitude', 'Longitude', 'Restaurant Name']]
    else:
        df_costs = df.loc[(df['Average Cost for two'] > 0), ['Average Cost for two', 'Latitude', 'Longitude', 'Restaurant Name']]

    return df_costs


# ----------------------

def cost_slider(desc : pd.Series):
    '''
    function to select initial and final price values. input: desc (pd.Series) as a variable for df.describe(); return cost (st.slider) slider 
    '''

    min, max        = desc.iloc[3], desc.iloc[7] # min, max (slider range)
    init, final     = desc.iloc[4], desc.iloc[6] # 25%, 75% (initial slider position)

    # slider for cost selection
    if min != max:
        cost = st.slider('Select Cost Range (Local Currency :money_with_wings: :moneybag:)', min_value=min, max_value=max, value=(init, final))
    else:
        cost = st.slider('Select Cost Range (Local Currency :money_with_wings: :moneybag:)', min_value=min-10, max_value=max, value=(init-10, final))
    
    return cost

# ----------------------