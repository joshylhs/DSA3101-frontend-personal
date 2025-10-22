import streamlit as st
import time
from datetime import datetime

# Page config
st.set_page_config(page_title="Sign Up - QuizArena", page_icon=":stadium:", layout="wide",)

# Create two columns
col1, col2 = st.columns(2)

# Left column - Branding
with col1:
    st.title("🏟 QuizArena")
    st.header("Build Better Exams, Together!")
    
    st.markdown("---")
    
    st.subheader("Features:")
    st.markdown("✅ 10,000+ curated questions")
    st.markdown("✅ Collaborative question sharing")
    st.markdown("✅ Student performance tracking")
    
    st.markdown("---")
    
    st.info("*'QuizBank saved me 10 hours on exam prep'* - Prof. Chen, NUS")
    st.success("*'Best databank 4ever!'* - blah blah")

# Right column - Signup Form
with col2:
    st.title("Sign Up")
    
    # Social signup buttons
    st.subheader("Other signup options:")
    col_social1, col_social2 = st.columns(2)
    with col_social1:
        if st.button("🔵 Sign up with Google", use_container_width=True):
            st.info("Google signup not implemented yet")
    with col_social2:
        if st.button("🔴 Sign up with Microsoft", use_container_width=True):
            st.info("Microsoft signup not implemented yet")
    
    st.markdown("**or**")
    
    # Signup form
    with st.form("signup_form"):
        # Name fields
        col_first, col_last = st.columns(2)
        with col_first:
            first_name = st.text_input("First Name*", placeholder="First name")
        with col_last:
            last_name = st.text_input("Last Name*", placeholder="Last name")
        
        # Username
        username = st.text_input("Username*", placeholder="Choose a username")
        
        # Email
        email = st.text_input("Email*", placeholder="Enter your email")
        
        # Password fields
        password = st.text_input("Password*", type="password", placeholder="Enter password (min 8 characters)")
        confirm_password = st.text_input("Re-enter Password*", type="password", placeholder="Confirm password")
        
        # Date of birth
        dob = st.date_input(
            "Date of Birth*",
            value=None,
            min_value=datetime(1940, 1, 1),
            max_value=datetime.now()
        )
        
        # Institution
        institution = st.selectbox(
            "Institution*",
            ["Select Institution", "National University of Singapore", "MIT", "Stanford", "Harvard", "Other"]
        )
        
        submit = st.form_submit_button("Sign Up", use_container_width=True, type="primary")
        
        if submit:
            # Validation
            errors = []
            
            if not first_name or not last_name:
                errors.append("⚠️ Please enter your full name")
            if not username:
                errors.append("⚠️ Please choose a username")
            if not email:
                errors.append("⚠️ Please enter your email")
            if not password or not confirm_password:
                errors.append("⚠️ Please enter and confirm your password")
            elif password != confirm_password:
                errors.append("⚠️ Passwords don't match")
            elif len(password) < 8:
                errors.append("⚠️ Password must be at least 8 characters")
            if not dob:
                errors.append("⚠️ Please enter your date of birth")
            if institution == "Select Institution":
                errors.append("⚠️ Please select your institution")
            
            if errors:
                for error in errors:
                    st.error(error)
            else:
                # Your signup logic here (save to database, etc.)
                with st.spinner("Creating your account..."):
                    time.sleep(1.5)
                    
                    # Simulate successful signup
                    # In real app: user_id = create_user(first_name, last_name, username, email, password, dob, institution)
                    
                    st.success("✅ Account created successfully!")
                    
                    # Store info in session state for login page
                    st.session_state.signup_success = True
                    st.session_state.signup_email = email
                    st.session_state.signup_name = f"{first_name} {last_name}"
                    
                    time.sleep(1)
                    
                    # Navigate to login page
                    st.switch_page("pages/Login.py")
    
    # Login link
    st.markdown("---")
    st.write("Already have an account?")
    if st.button("Login", use_container_width=True):
        st.switch_page("pages/Login.py")