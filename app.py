import streamlit as st

def find_largest_number(a, b, c):
    largest = max(a, b, c)
    return largest

# Streamlit app layout
st.title("Find the Largest Number")
st.write("Enter three numbers and find the largest among them.")
a = st.number_input("Enter the first number:", step=1)
b = st.number_input("Enter the second number:", step=1)
c = st.number_input("Enter the third number:", step=1)

if st.button("Find Largest"):
    largest_number = find_largest_number(a, b, c)
    st.write(f"The largest number is: {largest_number}")
