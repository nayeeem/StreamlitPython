import streamlit as st

st.title("Chai Maker App")
masala = False
if st.button("Make Chai"):
    masala = st.checkbox("Masala")
    

if masala:
    st.success("Masala chai ready.")
elif (masala == False):
    st.success("Chai Ready")
        





