import streamlit as st

# Page config
st.set_page_config(page_title="Search Questions - QuizBankPro", page_icon="🔍", layout="wide")

# Check if user is logged in
if not st.session_state.get('logged_in', False):
    st.warning("⚠️ Please login to search questions")
    if st.button("Go to Login"):
        st.switch_page("pages/Login.py")
    st.stop()

# Initialize cart
if 'cart_items' not in st.session_state:
    st.session_state.cart_items = []

def is_in_cart(question_id):
    """Check if question is already in cart"""
    return any(item['id'] == question_id for item in st.session_state.cart_items)

def add_to_cart(question_id, question_type, difficulty, question_text):
    """Add question to cart"""
    if is_in_cart(question_id):
        return False
    
    st.session_state.cart_items.append({
        "id": question_id,
        "type": question_type,
        "difficulty": difficulty,
        "question": question_text
    })
    return True

# Sidebar
with st.sidebar:
    st.title("📚 QuizBankPro")
    st.markdown("---")
    
    if st.button("📊 Dashboard", use_container_width=True):
        st.switch_page("pages/Homepage.py")
    
    if st.button("🔍 Search Questions", use_container_width=True, type="primary"):
        st.rerun()
    
    cart_count = len(st.session_state.cart_items)
    if st.button(f"🛒 My Cart ({cart_count})", use_container_width=True):
        st.switch_page("pages/My_Cart.py")
    
    if st.button("📝 Create Quiz", use_container_width=True):
        st.info("Create Quiz page coming soon!")
    
    if st.button("📈 Analyze Results", use_container_width=True):
        st.info("Analyze Results page coming soon!")

# Header
st.title("🔍 Search Questions")
st.markdown("---")

# Search bar and filters
col_search, col_button = st.columns([4, 1])

with col_search:
    search_query = st.text_input(
        "Search questions by keyword, topic...",
        placeholder="e.g., photosynthesis, Newton's laws, calculus",
        label_visibility="collapsed"
    )

with col_button:
    search_button = st.button("🔍 Search", use_container_width=True, type="primary")

# Filters
st.subheader("Filters")
col_course, col_concept, col_difficulty, col_type = st.columns(4)

with col_course:
    course = st.selectbox("Course", ["All Courses", "DSA3101", "ST2334", "CS2040"])

with col_concept:
    concept = st.selectbox("Concept", ["All Concepts", "Hypothesis Testing", "Regression", "ANOVA"])

with col_difficulty:
    difficulty = st.selectbox("Difficulty", ["All Levels", "Easy", "Medium", "Hard"])

with col_type:
    question_type = st.selectbox("Type", ["All Types", "Multiple Choice", "Short Answer", "True/False"])

st.markdown("---")

# Sample questions database
sample_questions = [
    {
        "id": 101,
        "type": "Multiple Choice",
        "difficulty": "Medium",
        "question": "Which of the following describes the process of photosynthesis?",
        "course": "Biology 101",
        "concept": "Plant Biology"
    },
    {
        "id": 102,
        "type": "Short Answer",
        "difficulty": "Hard",
        "question": "Explain Newton's third law of motion and provide an example.",
        "course": "Physics 201",
        "concept": "Classical Mechanics"
    },
    {
        "id": 103,
        "type": "Short Answer",
        "difficulty": "Medium",
        "question": "State the principle of conservation of energy.",
        "course": "Physics 201",
        "concept": "Energy"
    },
    {
        "id": 104,
        "type": "True/False",
        "difficulty": "Easy",
        "question": "True or False: The capital of France is Berlin.",
        "course": "Geography 101",
        "concept": "European Geography"
    },
    {
        "id": 105,
        "type": "Multiple Choice",
        "difficulty": "Medium",
        "question": "What is the derivative of x² with respect to x?",
        "course": "Calculus 101",
        "concept": "Differentiation"
    },
    {
        "id": 106,
        "type": "Short Answer",
        "difficulty": "Hard",
        "question": "Explain the difference between correlation and causation.",
        "course": "Statistics 201",
        "concept": "Statistical Analysis"
    },
    {
        "id": 107,
        "type": "Multiple Choice",
        "difficulty": "Easy",
        "question": "What is 2 + 2?",
        "course": "Math 101",
        "concept": "Basic Arithmetic"
    }
]

# Display results
st.subheader(f"📚 Found {len(sample_questions)} questions")

for question in sample_questions:
    with st.container():
        # Question header with tags
        col_tags1, col_tags2, col_tags3 = st.columns([2, 2, 2])
        
        with col_tags1:
            st.caption(f"📖 {question['course']}")
        
        with col_tags2:
            st.caption(f"🏷️ {question['concept']}")
        
        with col_tags3:
            # Difficulty badge
            if question['difficulty'] == 'Easy':
                st.success(f"🟢 {question['difficulty']}")
            elif question['difficulty'] == 'Medium':
                st.warning(f"🟡 {question['difficulty']}")
            else:
                st.error(f"🔴 {question['difficulty']}")
        
        # Question type
        st.markdown(f"**Type:** {question['type']}")
        
        # Question text
        st.markdown(f"### {question['question']}")
        
        # Action buttons
        col_preview, col_details, col_cart, col_space = st.columns([1, 1, 1.5, 3])
        
        with col_preview:
            if st.button("👁️ Preview", key=f"preview_{question['id']}", use_container_width=True):
                st.info(f"Preview for question {question['id']} - Coming soon!")
        
        with col_details:
            if st.button("ℹ️ Details", key=f"details_{question['id']}", use_container_width=True):
                with st.expander("Question Details", expanded=True):
                    st.write(f"**ID:** Q-{question['id']}")
                    st.write(f"**Course:** {question['course']}")
                    st.write(f"**Concept:** {question['concept']}")
                    st.write(f"**Type:** {question['type']}")
                    st.write(f"**Difficulty:** {question['difficulty']}")
                    st.write("**Last Used:** 3 months ago")
                    st.write("**Times Used:** 12")
        
        with col_cart:
            # Check if already in cart
            if is_in_cart(question['id']):
                st.success("✓ In Cart")
            else:
                if st.button("🛒 Add to Cart", key=f"add_{question['id']}", use_container_width=True, type="primary"):
                    success = add_to_cart(
                        question['id'],
                        question['type'],
                        question['difficulty'],
                        question['question']
                    )
                    if success:
                        st.success("✅ Added to cart!")
                        st.rerun()
        
        st.markdown("---")

# Show cart summary at bottom
if len(st.session_state.cart_items) > 0:
    st.info(f"🛒 You have {len(st.session_state.cart_items)} question(s) in your cart")
    if st.button("View Cart", use_container_width=False):
        st.switch_page("pages/My_Cart.py")