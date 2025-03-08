import streamlit as st

def convert_units(value, unit_from, unit_to):

    conversions = {
        "meters_kilometers": 0.001, # 1 meter = 0.001 kilometer
        "kilometers_meters": 1000, # 1 kilometer = 1000 meter
        "grams_kilograms": 0.001, # 1 gram = 0.001 kilogram
        "kilograms_grams": 1000  # 1 kilogram = gram
    }

    key = f"{unit_from}_{unit_to}"

    if key in conversions:
        conversion = conversions[key]
        return value * conversion
    else:
        return "Conversion not supported"

# Streamlit UI code outside the function
st.title("Simple Unit Convertor")

value = st.number_input("Enter the value:", min_value=1.0, step=1.0)

unit_from = st.selectbox(
     "Convert from:",["meters","kilometers", "grams", "kilograms"]
     )
    
unit_to = st.selectbox(
     "Convert to:", ["meters", "kilometers", "grams", "kilograms"] 
     )
    
if st.button("Convert"):
        result = convert_units(value, unit_from, unit_to)
        st.write(f"Converted value: {result}")
