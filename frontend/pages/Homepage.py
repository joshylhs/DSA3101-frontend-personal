import streamlit as st

# Page config
st.set_page_config(page_title="Dashboard - QuizArena", page_icon="📊", layout="wide")

# Check if user is logged in
if not st.session_state.get('logged_in', False):
    st.warning("⚠️ Please login to access the dashboard")
    if st.button("Go to Login"):
        st.switch_page("pages/Login.py")
    st.stop()

# User is logged in
user_email = st.session_state.get('user_email', 'User')
user_data = st.session_state.get('user_data', {})

# Header
st.title("📊 Dashboard")
st.write(f"Welcome back, **{user_data.get('first_name', user_email)}**!")

st.markdown("---")

# Stats row
st.subheader("📈 Your Activity")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Questions Used", value="47", delta="12 this month")

with col2:
    st.metric(label="Exams Created", value="8", delta="2 this month")

with col3:
    st.metric(label="Questions Saved", value="156", delta="23 new")

with col4:
    st.metric(label="Cart Items", value="5", delta=None)

st.markdown("---")

# Main content area
col_left, col_right = st.columns([2, 1])

with col_left:
    st.subheader("🔥 Recent Activity")
    
    st.info("📅 **Last Export:** Oct 3, 2025 - Midterm Exam")
    st.success("✅ **Exam Created:** Sep 28, 2025 - Quiz 2")
    st.warning("⏰ **Reminder:** Review questions for Final Exam")
    
    st.markdown("---")
    
    st.subheader("📚 Quick Actions")
    
    col_action1, col_action2 = st.columns(2)
    
    with col_action1:
        if st.button("🔍 Browse Questions", use_container_width=True, type="primary"):
            st.switch_page("pages/Question_Shopping.py")
        
        if st.button("📝 Create Exam", use_container_width=True):
            st.info("Exam creator coming soon!")
    
    with col_action2:
        if st.button("⬆️ Upload Questions", use_container_width=True):
            st.info("Upload feature coming soon!")
        
        if st.button("🛒 My Cart", use_container_width=True):
            st.switch_page("pages/My_Cart.py")

with col_right:
    st.subheader("💡 AI Recommendations")
    
    st.write("Based on your recent activity:")
    
    with st.expander("📌 Hypothesis Testing Questions"):
        st.write("12 new questions added")
        st.button("View Questions", key="rec1")
    
    with st.expander("📌 Regression Analysis"):
        st.write("8 updated questions")
        st.button("View Questions", key="rec2")
    
    with st.expander("📌 ANOVA"):
        st.write("5 highly-rated questions")
        st.button("View Questions", key="rec3")
    
    st.markdown("---")
    
    st.subheader("🏆 Your Contributions")
    st.metric(label="Questions Shared", value="34")
    st.metric(label="Used by Others", value="156 times")
    st.metric(label="Avg Rating", value="4.7 ⭐")

st.markdown("---")

# Alerts section
st.subheader("🔔 Alerts")

col_alert1, col_alert2 = st.columns(2)

with col_alert1:
    st.warning("⚠️ **12 questions** unused for 1+ year - Consider reviewing")

with col_alert2:
    st.info("📢 **23 new questions** added to Data Structures this week")

st.markdown("---")

# Footer with logout
col_footer1, col_footer2 = st.columns([3, 1])

with col_footer2:
    if st.button("🚪 Logout", use_container_width=True):
        st.session_state.logged_in = False
        st.session_state.user_email = None
        st.session_state.user_data = None
        st.success("Logged out successfully!")
        st.switch_page("Home.py")