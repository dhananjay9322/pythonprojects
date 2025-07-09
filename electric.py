import streamlit as st

st.set_page_config(page_title="Electricity Consumption Predictor", page_icon="⚡")

st.title("⚡ Monthly Electricity Consumption Predictor")
st.markdown("Estimate your monthly electricity usage based on your appliance usage.")

num_appliances = st.number_input("Number of different appliances you use:", min_value=1, max_value=20, value=1, step=1)

appliance_data = []
total_daily_kwh = 0

for i in range(num_appliances):
    st.subheader(f"Appliance {i+1}")
    name = st.text_input(f"Name of Appliance {i+1}", key=f"name_{i}")
    power_watts = st.number_input(f"Power Rating (Watts) for {name}", min_value=1.0, value=100.0, key=f"power_{i}")
    usage_hours = st.number_input(f"Daily Usage (Hours) for {name}", min_value=0.0, value=1.0, key=f"hours_{i}")
    quantity = st.number_input(f"Quantity of {name}", min_value=1, value=1, key=f"qty_{i}")

    daily_kwh = (power_watts * usage_hours * quantity) / 1000
    total_daily_kwh += daily_kwh

    appliance_data.append({
        "name": name,
        "power_watts": power_watts,
        "hours": usage_hours,
        "quantity": quantity,
        "daily_kwh": daily_kwh
    })

cost_per_kwh = st.number_input("Enter cost per unit (kWh) of electricity (optional)", min_value=0.0, value=0.0, step=0.01)


if st.button("Predict Monthly Consumption"):
    total_monthly_kwh = total_daily_kwh * 30
    st.success(f"🔋 Total Daily Consumption: **{total_daily_kwh:.2f} kWh**")
    st.success(f"📆 Total Monthly Consumption (30 days): **{total_monthly_kwh:.2f} kWh**")

    if cost_per_kwh > 0:
        estimated_cost = total_monthly_kwh * cost_per_kwh
        st.info(f"💸 Estimated Monthly Electricity Bill: **₹{estimated_cost:.2f}**")

    st.markdown("### 📊 Appliance-wise Breakdown:")
    for item in appliance_data:
        st.markdown(f"- **{item['name']}**: {item['daily_kwh']:.2f} kWh/day "
                    f"({item['quantity']}x, {item['hours']} hr/day, {item['power_watts']} W each)")
