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

# Conversion Factors
conversion_factors = {
    "Length": {
        "Metre": 1,
        "Centimetre": 100,
        "Kilometre": 0.001,
        "Millimetre": 1000
    },
    "Weight": {
        "Kilogram": 1,
        "Gram": 1000,
        "Pound": 2.20462
    }
}

# UI Layout
st.title("Unit Converter")

# Select Measurement Type
measurement_type = st.selectbox("Select Measurement Type", list(conversion_factors.keys()))

# Select Units
unit_options = list(conversion_factors[measurement_type].keys())
from_unit = st.selectbox("From", unit_options)
to_unit = st.selectbox("To", unit_options)

# Input Value
value = st.number_input("Enter Value", min_value=0.0, value=1.0, step=0.1)

# Conversion Logic
converted_value = value * (conversion_factors[measurement_type][to_unit] / conversion_factors[measurement_type][from_unit])

# Display Result
st.write(f"### {value} {from_unit} = {converted_value} {to_unit}")

# Display Formula
st.markdown(f"**Formula:** Multiply the {from_unit} value by {conversion_factors[measurement_type][to_unit]} / {conversion_factors[measurement_type][from_unit]}")
