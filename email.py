import smtplib
import streamlit as st

st.title("Sending Emails with a click - Build with Python ")
st.write("Enter Details Given Below....")
From = "kkharatdhananjay@gmail.com"
Sub = st.text_input("Enter subject:")
To = st.text_input("Enter receiver's email:")
msg =  st.text_input("Enter message:")

text = f"Subject: {Sub}\n\n{msg}"

if st.button("Send Email"):

  with smtplib.SMTP("smtp.gmail.com",587) as server:
    server.starttls()
    server.login(From,password="mkvp qcvt warr jjbg")
    server.sendmail(from_addr=From,to_addrs=To, msg=text)

    print("Email sent successfully")
    st.success("Email sent successfully")