import streamlit as st

st.title("linkedin scraper")

if 'show_second_button' not in st.session_state:
    st.session_state.show_second_button = False

button_container = st.container()

name = st.text_input("What Job do you want to Search for?", placeholder="Enter Job Title")

col1, col2 = st.columns([1, 7.5])

with col1:
        if st.button("Search"):
            st.session_state.show_second_button = True

with col2:
        if st.session_state.show_second_button:
            if st.button("Results"):
                st.success("results")



