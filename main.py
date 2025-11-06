import streamlit as st

st.title("My First Chai Streamlit App")


st.subheader("Streamlit Demo by Naim")
st.text("CHAI IS THE BEST TEA!")
st.write("Welcome to our first ineractive app!")
arrchai = ["Masala Chai", "Ginger Chai", "Lemon Chai"]
chai = st.selectbox("Fev. Chai:", arrchai)
st.button("Click Me!")

st.write(f"You choose {chai}. Excellient choice!")
st.success("Enjoy your chai!")
