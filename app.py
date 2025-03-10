import streamlit as st
import re
import string

def check_password_strength(password):
    strength = 0
    criteria = {
        '✅ Length (8+ characters)': len(password) >= 8,
        '✅ Upper & Lower case': bool(re.search(r'[A-Z]', password)) and bool(re.search(r'[a-z]', password)),
        '✅ Numbers': bool(re.search(r'\d', password)),
        '✅ Special Characters': bool(re.search(f'[{re.escape(string.punctuation)}]', password))
    }
    
    strength = sum(criteria.values())
    
    if strength == 4:
        return 'Strong', criteria
    elif strength == 3:
        return 'Medium', criteria
    else:
        return 'Weak', criteria

# Streamlit UI Styling
st.set_page_config(page_title="Password Strength Meter", page_icon="🔒", layout="centered")
st.markdown("""
    <style>
        body {background-color: #f4f4f4;}
        .main {background: white; padding: 30px; border-radius: 15px; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);}
        .stTextInput > div > div > input {border: 2px solid #007bff; border-radius: 10px; padding: 8px;}
        .stProgress > div > div > div {border-radius: 10px;}
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class='main'>
        <h1 style='text-align: center; color: #007bff;'>🔐 Password Strength Meter</h1>
        <p style='text-align: center; font-size: 18px;'>Check how strong your password is!</p>
    </div>
""", unsafe_allow_html=True)

password = st.text_input("Enter your password", type="password", help="Try adding uppercase, numbers, and special characters for a stronger password!")

if password:
    strength, criteria = check_password_strength(password)
    
    color_map = {'Weak': 'red', 'Medium': 'orange', 'Strong': 'green'}
    progress = {'Weak': 33, 'Medium': 66, 'Strong': 100}
    
    st.markdown(f"""
        <h3 style='color: {color_map[strength]}; text-align: center;'>Strength: {strength}</h3>
    """, unsafe_allow_html=True)
    
    st.progress(progress[strength] / 100)
    
    st.markdown("<div class='main'>", unsafe_allow_html=True)
    st.markdown("### 🔍 Strength Criteria:")
    for key, value in criteria.items():
        st.markdown(f"- {key}" if value else f"- ❌ {key[2:]}")
    
    if strength == "Weak":
        st.warning("⚠️ Your password is weak. Consider making it longer and adding numbers/special characters.")
    elif strength == "Medium":
        st.info("ℹ️ Your password is okay, but it can be improved!")
    else:
        st.success("✅ Great! Your password is strong.")
    st.markdown("</div>", unsafe_allow_html=True)
