import streamlit as st

st.title("Welcome to the Streamlit App!")
st.header("This is a simple introduction to Streamlit. Its :blue[Cool]")
st.subheader("Let's get started!")

st.write("Streamlit is an open-source app framework for Machine Learning and Data Science teams. It allows you to create beautiful web apps for your machine learning projects with minimal effort.")

agree = st.checkbox("I agree to the terms and conditions")

if agree:
    st.write("You have agreed to the terms and conditions. You can now proceed to use the app.")
    st.success("Thank you for agreeing to the terms and conditions!")



import streamlit as st

genre = st.radio(
    "What's your favorite movie genre",
    ["Comedy", "Drama", "Documentary"]
)

if genre == "Comedy":
    st.write("You selected comedy.")
else:
    st.write("You didn't select comedy.")


number1 = st.number_input("Insert a number")
number2 = st.number_input("Insert another number")

result = number1 + number2

if st.button("Calculate"):
    st.success(f"The result of adding {number1} and {number2} is {result}.")
