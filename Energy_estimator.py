import streamlit as st
import pandas as pd

st.set_page_config(page_title="Energy Calculator", layout="wide")
st.title("Advanced Energy Consumption & Solar Estimator")

# Pre-defined appliance power ratings (Watts)
appliance_power_map = {
    "TV (LED, 32)": 60,
    "Refrigerator (Medium)": 150,
    "Standing Fan": 75,
    "Ceiling Fan": 50,
    "Laptop": 45,
    "Air Conditioner (1HP)": 900,
    "Light Bulb (LED)": 10
}

# Emission factor (kg CO₂ per kWh)
carbon_factor = 0.92  # Approximation

# Solar panel efficiency assumption
solar_daily_output_per_kw = 4  # kWh/day per kW of solar panel

# Form input
with st.form("energy_form"):
    st.subheader("Step 1: Select or Enter Appliance Details")

    use_picker = st.checkbox("Use Appliance Picker", value=True)

    if use_picker:
        appliance = st.selectbox("Choose Appliance", list(appliance_power_map.keys()))
        power = appliance_power_map[appliance]
    else:
        appliance = st.text_input("Appliance Name")
        power = st.number_input("Power Rating (Watts)", min_value=1.0)

    hours = st.number_input("Hours Used per Day", min_value=0.0)
    quantity = st.number_input("Quantity", min_value=1)
    rate = st.number_input("Electricity Cost per kWh (₦)", value=225.0)

    submitted = st.form_submit_button("Calculate")

if submitted:
    # Energy and cost calculations
    energy_per_day = (power * hours * quantity) / 1000
    daily_cost = energy_per_day * rate
    monthly_cost = daily_cost * 30
    yearly_cost = daily_cost * 365

    # Carbon emissions estimate
    daily_emissions = energy_per_day * carbon_factor

    # Solar estimation
    solar_kw_required = energy_per_day / solar_daily_output_per_kw

    # Financing (e.g., ₦700,000 per kW system cost, paid over 12 months @ 10% interest)
    solar_cost_per_kw = 700000
    total_solar_cost = solar_kw_required * solar_cost_per_kw
    monthly_finance_payment = (total_solar_cost * 1.10) / 12  # Simple interest model

    # Results
    st.success(f"Daily Energy Use: {energy_per_day:.2f} kWh")
    st.write(f"Daily Cost: ₦{daily_cost:.2f}")
    st.write(f"Monthly Cost: ₦{monthly_cost:.2f}")
    st.write(f"Yearly Cost: ₦{yearly_cost:.2f}")

    st.info(f"Estimated CO₂ Emissions per Day: {daily_emissions:.2f} kg")

    st.subheader("Solar Panel Recommendation")
    st.write(f"You need approximately **{solar_kw_required:.2f} kW** of solar panels to meet this daily usage.")
    st.write(f"Estimated Solar System Cost: ₦{total_solar_cost:,.0f}")

    st.subheader("Financing Simulation")
    st.write(f"If financed over 12 months @ 10% interest:")
    st.write(f"Monthly Payment: **₦{monthly_finance_payment:,.0f}**")
