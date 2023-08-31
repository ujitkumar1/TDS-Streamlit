import streamlit as st

st.set_page_config(page_title="Largest Number Finder", page_icon="🔍")

st.title("Find the Largest Number")
st.write("Enter three numbers below to find the largest among them.")

n1_input = st.number_input("First Number", value=0)
n2_input = st.number_input("Second Number", value=0)
n3_input = st.number_input("Third Number", value=0)

n1 = int(n1_input)
n2 = int(n2_input)
n3 = int(n3_input)
largest_number = max(n1, n2, n3)

st.write("The largest number is:", f"**{largest_number}**")

st.markdown("---")
st.write("Created by Ujit Kumar - 21f3000786")
