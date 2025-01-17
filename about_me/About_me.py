import streamlit as st

st.set_page_config(
    page_title="About Me",
    page_icon="",
)

st.sidebar.success("There's more to me??")

st.title("Hi! I'm Chris")
st.image("about_me/images/FullSizeRender.jpg")
st.caption("I'm on the left, the one on the right is my brother.")
st.subheader("Age: 15")
st.subheader("Living in: Saratoga, CA")
st.subheader("Hobbies: Playing video games, scrolling on Wikipedia")
st.subheader("Status: Tired")
if st.checkbox("Favorite Game"):
    st.write("Splatoon 3")
    st.image("about_me/images/download.jpg")
st.checkbox("Favorite color")