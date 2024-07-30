import streamlit as st
import functions as f
import analysis as a


# 0. load data
df1 = a.DataFrame() 


# 1. streamlit 
# 1.1 title
st.title(":violet[Find a Good Place to Eat] :fork_and_knife:", anchor=False)
st.title(":fries: :sushi: :icecream: :wine_glass:", anchor=False)
st.divider()


# 1.2 select box to choose a city
df_costs = f.citySelection(df1)


# 1.3 df.describe() values for slider parameters (min, max, 25% and 75%)
desc = df_costs['Average Cost for two'].describe()


# 1.4 slider for cost selection
cost = f.cost_slider(desc)

min_cost, max_cost = cost[0], cost[1]

filter = (df_costs['Average Cost for two'] >= min_cost) & (df_costs['Average Cost for two'] <= max_cost)


# 1.5 map plot
st.map(df_costs.loc[filter], latitude='Latitude', longitude='Longitude')


# 1.6 the names of the restaurants that match the filter
container = st.container(height=400, border=True)
container.title("Restaurants:")
container.write_stream(['{index}. {name} \n'.format(index=index, name=name) for index, name in enumerate (df_costs.loc[filter, 'Restaurant Name'])])

