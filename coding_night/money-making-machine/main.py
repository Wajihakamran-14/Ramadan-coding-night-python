import streamlit as st
import random
import time
import requests

st.title("Money Making Machine")

def generate_money():
    return random.randint(1, 100)

st.subheader("Instant Cash Generator")
if st.button("Generate Money"):
    st.write("Counting your money...")
    time.sleep(5)
    amount = generate_money()
    st.success(f"You made ${amount}!")


def fetch_side_hustle():
    try:
        response = requests.get("http://127.0.0.1:8000/side.hustle")    