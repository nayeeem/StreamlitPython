import streamlit as st

st.title("My First Chai Streamlit App")


st.subheader("Streamlit Demo by Naim")
st.text("CHAI IS THE BEST TEA!")
st.write("Welcome to our first ineractive app!")

chai = st.selectbox("Fev. Chai:", ["Masala Chai", "Ginger Chai", "Lemon Chai"])
st.button("Click Me!")

st.write(f"You choose {chai}. Excellient choice!")
st.success("Enjoy your chai!")
st.balloons()
st.snow()
st.snow()