import streamlit as st

st.set_page_config(page_title="Instagram Messenger", layout="centered")
st.title("📸 Send Instagram Message")
st.write("⚠️ *Note:* This app simulates sending Instagram messages. Real messaging requires official API access.")

with st.form("instagram_form"):
    instagram_username = st.text_input("@ Recipient Instagram Username", placeholder="e.g. john_doe")
    instagram_message = st.text_area("Instagram Message", placeholder="Type your message here...")
    submitted = st.form_submit_button("Send Instagram Message")

    if submitted:
        if not instagram_username or not instagram_message:
            st.warning("🚫 Please enter both a username and a message.")
        else:
            st.success(f"✅ Message to @{instagram_username} would be sent here (simulation).")
