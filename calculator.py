import streamlit as st

# Set up the title of the app
st.title('Simple Calculator')

# Create input fields for the user to enter numbers
num1 = st.number_input('Enter the first number:', value=0.0)
num2 = st.number_input('Enter the second number:', value=0.0)

# Create a select box for the user to choose an operation
operation = st.selectbox('Choose an operation:', ['Addition', 'Subtraction', 'Multiplication', 'Division'])

# Perform the selected operation
if operation == 'Addition':
    result = num1 + num2
elif operation == 'Subtraction':
    result = num1 - num2
elif operation == 'Multiplication':
    result = num1 * num2
elif operation == 'Division':
    if num2 != 0:
        result = num1 / num2
    else:
        result = 'Error: Division by zero'

# Display the result
st.write(f'The result is: {result}')
