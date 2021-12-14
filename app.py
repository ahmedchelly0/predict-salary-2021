
import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page
from explore1_page import show_explore1_page
from explore2_page import show_explore2_page
from explore3_page import show_explore3_page

page = st.sidebar.selectbox("Predict", ("Predict",))

page2 = st.sidebar.selectbox("Explore ", ("Table","Bar Charts", "Spline Chart", "Pie Charts"))

if page == "Predict":
    show_predict_page()

if page2 == "Table":
    show_explore_page()
elif page2 == "Bar Charts":
    show_explore1_page()
elif page2 == "Spline Chart":
    show_explore2_page()
else:
    show_explore3_page()
