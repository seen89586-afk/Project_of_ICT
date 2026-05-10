import streamlit as st

# PAGE SETTINGS
st.set_page_config(
    page_title="Mechanical Unit Converter",
    page_icon="⚙️",
    layout="centered"
)

# CUSTOM CSS
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .title {
        text-align: center;
        color: #003366;
        font-size: 40px;
        font-weight: bold;
    }
    .subtitle {
        text-align: center;
        color: #555555;
        font-size: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# HEADER
st.markdown('<p class="title">⚙️ Mechanical Unit Converter & Density Checker</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Developed by Muhammad Sameer 25_ME_151</p>', unsafe_allow_html=True)

st.write("---")

# SIDEBAR
st.sidebar.title("Navigation")
option = st.sidebar.radio(
    "Select Tool",
    ["Unit Converter", "Density Checker"]
)

# UNIT CONVERTER
if option == "Unit Converter":

    st.header("🔄 Mechanical Unit Converter")

    category = st.selectbox(
        "Select Conversion Type",
        ["Length", "Pressure", "Temperature"]
    )

    value = st.number_input("Enter Value", value=0.0)

    if category == "Length":

        st.subheader("Length Conversion")

        meters = value
        millimeters = meters * 1000
        inches = meters * 39.3701
        feet = meters * 3.28084

        st.success(f"Millimeters: {millimeters:.2f} mm")
        st.success(f"Inches: {inches:.2f} in")
        st.success(f"Feet: {feet:.2f} ft")

    elif category == "Pressure":

        st.subheader("Pressure Conversion")

        pascal = value
        bar = pascal / 100000
        psi = pascal / 6895
        atm = pascal / 101325

        st.success(f"Bar: {bar:.4f} bar")
        st.success(f"PSI: {psi:.4f} psi")
        st.success(f"Atmosphere: {atm:.4f} atm")

    elif category == "Temperature":

        st.subheader("Temperature Conversion")

        celsius = value
        fahrenheit = (celsius * 9/5) + 32
        kelvin = celsius + 273.15

        st.success(f"Fahrenheit: {fahrenheit:.2f} °F")
        st.success(f"Kelvin: {kelvin:.2f} K")

# DENSITY CHECKER
elif option == "Density Checker":

    st.header("🧱 Material Density Checker")

    materials = {
        "Steel": 7850,
        "Aluminum": 2700,
        "Copper": 8960,
        "Brass": 8500,
        "Titanium": 4500,
        "Cast Iron": 7200
    }

    material = st.selectbox(
        "Select Material",
        list(materials.keys())
    )

    density = materials[material]

    st.metric(
        label=f"Density of {material}",
        value=f"{density} kg/m³"
    )

    st.info("Typical engineering density values.")

# FOOTER
st.write("---")
st.caption("Mechanical Engineering Web App using Streamlit")
