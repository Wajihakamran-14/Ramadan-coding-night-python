import streamlit as st  # Importing the streamlit library for creating the web app
import random # Importing the random library for generating random characters:
import string # Importing the string library for using string characters:

# Function to generate a Password
def generate_password(length, use_digit, use_special):
    characters = string.ascii_letters # Include all characters (a-z, (A-z))

    if use_digit:
        characters += string.digits # Adds number (1,2,3,4,5,6,7,.....) if selected

    if use_special:
        characters += string.punctuation # Adds special characters (!, @, #, $, %, ^, &, *)

    # Generates a random password of the specified  length using characters define above
    return ''.join(random.choice(characters) for _ in range(length))      

# Use streamlit for UI
st.title("Password Generator")

length = st.slider("Select Password Length", min_value=6, max_value=32, value=15)

use_digit = st.checkbox("Include Digits")

use_special = st.checkbox("Include Special Characters")

if st.button("Generate Password"):
    password = generate_password(length, use_digit, use_special)
    st.write(f"Generated Password: '{password}'")


st.write("--------------------------")
  
st.write("Build with ❤ by Wajiha Kamran")