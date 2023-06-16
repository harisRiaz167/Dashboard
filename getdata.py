import pandas as pd
import plotly.express as px
import streamlit as st

def getLineChart(dataframe, brandname):
    dataframe = dataframe.drop(['date', 'time'], axis=1)
    brands = dataframe[(dataframe['event_type'] == 'purchase')]
    brands = brands[['brand', 'price']]
    start_date = '2019-01-01'
    brands['date'] = pd.date_range(start=start_date, periods=len(brands), freq='D')
    my_df = brands[brands['brand'] == brandname]
    
    fig = px.line(my_df, x='date', y='price')

    return fig

def getPieChart(dataframe, brandname):
    events = dataframe[dataframe['brand'] == brandname]
    events = events[['event_type']].value_counts().reset_index()
    events.columns = ['event_type', 'count']
    fig2 = px.pie(events,'event_type','count')
    return fig2

def getbarchart(dataframe,brandname):
    dataframe = dataframe[dataframe['brand'] == brandname] 
    dataframe =  dataframe[dataframe['event_type'] == 'purchase']
    dataframe = dataframe['category_code'].value_counts().reset_index().head(4)
    dataframe.columns = ['category_code','count']
    fig3 = px.bar(dataframe, x='category_code', y='count', color='category_code' )
    return fig3

def gethorizontalchart(dataframe,brandname):
    dataframe = dataframe[dataframe['event_type'] == 'purchase']
    dataframe = dataframe[dataframe['brand'] == brandname] 
    dataframe = dataframe['user_id'].value_counts().head(5).reset_index()
    dataframe.columns = ['user_id', 'count']
    fig4 = px.bar(dataframe, x='count', y='user_id',orientation='h') 
    fig4.update_layout(yaxis = dict(tickformat = ',d'))
    return fig4

def getTotalsales(dataframe,brandname):
    dataframe = dataframe[(dataframe['event_type'] == 'purchase') & (dataframe['brand'] == brandname)]
    dataframe = dataframe.groupby('brand')['price'].sum().reset_index()
    dataframe.columns = ['brand', 'price']
    dataframe = st.metric(label='Total Sales', value=dataframe['price'])
    return dataframe

