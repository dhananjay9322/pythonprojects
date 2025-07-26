import smtplib, ssl, urllib.parse
from email.mime.text import MIMEText
from twilio.rest import Client as TwilioClient

# Twilio Config (Replace with your credentials)
TWILIO_SID = "YOUR_TWILIO_SID"
TWILIO_AUTH = "YOUR_TWILIO_AUTH_TOKEN"
TWILIO_PHONE = "+15074185310"
CALL_TO = "+91XXXXXXXXXX"
WHATSAPP_FROM = "whatsapp:+14155238886"
WHATSAPP_TO = "whatsapp:+91XXXXXXXXXX"
WHATSAPP_MSG = "Hello! This is an automated WhatsApp message."
CALL_TTS = "Hello! This is an automated call from my Linux project."

# Gmail Config (Replace with your Gmail and app password)
GMAIL_USER = "your_email@gmail.com"
GMAIL_PASS = "your_gmail_app_password"
MAIL_TO = "recipient@example.com"
MAIL_SUBJECT = "Hello from Linux"
MAIL_BODY = "This is a email sent from linux Python script."

def place_call():
    client = TwilioClient(TWILIO_SID, TWILIO_AUTH)
    twiml = f'<Response><Say voice="alice">{CALL_TTS}</Say></Response>'
    url = "https://twimlets.com/echo?Twiml=" + urllib.parse.quote(twiml)
    call = client.calls.create(to=CALL_TO, from_=TWILIO_PHONE, url=url)
    print(f"[CALL] Call placed successfully. SID: {call.sid}")

def send_whatsapp():
    client = TwilioClient(TWILIO_SID, TWILIO_AUTH)
    msg = client.messages.create(from_=WHATSAPP_FROM, to=WHATSAPP_TO, body=WHATSAPP_MSG)
    print(f"[WHATSAPP] WhatsApp message sent. SID: {msg.sid}")

def send_email():
    msg = MIMEText(MAIL_BODY)
    msg["Subject"] = MAIL_SUBJECT
    msg["From"] = GMAIL_USER
    msg["To"] = MAIL_TO
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(GMAIL_USER, GMAIL_PASS)
        server.send_message(msg)
    print("[EMAIL] Email sent successfully.")

if __name__ == "__main__":
    print("=== Starting Integrated Communication Script ===")
    place_call()
    send_whatsapp()
    send_email()
    print("=== All tasks completed successfully! ===")
