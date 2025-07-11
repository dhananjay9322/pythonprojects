import streamlit as st
import tweepy
import os

st.set_page_config(page_title="Tweet Poster", layout="centered")

st.title("🐦 Post to Twitter")

st.sidebar.header("🔐 Twitter API Credentials")
twitter_api_key = st.sidebar.text_input("API Key", type="password")
twitter_api_secret = st.sidebar.text_input("API Secret", type="password")
twitter_access_token = st.sidebar.text_input("Access Token", type="password")
twitter_access_secret = st.sidebar.text_input("Access Token Secret", type="password")

tweet_content = st.text_area("📝 Enter your tweet", max_chars=280, height=100)

if st.button("📤 Post Tweet"):
    if not all([twitter_api_key, twitter_api_secret, twitter_access_token, twitter_access_secret]):
        st.error("Please fill in all API credentials.")
    elif not tweet_content.strip():
        st.warning("Tweet content cannot be empty.")
    else:
        try:
            auth = tweepy.OAuthHandler(twitter_api_key, twitter_api_secret)
            auth.set_access_token(twitter_access_token, twitter_access_secret)
            api = tweepy.API(auth)

            api.verify_credentials()
            api.update_status(tweet_content)
            st.success("✅ Tweet posted successfully!")

        except tweepy.errors.TweepyException as e:
            st.error(f"❌ Twitter error: {str(e)}")
        except Exception as e:
            st.error(f"⚠️ Unexpected error: {str(e)}")
