import streamlit as st

from main import TripCrew

st.set_page_config(page_title="Streamlit App", page_icon="✈️", layout="centered")
st.title("Virtual Travel Agent")

with st.sidebar:
    st.subheader("Travel Agent Tasks")
    st.write("Select the task you'd like the travel agent to perform:")
    origin = st.text_input("From where will you be traveling from?")
    cities = st.text_input("Enter the cities you'd like to visit (comma separated)")
    duration = st.slider("How many days will you be traveling?", 1, 15)
    date_range = st.text_input("Select the month you are interested in traveling")
    interests = st.text_input("What are your interests? (comma separated)")
    
    if st.button("Plan Itinerary"):
        trip_crew = TripCrew(origin, cities, duration, date_range, interests)
        with st.spinner("Planning your trip..."):
            st.session_state.result = trip_crew.plan_trip()
    
if "result" not in st.session_state:
    st.info("Awaiting input...")
else:
    st.write("## Trip Planning Completed")
    st.write(st.session_state.result)