import pandas as pd
import streamlit as st
import plotly.express as px
from getdata import getLineChart, getPieChart,getbarchart,getbarchartcust,getTotalsales

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
    st.plotly_chart(getbarchartcust(df,options))



