import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

from langchain_helper import generate_country_summary

st.title("Virtual Travel Guide")

# Sidebar for selecting a country
selected_country = st.sidebar.selectbox("Select Destination", ("India", "Sri Lanka", "Maldives", "Thailand"))

# Display information based on the selected country
if selected_country == "India":
    st.write("Welcome to India! Here are some facts about India...")
elif selected_country == "Sri Lanka":
    st.write("Welcome to Sri Lanka! Here are some facts about Sri Lanka...")
elif selected_country == "Maldives":
    st.write("Welcome to Maldives! Here are some facts about Maldives...")
elif selected_country == "Thailand":
    st.write("Welcome to Thailand! Here are some facts about Thailand...")
    
    
if selected_country:
    # st.header(selected_country)
    response = generate_country_summary(selected_country)
    st.header(selected_country)
    st.write(response)
    
    