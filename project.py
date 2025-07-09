"""
All‑in‑One Streamlit Control Panel
=================================
• 🔌 Electricity Consumption Predictor  (local Streamlit logic)
• 🐳 Docker Remote Controller           (SSH via Paramiko)
• 🤖 Gradio App launcher / embed        (runs separately on port 7860)
• 💻 Linux Command Runner               (SSH and shell commands)

Run:  streamlit run main_app.py
Make sure the Gradio app is running separately, e.g.:
       python gradio_script.py  # or run the notebook cell
"""

import streamlit as st
import paramiko
import subprocess

# ----------------------------
# Shared SSH Command Function
# ----------------------------
def run_ssh_command(host, username, password, command):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host, username=username, password=password)
        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.read().decode()
        error = stderr.read().decode()
        ssh.close()
        return output if output else error
    except Exception as e:
        return f"❌ SSH Error: {e}"

# ----------------------------
# Page Setup & Sidebar
# ----------------------------
st.set_page_config(page_title="All-in-One Control Panel", layout="wide")
st.sidebar.title("🧭 Navigation")
section = st.sidebar.radio("Select a feature:", [
    "🔌 Electricity Calculator",
    "🐳 Docker Remote Controller",
    "💻 Linux Command Runner",
    "🤖 Gradio App Launcher"
])

# ----------------------------
# Section: Electricity Project
# ----------------------------
if section == "🔌 Electricity Calculator":
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
        st.success(f"🔋 Daily Consumption: {total_daily_kwh:.2f} kWh")
        st.success(f"📆 Monthly Consumption (30 days): {total_monthly_kwh:.2f} kWh")

        if cost_per_kwh > 0:
            estimated_cost = total_monthly_kwh * cost_per_kwh
            st.info(f"💸 Estimated Monthly Electricity Bill: ₹{estimated_cost:.2f}")

        st.markdown("### 📊 Appliance-wise Breakdown:")
        for item in appliance_data:
            st.markdown(f"- {item['name']}: {item['daily_kwh']:.2f} kWh/day "
                        f"({item['quantity']}x, {item['hours']} hr/day, {item['power_watts']} W each)")

# ----------------------------
# Section: Docker Remote Controller
# ----------------------------
elif section == "🐳 Docker Remote Controller":
    st.title("🐳 Docker Remote Controller via SSH")

    host = st.text_input("🔗 Server IP (e.g., 192.168.1.100)")
    username = st.text_input("👤 SSH Username")
    password = st.text_input("🔑 SSH Password", type="password")

    docker_options = [
        "Create New Container",
        "Show running containers (docker ps)",
        "Show Docker images (docker images)",
        "Pull an image",
        "Stop a container",
        "Remove a container",
        "Show container logs"
    ]
    selected = st.selectbox("Select Docker Action", docker_options)

    if host and username and password:
        if selected == "Create New Container":
            name = st.text_input("Enter the name of Container")
            image = st.text_input("Enter the name of image you want to create in")
            if st.button("Create"):
                st.code(run_ssh_command(host, username, password, f"docker run -dit --name={name} {image}"))
        if selected == "Show running containers (docker ps)":
            if st.button("Run"):
                st.code(run_ssh_command(host, username, password, "docker ps"))

        elif selected == "Show Docker images (docker images)":
            if st.button("Run"):
                st.code(run_ssh_command(host, username, password, "docker images"))

        elif selected == "Pull an image":
            image_name = st.text_input("Image name to pull (e.g. ubuntu)")
            if st.button("Pull"):
                st.code(run_ssh_command(host, username, password, f"docker pull {image_name}"))

        elif selected == "Stop a container":
            container = st.text_input("Container ID/Name to stop:")
            if st.button("Stop"):
                st.code(run_ssh_command(host, username, password, f"docker stop {container}"))

        elif selected == "Remove a container":
            container = st.text_input("Container ID/Name to remove:")
            if st.button("Remove"):
                st.code(run_ssh_command(host, username, password, f"docker rm {container}"))

        elif selected == "Show container logs":
            container = st.text_input("Container ID/Name for logs:")
            if st.button("Show Logs"):
                st.code(run_ssh_command(host, username, password, f"docker logs {container}"))
    else:
        st.info("Please enter SSH connection details to proceed.")

# ----------------------------
# Section: Linux Command Runner
# ----------------------------
elif section == "💻 Linux Command Runner":
    st.title("💻 Remote Linux Command Runner")
    host = st.text_input("🔗 Server IP (e.g., 192.168.1.100)", key="cmd_host")
    username = st.text_input("👤 SSH Username", key="cmd_user")
    password = st.text_input("🔑 SSH Password", type="password", key="cmd_pass")
    command = st.text_area("📥 Enter your Linux command to run:", height=100)

    if st.button("Execute Command"):
        if all([host, username, password, command]):
            result = run_ssh_command(host, username, password, command)
            st.code(result)
        else:
            st.warning("Please fill in all fields before running the command.")

# ----------------------------
# Section: Gradio App Launcher
# ----------------------------
elif section == "🤖 Gradio App Launcher":
    st.title("🤖 Gradio Project Launcher")
    st.markdown("Click below to open your Gradio project in a new tab:")
    gradio_url = "http://localhost:7860"
    st.markdown(f"[🚀 Open Gradio App]({gradio_url})", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🔍 Optional Preview:")
    st.markdown(f'<iframe src="{gradio_url}" width="100%" height="600px"></iframe>', unsafe_allow_html=True)