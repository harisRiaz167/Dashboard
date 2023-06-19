import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from getdata import getLineChart, getPieChart,getbarchart,getpiechartcust,getTotalsales

st.set_page_config(page_title = 'Sales Dashboard', layout='wide')
df = pd.read_csv('./data/final.csv')

# brands = df['brand'].sort_values(ascending=True).unique()
brands = df['brand'].value_counts().head(10).reset_index()
brands.columns = ['brand', 'count'] 
brands = brands['brand']
with st.sidebar:
     options = st.selectbox("Choose Brand for Details", options=brands)

st.title('Sales Dashboard')
st.markdown('visulization for the sales data, important insight provided of top brands with sidebar option')

getTotalsales(df,options)

fig1, fig2 = st.columns(2)
with fig1:
    st.subheader('Price of brands')
    st.plotly_chart(getLineChart(df, options))
with fig2:
    st.subheader('Events')
    st.plotly_chart(getPieChart(df,options))

fig3,fig4 = st.columns(2)
with fig3:
   st.subheader('Top Category')
   st.plotly_chart(getbarchart(df,options))
with fig4:
    st.subheader('Top Customers id')
    st.plotly_chart(getpiechartcust(df,options))

# Price Comparison of brands
data = df.drop('date',axis=1)
start_date = '2019-01-01'
data['final_date'] = pd.date_range(start=start_date, periods=len(data), freq='D')
st.header('Price comparison of brands')
def plot():

    df = data

    clist = df["brand"].value_counts().head(10).reset_index()

    brands = st.multiselect("Select brand", clist)
    st.header("You selected: {}".format(", ".join(brands)))

    dfs = {brand: df[df["brand"] == brand] for brand in brands}

    fig = go.Figure()
    for brand, df in dfs.items():
          fig = fig.add_trace(go.Scatter(x=df["final_date"], y=df["price"], name=brand))
    st.plotly_chart(fig, use_container_width=True)

plot()
