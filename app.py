import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import os
import subprocess
import sys

# Install required packages
required_packages = [
    "streamlit",
    "streamlit-extras",
    # "fontawesome-free"  # Removed package
]

if 'packages_installed' not in st.session_state:
    for package in required_packages:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        except subprocess.CalledProcessError as e:
            st.error(f"Failed to install package {package}. Error: {e}")
    st.session_state['packages_installed'] = True

# Streamlit Page Configuration
st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")

# Conversion Data
conversion_factors = {
    "Length": {
        "Metre": 1,
        "Kilometre": 0.001,
        "Centimetre": 100,
        "Millimetre": 1000,
        "Mile": 0.000621371,
        "Yard": 1.09361,
        "Foot": 3.28084,
        "Inch": 39.3701
    },
    "Weight": {
        "Kilogram": 1,
        "Gram": 1000,
        "Milligram": 1000000,
        "Pound": 2.20462,
        "Ounce": 35.274
    },
    "Temperature": {
        "Celsius": 1,
        "Fahrenheit": 33.8,
        "Kelvin": 274.15
    }
}

# UI Elements
st.title("Unit Converter")
st.markdown("Convert between different units easily.")

# Category Selection
category = st.selectbox("Select Category", list(conversion_factors.keys()))

# Unit Selection
units = list(conversion_factors[category].keys())
unit_from = st.selectbox("From", units)
unit_to = st.selectbox("To", units)

# Input Value
value = st.number_input("Enter Value", min_value=0.0, format="%.2f")

# Conversion Logic
def convert(value, unit_from, unit_to, category):
    if category == "Temperature":
        if unit_from == "Celsius" and unit_to == "Fahrenheit":
            return (value * 9/5) + 32
        elif unit_from == "Fahrenheit" and unit_to == "Celsius":
            return (value - 32) * 5/9
        elif unit_from == "Celsius" and unit_to == "Kelvin":
            return value + 273.15
        elif unit_from == "Kelvin" and unit_to == "Celsius":
            return value - 273.15
        elif unit_from == "Fahrenheit" and unit_to == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif unit_from == "Kelvin" and unit_to == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
    else:
        return value * (conversion_factors[category][unit_to] / conversion_factors[category][unit_from])

# Perform Conversion
if st.button("Convert"):
    result = convert(value, unit_from, unit_to, category)
    st.success(f"{value} {unit_from} = {result:.2f} {unit_to}")