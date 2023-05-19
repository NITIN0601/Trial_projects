import streamlit as st

# Create two columns
col1, col2 = st.beta_columns(2)

# Section 1
with col1:
    st.header("Section 1")
    st.write("This is the content of section 1.")

# Section 2
with col2:
    st.header("Section 2")
    st.write("This is the content of section 2.")
