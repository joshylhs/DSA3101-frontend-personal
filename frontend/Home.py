import streamlit as st

# Page config
st.set_page_config(
    page_title="QuizArena - Home",
    page_icon=":stadium:",
    layout="wide"
)

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Header
st.title("🏟 Welcome to QuizArena")
st.subheader("Build Better Exams, Together!")

st.markdown("---")

# Check if user is logged in
if st.session_state.logged_in:
    # Logged in view
    st.success(f"✅ Welcome back, {st.session_state.get('user_email', 'User')}!")
    
    st.write("### Quick Actions:")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("📚 **Question Bank**")
        st.write("Browse and search questions")
        if st.button("Go to Question Bank", use_container_width=True):
            st.info("Question Bank page coming soon!")
    
    with col2:
        st.info("📝 **Create Exam**")
        st.write("Start building your exam")
        if st.button("Create New Exam", use_container_width=True):
            st.info("Create Exam page coming soon!")
    
    with col3:
        st.info("📊 **Analytics**")
        st.write("View your statistics")
        if st.button("View Analytics", use_container_width=True):
            st.info("Analytics page coming soon!")
    
    st.markdown("---")
    
    # Logout button
    if st.button("🚪 Logout", type="secondary"):
        st.session_state.logged_in = False
        st.session_state.user_email = None
        st.session_state.user_data = None
        st.success("Logged out successfully!")
        st.rerun()

else:
    # Not logged in view
    st.write("### About QuizArena")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**QuizArena** is a collaborative quiz bank platform designed for educators.")
        
        st.write("#### Key Features:")
        st.markdown("✅ **10,000+ Curated Questions** - Access a vast library of quality questions")
        st.markdown("✅ **Collaborative Sharing** - Share and contribute questions with colleagues")
        st.markdown("✅ **Performance Tracking** - Monitor student performance and question effectiveness")
        st.markdown("✅ **Smart Search** - Find questions by topic, difficulty, and more")
        st.markdown("✅ **Multiple Export Formats** - PDF, QTI, R Markdown, and more")
        
        st.markdown("---")
        
        st.info("💬 *'QuizBank saved me 10 hours on exam prep'* - Prof. Chen, NUS")
    
    with col2:
        st.write("#### Get Started")
        st.write("Join thousands of educators using QuizArena to create better exams.")
        
        if st.button("🔐 Login", use_container_width=True, type="primary"):
            st.switch_page("pages/Login.py")
        
        if st.button("📝 Sign Up", use_container_width=True):
            st.switch_page("pages/Signup.py")
        
        st.markdown("---")
        
        st.write("#### Why Choose QuizArena?")
        with st.expander("🚀 Save Time"):
            st.write("No more hunting for questions. Our curated database and AI recommendations help you build exams faster.")
        
        with st.expander("🤝 Collaborate"):
            st.write("Share questions with your department and benefit from peer contributions.")
        
        with st.expander("📈 Improve Quality"):
            st.write("Track question performance and student responses to continuously improve your assessments.")
        
        with st.expander("🔧 Easy Export"):
            st.write("Export to any format you need - Canvas, Moodle, PDF, and more.")

st.markdown("---")

# Footer
col1, col2, col3 = st.columns(3)

with col1:
    st.write("📧 [Contact Support](mailto:support@quizarena.com)")

with col2:
    st.write("📖 [Documentation](#)")

with col3:
    st.write("🔒 [Privacy Policy](#)")