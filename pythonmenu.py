import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from twilio.rest import Client
import tweepy
import requests


def send_email(sender_email, password, smtp_server, smtp_port, recipient, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, recipient, msg.as_string())
        server.quit()

        return True, "✅ Email sent successfully!"
    except Exception as e:
        return False, f"❌ Failed to send email: {str(e)}"

def send_sms(account_sid, auth_token, from_number, to_number, message):
    try:
        client = Client(account_sid, auth_token)
        msg = client.messages.create(body=message, from_=from_number, to=to_number)
        return True, f"✅ SMS sent! SID: {msg.sid}"
    except Exception as e:
        return False, f"❌ Failed to send SMS: {str(e)}"

def make_call(account_sid, auth_token, from_number, to_number, message):
    try:
        client = Client(account_sid, auth_token)
        call = client.calls.create(
            twiml=f'<Response><Say>{message}</Say></Response>',
            from_=from_number,
            to=to_number
        )
        return True, f"✅ Call placed! SID: {call.sid}"
    except Exception as e:
        return False, f"❌ Failed to place call: {str(e)}"

def send_whatsapp(account_sid, auth_token, from_number, to_number, message):
    try:
        client = Client(account_sid, auth_token)
        msg = client.messages.create(
            body=message,
            from_='whatsapp:' + from_number,
            to='whatsapp:' + to_number
        )
        return True, f"✅ WhatsApp message sent! SID: {msg.sid}"
    except Exception as e:
        return False, f"❌ Failed to send WhatsApp message: {str(e)}"

def post_tweet(api_key, api_secret, access_token, access_secret, tweet_text):
    try:
        auth = tweepy.OAuthHandler(api_key, api_secret)
        auth.set_access_token(access_token, access_secret)
        api = tweepy.API(auth)
        api.verify_credentials()
        api.update_status(tweet_text)
        return True, "✅ Tweet posted successfully!"
    except Exception as e:
        return False, f"❌ Failed to post tweet: {str(e)}"

def post_linkedin(access_token, user_urn, content, visibility="PUBLIC"):
    try:
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }

        data = {
            "author": user_urn,
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {
                        "text": content
                    },
                    "shareMediaCategory": "NONE"
                }
            },
            "visibility": {
                "com.linkedin.ugc.MemberNetworkVisibility": visibility
            }
        }

        response = requests.post("https://api.linkedin.com/v2/ugcPosts", headers=headers, json=data)
        if response.status_code == 201:
            return True, "✅ LinkedIn post published!"
        else:
            return False, f"❌ LinkedIn post failed: {response.text}"
    except Exception as e:
        return False, f"❌ Error posting on LinkedIn: {str(e)}"

st.set_page_config(page_title="Multi-Platform Messenger", layout="wide")
st.title("📬 Multi-Platform Messenger")

with st.sidebar:
    st.header("🔐 Credentials")

    with st.expander("Twilio (SMS, WhatsApp, Call)"):
        twilio_account_sid = st.text_input("Twilio Account SID")
        twilio_auth_token = st.text_input("Twilio Auth Token", type="password")
        twilio_phone_number = st.text_input("Twilio Phone Number")

    with st.expander("Email Settings"):
        email_address = st.text_input("Your Email Address")
        email_password = st.text_input("Email Password", type="password")
        smtp_server = st.text_input("SMTP Server", value="smtp.gmail.com")
        smtp_port = st.number_input("SMTP Port", value=587)

    with st.expander("Twitter API"):
        twitter_api_key = st.text_input("Twitter API Key")
        twitter_api_secret = st.text_input("Twitter API Secret", type="password")
        twitter_access_token = st.text_input("Twitter Access Token")
        twitter_access_secret = st.text_input("Twitter Access Secret", type="password")

    with st.expander("LinkedIn API"):
        linkedin_access_token = st.text_input("LinkedIn Access Token", type="password")
        linkedin_user_urn = st.text_input("LinkedIn User URN (e.g. urn:li:person:XXXX)")

tabs = st.tabs(["WhatsApp", "Instagram", "Email", "SMS", "Phone Call", "LinkedIn", "Twitter"])

with tabs[0]:
    st.subheader("📱 Send WhatsApp Message")
    with st.form("whatsapp_form"):
        number = st.text_input("Recipient Number (with country code)")
        message = st.text_area("Message")
        send_btn = st.form_submit_button("Send WhatsApp")

    if send_btn:
        with st.spinner("Sending WhatsApp message..."):
            ok, msg = send_whatsapp(twilio_account_sid, twilio_auth_token, twilio_phone_number, number, message)
            st.success(msg) if ok else st.error(msg)

with tabs[1]:
    st.subheader("📸 Instagram Message")
    st.info("Instagram messaging is not available via public API. Use Facebook Graph API or third-party services.")

with tabs[2]:
    st.subheader("📧 Send Email")
    with st.form("email_form"):
        recipient = st.text_input("Recipient Email")
        subject = st.text_input("Subject")
        body = st.text_area("Email Body")
        email_btn = st.form_submit_button("Send Email")

    if email_btn:
        with st.spinner("Sending email..."):
            ok, msg = send_email(email_address, email_password, smtp_server, smtp_port, recipient, subject, body)
            st.success(msg) if ok else st.error(msg)

with tabs[3]:
    st.subheader("📲 Send SMS")
    with st.form("sms_form"):
        number = st.text_input("Recipient Number")
        message = st.text_area("Message")
        sms_btn = st.form_submit_button("Send SMS")

    if sms_btn:
        with st.spinner("Sending SMS..."):
            ok, msg = send_sms(twilio_account_sid, twilio_auth_token, twilio_phone_number, number, message)
            st.success(msg) if ok else st.error(msg)

with tabs[4]:
    st.subheader("📞 Make Phone Call")
    with st.form("call_form"):
        number = st.text_input("Recipient Number")
        message = st.text_area("Message to Speak")
        call_btn = st.form_submit_button("Make Call")

    if call_btn:
        with st.spinner("Placing call..."):
            ok, msg = make_call(twilio_account_sid, twilio_auth_token, twilio_phone_number, number, message)
            st.success(msg) if ok else st.error(msg)

with tabs[5]:
    st.subheader("🔗 Post on LinkedIn")
    with st.form("linkedin_form"):
        post = st.text_area("Post Content")
        visibility = st.selectbox("Visibility", ["PUBLIC", "CONNECTIONS"])
        post_btn = st.form_submit_button("Post to LinkedIn")

    if post_btn:
        with st.spinner("Posting to LinkedIn..."):
            ok, msg = post_linkedin(linkedin_access_token, linkedin_user_urn, post, visibility)
            st.success(msg) if ok else st.error(msg)

with tabs[6]:
    st.subheader("🐦 Post on Twitter")
    with st.form("twitter_form"):
        tweet = st.text_area("Tweet Content", max_chars=280)
        tweet_btn = st.form_submit_button("Tweet")

    if tweet_btn:
        with st.spinner("Posting Tweet..."):
            ok, msg = post_tweet(twitter_api_key, twitter_api_secret, twitter_access_token, twitter_access_secret, tweet)
            st.success(msg) if ok else st.error(msg)

st.markdown("---")
st.info("Note: Some features require API access or paid services such as Twilio.")
