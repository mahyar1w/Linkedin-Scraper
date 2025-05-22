import streamlit as st
import subprocess
from pathlib import Path



st.title("linkedin scraper")

if 'show_results_button' not in st.session_state:
    st.session_state.show_results_button = False

button_container = st.container()

def handle_change():
    st.session_state.output = st.session_state.user_input

name = st.text_input(
    "What Job do you want to Search for?",
    placeholder="Enter Job Title", 
    key="user_input", 
    on_change=handle_change
)
n = st.number_input(
    "How many Positions?", 
    min_value=0, 
    max_value=None, 
    value=0, 
    step=1, 
    format="%d"
)


col1, col2 = st.columns([1, 5])

with col1:
        if st.button("Search"):
           if n != 0 : 
            st.session_state.show_results_button = True
           else:
            st.session_state.show_results_button = False
            st.error("Error! number of postions cannot be zero!") 

with col2:
        if st.session_state.show_results_button:
            if st.button("Results"):
             subprocess.Popen(["streamlit", "run", (Path(__file__).parent / "place-holder.py")])



