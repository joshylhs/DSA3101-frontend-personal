"""
Helper functions for managing the shopping cart
Add this file as: cart_utils.py
"""

import streamlit as st

def initialize_cart():
    """Initialize cart in session state if it doesn't exist"""
    if 'cart_items' not in st.session_state:
        st.session_state.cart_items = []
    
    if 'export_formats' not in st.session_state:
        st.session_state.export_formats = {
            "PDF Document": True,
            "LaTeX Source": True,
            "QTI XML": True,
            "R Markdown": True
        }

def add_to_cart(question_id, question_type, difficulty, question_text):
    """Add a question to the cart"""
    initialize_cart()
    
    # Check if already in cart
    if any(item['id'] == question_id for item in st.session_state.cart_items):
        return False, "Question already in cart"
    
    # Add to cart
    st.session_state.cart_items.append({
        "id": question_id,
        "type": question_type,
        "difficulty": difficulty,
        "question": question_text
    })
    
    return True, "Question added to cart"

def remove_from_cart(question_id):
    """Remove a question from the cart"""
    st.session_state.cart_items = [
        item for item in st.session_state.cart_items 
        if item['id'] != question_id
    ]

def get_cart_count():
    """Get number of items in cart"""
    initialize_cart()
    return len(st.session_state.cart_items)

def clear_cart():
    """Clear all items from cart"""
    st.session_state.cart_items = []

def is_in_cart(question_id):
    """Check if a question is in the cart"""
    initialize_cart()
    return any(item['id'] == question_id for item in st.session_state.cart_items)

def get_cart_items():
    """Get all cart items"""
    initialize_cart()
    return st.session_state.cart_items

def get_selected_export_formats():
    """Get list of selected export formats"""
    initialize_cart()
    return [fmt for fmt, checked in st.session_state.export_formats.items() if checked]

# Example usage in a search/browse page:
"""
import cart_utils

# When displaying a question
if st.button(f"Add to Cart", key=f"add_{question_id}"):
    success, message = cart_utils.add_to_cart(
        question_id=question_id,
        question_type="Multiple Choice",
        difficulty="Medium",
        question_text="What is the capital of France?"
    )
    
    if success:
        st.success(message)
    else:
        st.warning(message)

# Show cart count in header
cart_count = cart_utils.get_cart_count()
st.write(f"🛒 Cart ({cart_count})")
"""