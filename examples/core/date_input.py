import streamlit as st
from datetime import datetime
from datetime import date

w1 = st.date_input('Label 1', date(1970, 1, 1))
st.write('Value 1:', w1)

w2 = st.date_input('Label 2', datetime(2019, 7, 6, 21, 15))
st.write('Value 2:', w2)
