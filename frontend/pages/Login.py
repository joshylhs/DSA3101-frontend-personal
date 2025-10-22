import streamlit as st
import time

# Page config
st.set_page_config(page_title="Login - QuizArena", page_icon=":stadium:", layout="wide")

# Check if just signed up
if st.session_state.get('signup_success', False):
    st.success(f"✅ Account created successfully! Welcome {st.session_state.get('signup_name', '')}!")
    st.info(f"Please login with: {st.session_state.get('signup_email', '')}")
    st.session_state.signup_success = False

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

# Right column - Login Form
with col2:
    st.title("Login")
    
    # Social login buttons
    st.subheader("Other login options:")
    col_social1, col_social2 = st.columns(2)
    with col_social1:
        if st.button("🔵 Login with Google", use_container_width=True):
            st.info("Google login not implemented yet")
    with col_social2:
        if st.button("🔴 Login with Microsoft", use_container_width=True):
            st.info("Microsoft login not implemented yet")
    
    st.markdown("**or**")
    
    # Login form
    with st.form("login_form"):
        email = st.text_input("Email / Username", placeholder="Enter your email or username")
        password = st.text_input("Password", type="password", placeholder="Enter your password")
        
        col_remember, col_forgot = st.columns([1, 1])
        with col_remember:
            remember = st.checkbox("Remember me")
        with col_forgot:
            if st.form_submit_button("Forgot Password?"):
                st.switch_page("pages/Forgot_Password.py")
        
        submit = st.form_submit_button("LOGIN", use_container_width=True, type="primary")
        
        if submit:
            if not email or not password:
                st.error("⚠️ Please fill in all fields")
            else:
                # Your authentication logic here
                with st.spinner("Logging in..."):
                    time.sleep(1)
                    
                    # Demo: Check credentials (replace with real authentication)
                    if email and password:  # Replace with actual check
                        st.session_state.logged_in = True
                        st.session_state.user_email = email
                        st.success("✅ Login successful! Redirecting...")
                        time.sleep(1)
                        st.switch_page("pages/Homepage.py")  
                    else:
                        st.error("❌ Invalid credentials")
    
    # Sign up link
    st.markdown("---")
    st.write("Don't have an account?")
    if st.button("Sign Up!", use_container_width=True):
        st.switch_page("pages/Signup.py")