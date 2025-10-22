import streamlit as st

# Page config
st.set_page_config(page_title="My Cart - QuizBankPro", page_icon="🛒", layout="wide")

# Check if user is logged in
if not st.session_state.get('logged_in', False):
    st.warning("⚠️ Please login to view your cart")
    if st.button("Go to Login"):
        st.switch_page("pages/Login.py")
    st.stop()

# Initialize cart in session state if it doesn't exist
if 'cart_items' not in st.session_state:
    st.session_state.cart_items = [
        {
            "id": 1,
            "type": "Multiple Choice",
            "difficulty": "Medium",
            "question": "Which of the following describes the process of photosynthesis?"
        },
        {
            "id": 2,
            "type": "Short Answer",
            "difficulty": "Hard",
            "question": "Explain Newton's third law of motion and provide an example."
        },
        {
            "id": 3,
            "type": "Short Answer",
            "difficulty": "Medium",
            "question": "State the principle of conservation of energy."
        },
        {
            "id": 4,
            "type": "True/False",
            "difficulty": "Easy",
            "question": "True or False: The capital of France is Berlin."
        },
        {
            "id": 5,
            "type": "Short Answer",
            "difficulty": "Medium",
            "question": "Calculate the area of a circle with a radius of 5 cm. (Use π = 3.14)"
        }
    ]

# Initialize export formats in session state
if 'export_formats' not in st.session_state:
    st.session_state.export_formats = {
        "PDF Document": True,
        "LaTeX Source": True,
        "QTI XML": True,
        "R Markdown": True
    }

# Sidebar
with st.sidebar:
    st.title("📚 QuizBankPro")
    st.markdown("---")
    
    if st.button("📊 Homepage", use_container_width=True):
        st.switch_page("pages/Homepage.py")
    
    if st.button("🔍 Search Questions", use_container_width=True):
        st.info("Search page coming soon!")
    
    if st.button("🛒 My Cart", use_container_width=True, type="primary"):
        st.rerun()
    
    if st.button("📝 Create Quiz", use_container_width=True):
        st.info("Create Quiz page coming soon!")
    
    if st.button("📈 Analyze Results", use_container_width=True):
        st.info("Analyze Results page coming soon!")
    
    st.markdown("---")
    
    if st.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.switch_page("pages/Login.py")

# Main header
col_header1, col_header2, col_header3 = st.columns([2, 4, 2])

with col_header2:
    st.title("My Cart")

with col_header3:
    if st.button("← Back to Search", type="secondary"):
        st.switch_page("pages/Question_Shopping.py")

st.markdown("---")

# Main layout - cart items on left, summary on right
col_main, col_summary = st.columns([2, 1])

# Left column - Cart items
with col_main:
    if len(st.session_state.cart_items) == 0:
        st.info("🛒 Your cart is empty. Add some questions to get started!")
    else:
        for item in st.session_state.cart_items:
            with st.container():
                # Question card
                col_badge, col_type, col_diff = st.columns([1, 2, 2])
                
                with col_type:
                    st.markdown(f"**Type:** {item['type']}")
                
                with col_diff:
                    # Color code difficulty
                    if item['difficulty'] == 'Easy':
                        st.success(f"🟢 {item['difficulty']}")
                    elif item['difficulty'] == 'Medium':
                        st.warning(f"🟡 {item['difficulty']}")
                    else:  # Hard
                        st.error(f"🔴 {item['difficulty']}")
                
                # Question text
                st.markdown(f"### {item['question']}")
                
                # Action buttons
                col_edit, col_remove, col_space = st.columns([1, 1, 4])
                
                with col_edit:
                    if st.button("✏️ Edit", key=f"edit_{item['id']}", use_container_width=True):
                        st.info(f"Edit question {item['id']} - Coming soon!")
                
                with col_remove:
                    if st.button("🗑️ Remove", key=f"remove_{item['id']}", use_container_width=True, type="secondary"):
                        # Remove item from cart
                        st.session_state.cart_items = [i for i in st.session_state.cart_items if i['id'] != item['id']]
                        st.success(f"Question removed from cart!")
                        st.rerun()
                
                st.markdown("---")

# Right column - Order Summary
with col_summary:
    st.subheader("Order Summary")
    
    # Questions selected
    st.metric(
        label="Questions Selected",
        value=len(st.session_state.cart_items)
    )
    
    st.markdown("---")
    
    # Export formats
    st.subheader("Export Formats")
    
    st.session_state.export_formats["PDF Document"] = st.checkbox(
        "📄 PDF Document",
        value=st.session_state.export_formats["PDF Document"],
        key="pdf_check"
    )
    
    st.session_state.export_formats["LaTeX Source"] = st.checkbox(
        "📝 LaTeX Source",
        value=st.session_state.export_formats["LaTeX Source"],
        key="latex_check"
    )
    
    st.session_state.export_formats["QTI XML"] = st.checkbox(
        "🔗 QTI XML",
        value=st.session_state.export_formats["QTI XML"],
        key="qti_check"
    )
    
    st.session_state.export_formats["R Markdown"] = st.checkbox(
        "📊 R Markdown",
        value=st.session_state.export_formats["R Markdown"],
        key="rmd_check"
    )
    
    st.markdown("---")
    
    # Proceed to checkout button
    if st.button("✅ Proceed to Checkout", use_container_width=True, type="primary", disabled=len(st.session_state.cart_items) == 0):
        # Get selected formats
        selected_formats = [fmt for fmt, checked in st.session_state.export_formats.items() if checked]
        
        if not selected_formats:
            st.error("⚠️ Please select at least one export format")
        else:
            st.success(f"✅ Proceeding to checkout with {len(st.session_state.cart_items)} questions")
            st.info(f"Export formats: {', '.join(selected_formats)}")
            # In real app: st.switch_page("pages/Checkout.py")
    
    if len(st.session_state.cart_items) == 0:
        st.caption("Add questions to your cart to proceed")

# Footer
st.markdown("---")
col_footer1, col_footer2, col_footer3 = st.columns(3)

with col_footer1:
    st.caption("Quick Links")

with col_footer2:
    st.caption("Resources")

with col_footer3:
    st.caption("Company")