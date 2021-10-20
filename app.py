import streamlit as st

st.title("Temperature Controller")

step = 0.5

if "temperature" not in st.session_state:
    st.session_state["temperature"] = 25.0

raise_temperature = st.button("Raise temperature")
if raise_temperature:
    st.session_state["temperature"] += step
lower_temperature = st.button("Lower temperature")
if lower_temperature:
    st.session_state["temperature"] -= step
st.write("The temperature will be set to ",
         st.session_state["temperature"],
         "degrees.")

