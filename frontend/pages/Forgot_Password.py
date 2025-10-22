import streamlit as st
import time

# Page config
st.set_page_config(page_title="Forgot Password - QuizArena", page_icon="🎓", layout="wide")

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

# Right column - Forgot Password Form
with col2:
    st.title("Forgot Password")
    st.write("Enter your email to retrieve your password")
    
    st.markdown("---")
    
    # Forgot password form
    with st.form("forgot_password_form"):
        email = st.text_input("Email / Username*", placeholder="Enter your email or username")
        
        submit = st.form_submit_button("Retrieve Password", use_container_width=True, type="primary")
        
        if submit:
            if not email:
                st.error("⚠️ Please enter your email or username")
            else:
                # Your password reset logic here
                # In real app: send_password_reset_email(email)
                
                with st.spinner("Sending reset link..."):
                    time.sleep(1.5)
                    
                    st.success(f"✅ Password reset link has been sent to **{email}**")
                    st.info("📧 Please check your email inbox (and spam folder) for the reset link.")
    
    # Back to login link
    st.markdown("---")
    st.write("Remember your password?")
    if st.button("← Back to Login", use_container_width=True):
        st.switch_page("pages/Login.py")