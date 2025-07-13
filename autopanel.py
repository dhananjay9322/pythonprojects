import streamlit as st
import subprocess
import time
import schedule

def send_email():
    st.success("📧 Email sent (simulated).")

def run_script():
    st.info("⏳ Running script...")
    result = subprocess.run("echo Script Executed", capture_output=True, text=True, shell=True)

    st.success(f"✅ Script Output: {result.stdout.strip()}")

def show_logs():
    st.subheader("📜 System Logs (simulated)")
    log_data = "2025-07-13 14:00: Service restarted\n2025-07-13 14:10: Task completed"
    st.code(log_data, language='bash')

def restart_service():
    st.warning("🔁 Restarting service...")
    time.sleep(1)
    st.success("✅ Service restarted!")

def schedule_task():
    def task():
        print("Scheduled Task Executed.")
    schedule.every(1).minutes.do(task)
    st.success("🕒 Task scheduled every 1 minute.")

st.title("⚙️ Automation Control Panel")

st.markdown("Welcome to your automation dashboard. Choose an action:")

if st.button("📧 Send Email"):
    send_email()

if st.button("🚀 Run Script"):
    run_script()

if st.button("📜 View Logs"):
    show_logs()

if st.button("🔁 Restart Service"):
    restart_service()

if st.button("⏰ Schedule Task"):
    schedule_task()
