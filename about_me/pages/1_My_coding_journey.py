import streamlit as st
import pandas as pd
import numpy as np

st.write("My coding journey")
x = st.slider("Slide for my age", 0, 15)
st.write("My Age: ", str(x))
if x == 0:
    st.write("I was born")
if x==5:
    st.write('I watched one robotics documentary by Nova, the PBS show. At that time, I though that coding was just "if/then" statements')
elif x ==7:
    st.write("Mastered Code.org")
    st.image("about_me/images/download.png")
elif x == 9:
    st.write("Worked on LEGO Mindstorm, canceled due to COVID")
elif x == 10:
    st.write("Read Python Crash Course by Eric Matthens")
    st.image("about_me/images/71pys4B4OVL._AC_UF1000,1000_QL80_.jpg")
elif x == 14:
    st.write("Created GrEG, a CV model that can detect if an image came from 6 countries, with my team at AI Camp")
    st.image("about_me/images/Quality_Quesadillas.png")
    st.write("Passed USACO Bronze")
elif x == 15:
    st.write("AI Camp Internship")
    st.image("about_me/images/12b467_a4ceef0f338c41c7885cb083ea36a00f~mv2_d_1742_1743_s_2.png")
    