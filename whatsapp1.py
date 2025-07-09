import streamlit as st
import pywhatkit as kit
from datetime import datetime


st.set_page_config(page_title="📲 WhatsApp Automation", layout="centered")
st.title("📱 WhatsApp Message Sender")


st.sidebar.header("🛠️ Choose Action")
action = st.sidebar.selectbox("Select Option", ["Send Instant Message", "Schedule Message"])

phone = st.text_input("📞 Enter Phone Number (with country code)", value="+91", help="E.g., +91XXXXXXXXXX")
message = st.text_area("💬 Enter Your Message")

if action == "Send Instant Message":
    if st.button("📤 Send Now"):
        if phone and message:
            try:
                kit.sendwhatmsg_instantly(phone_no=phone, message=message, wait_time=10, tab_close=True)
                st.success("✅ Message sent successfully.")
            except Exception as e:
                st.error(f"❌ Error: {e}")
        else:
            st.warning("⚠️ Please enter both phone number and message.")

elif action == "Schedule Message":
    st.markdown("🕒 **Schedule Time**")
    col1, col2 = st.columns(2)
    with col1:
        hour = st.number_input("Hour (24h)", min_value=0, max_value=23, step=1, value=datetime.now().hour)
    with col2:
        minute = st.number_input("Minute", min_value=0, max_value=59, step=1, value=(datetime.now().minute + 1) % 60)

    if st.button("📅 Schedule Message"):
        if phone and message:
            try:
                kit.sendwhatmsg(phone_no=phone, message=message, time_hour=int(hour), time_min=int(minute))
                st.success(f"✅ Message scheduled at {hour:02d}:{minute:02d}")
            except Exception as e:
                st.error(f"❌ Error: {e}")
        else:
            st.warning("⚠️ Please enter both phone number and message.")
