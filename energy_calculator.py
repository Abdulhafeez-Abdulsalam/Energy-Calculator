# -*- coding: utf-8 -*-
"""Energy Calculator.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zvLOYVO-325XlX_byrgriIgNJ4iTmOsv
"""

import streamlit as st
import pandas as pd

st.title("🔋 Energy Consumption & Cost Estimator")

with st.form("energy_form"):
    appliance = st.text_input("Appliance Name")
    power = st.number_input("Power Rating (Watts)", min_value=1.0)
    hours = st.number_input("Hours Used per Day", min_value=0.0)
    quantity = st.number_input("Quantity", min_value=1)
    rate = st.number_input("Electricity Cost per kWh (₦)", value=72.0)

    submitted = st.form_submit_button("Calculate")

if submitted:
    energy_per_day = (power * hours * quantity) / 1000
    daily_cost = energy_per_day * rate
    monthly_cost = daily_cost * 30
    yearly_cost = daily_cost * 365

    st.success(f"📅 Daily Energy Use: {energy_per_day:.2f} kWh")
    st.write(f"💰 Daily Cost: ₦{daily_cost:.2f}")
    st.write(f"📆 Monthly Cost: ₦{monthly_cost:.2f}")
    st.write(f"📅 Yearly Cost: ₦{yearly_cost:.2f}")

