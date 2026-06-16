import streamlit as st  


st.title("My First Streamlit App")  
st.header("Section 1")  
st.subheader("Header")  
st.subheader("Subheader")  
st.text("Simple text")  
st.markdown("**Bold** and *italic* text")  

st.write("Automatic data display")  
st.code("print('Hello World')", language='python')  
st.latex(r"\int_{a}^{b} x^2 dx")  


col1, col2 = st.columns(2)

with col1:  
    st.header("Column 1")
    st.write("Content for column 1")

with col2: 
    st.header("Column 2")
    st.write("Content for column 2")


with st.expander("Click to expand"):
    st.write("Expanded content here")


st.sidebar.title("Sidebar")
sidebar_option = st.sidebar.selectbox("Select option", ["A", "B", "C"])

with col1:
    st.write("Some content")