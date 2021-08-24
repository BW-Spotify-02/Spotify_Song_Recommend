import streamlit as st
import pandas as pd
import numpy as np


st.header("Spotify Song Reccommender")
st.write("Directions: Input the name of a song and we will throw a similar song back at you.")

user_input = st.text_input('Enter some text')
st.write(user_input)

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))
