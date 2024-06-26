import streamlit as st

st.title("Virtual Travel Guide")

# Sidebar for selecting a country
selected_country = st.sidebar.selectbox("Pick a Country", ("India", "Sri Lanka", "Maldives", "Thailand"))

# Display information based on the selected country
if selected_country == "India":
    st.write("Welcome to India! Here are some facts about India...")
elif selected_country == "Sri Lanka":
    st.write("Welcome to Sri Lanka! Here are some facts about Sri Lanka...")
elif selected_country == "Maldives":
    st.write("Welcome to Maldives! Here are some facts about Maldives...")
elif selected_country == "Thailand":
    st.write("Welcome to Thailand! Here are some facts about Thailand...")