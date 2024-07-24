import streamlit as st
import functions as f
import analysis as a

# test purposes
import importlib
importlib.reload(f)
importlib.reload(a)


# 0. load data
df1 = a.dataframe() # 1 row removed, 25kk dollar price 

# f.test(df1)

# 1. streamlit 
# 1.1 title
st.title(":violet[Find a Good Place to Eat] :fork_and_knife:", anchor=False)
st.title(":fries: :sushi: :icecream: :wine_glass:", anchor=False)
st.divider()

# 1.2 select box to choose a city
city = st.selectbox('Select City', df1['City'].unique(), placeholder="Choose an Option", index=None)

# avg cost for two, coordinates and restaurant name for the chosen city
if city:
    df_costs = df1.loc[(df1['City'] == city) & (df1['Average Cost for two'] > 0), ['Average Cost for two', 'Latitude', 'Longitude', 'Restaurant Name']]
else:
    df_costs = df1.loc[(df1['Average Cost for two'] > 0), ['Average Cost for two', 'Latitude', 'Longitude', 'Restaurant Name']]


# 1.3 describe values for slider parameters (min, max, 25% and 75%)
desc = df_costs['Average Cost for two'].describe()

min_value, max_value       = desc.iloc[3], desc.iloc[7] # min, max (slider range)
initial_value, final_value = desc.iloc[4], desc.iloc[6] # 25%, 75% (initial slider position)

# slider for cost selection
if min_value != max_value:
    cost = st.slider('Select Cost Range (Local Currency :money_with_wings: :moneybag:)', min_value=min_value, max_value=max_value, value=(initial_value, final_value))
else:
    cost = st.slider('Select Cost Range (Local Currency :money_with_wings: :moneybag:)', min_value=min_value-10, max_value=max_value, value=(initial_value-10, final_value))


filter = (df_costs['Average Cost for two'] >= cost[0]) & (df_costs['Average Cost for two'] <= cost[1])

st.map(df_costs.loc[filter], latitude='Latitude', longitude='Longitude')



container = st.container(height=400, border=True)
container.title("Restaurants:")
container.write_stream(['{index}. {name} \n'.format(index=index, name=name) for index, name in enumerate (df_costs.loc[filter, 'Restaurant Name'])])

