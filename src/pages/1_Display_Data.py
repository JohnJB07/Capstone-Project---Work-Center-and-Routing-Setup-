import streamlit as st
import numpy # not used yet
import pandas # not used yet
import json

def main():
    st.header("This Page displays your data in tabular form.")
    home, display, hide = st.columns([2, 2, 2], gap="large", )

    with display:
        if st.button("Display Data"):
            
            pass

    with home:
        if st.button("Home"):
            st.switch_page("Home.py")

    with hide:
        if st.button("Hide page"):
            pass

main()