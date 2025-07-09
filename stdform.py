import streamlit as st

st.set_page_config(page_title="Student Registration Form", page_icon="🎓")

st.title("🎓 Student Registration Form")
st.markdown("Please fill in the student details below:")

# Start a form
with st.form("student_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    age = st.number_input("Age", min_value=3, max_value=100, value=18)
    gender = st.radio("Gender", ["Male", "Female", "Other"])
    course = st.selectbox("Select course", ["B.Tech", "B.Com", "BCA", "BSC"])
    branch = st.selectbox("Select Branch", [" CSE", "Electric", "Civil", "Other"])
    hobbies = st.multiselect("Select Hobbies", ["Reading", "Sports", "Music", "Coding", "Art", "Traveling"])
    photo = st.file_uploader("Upload a Profile Photo (optional)", type=["jpg", "jpeg", "png"])

    submitted = st.form_submit_button("Submit")

# If the form is submitted
if submitted:
    st.success("✅ Student Registered Successfully!")
    
    st.markdown("---")
    st.header("📄 Submitted Information")

    st.markdown(f"**Name:** {name}")
    st.markdown(f"**Email:** {email}")
    st.markdown(f"**Age:** {age}")
    st.markdown(f"**Gender:** {gender}")
    st.markdown(f"**Grade:** {grade}")
    st.markdown(f"**Hobbies:** {', '.join(hobbies) if hobbies else 'None'}")

    if photo is not None:
        st.markdown("**Uploaded Photo:**")
        st.image(photo, width=150)
