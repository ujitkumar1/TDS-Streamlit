import streamlit as st

n1_input = st.text_input("Enter First Number")
n2_input = st.text_input("Enter Second Number")
n3_input = st.text_input("Enter Third Number")

# Convert input to integers if they are not empty
n1 = int(n1_input) if n1_input else 0
n2 = int(n2_input) if n2_input else 0
n3 = int(n3_input) if n3_input else 0

st.write("The largest number is:", max(n1, n2, n3))
