
import streamlit as st

st.set_page_config(page_title="Calculator App", page_icon="🧮")

st.title("🧮 Calculator App")
st.write("Simple Calculator deployed on Streamlit")

# Inputs
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

operation = st.radio(
    "Select Operation",
    ("Addition", "Subtraction", "Multiplication", "Division")
)

if st.button("Calculate"):
    if operation == "Addition":
        st.success(f"Result: {num1 + num2}")

    elif operation == "Subtraction":
        st.success(f"Result: {num1 - num2}")

    elif operation == "Multiplication":
        st.success(f"Result: {num1 * num2}")

    elif operation == "Division":
        if num2 == 0:
            st.error("❌ Division by zero not allowed")
        else:
            st.success(f"Result: {num1 / num2}")
            