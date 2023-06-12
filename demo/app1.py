import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import altair as alt

uploaded_file = st.file_uploader("Choose a file")
dataframe = pd.read_csv(uploaded_file)

st.write(dataframe.shape)
st.write(dataframe.describe())
st.write(dataframe)


st.line_chart(dataframe.iloc[5:20], x='id', y='age')

st.area_chart(dataframe.iloc[5:20],x='id',y='age')

st.bar_chart(dataframe.iloc[5:20],x='id',y='age')

#plot_id_age = plt.plot([dataframe['age']])
#st.pyplot(plot_id_age)

plotly_fig = px.funnel(dataframe.iloc[5:20], x='city', y='age')
st.plotly_chart(plotly_fig)


st.vega_lite_chart(dataframe, {
    'mark': {'type': 'circle', 'tooltip': True},
    'encoding': {
        'x': {'field': 'age', 'type': 'quantitative'},
        'y': {'field': 'id', 'type': 'quantitative'},
        'size': {'field': 'age', 'type': 'quantitative'},
        'color': {'field': 'id', 'type': 'quantitative'},
    },
})

#altair_fig = alt.Chart(dataframe).mark_bar().encode('age','id','city')
