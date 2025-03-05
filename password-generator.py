import streamlit as st  # Import Streamlit for creating the web-based UI
import random  # Import random for generating random choices
import string  # Import string to use predefined character sets

# Function to generate a random password
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters  # Includes uppercase and lowercase letters

    if use_digits:
        characters += string.digits  # Adds numbers (0-9) if selected

    if use_special:
        # Exclude brackets, slashes, and pipes from special characters
        special_chars = "".join(c for c in string.punctuation if c not in "()[]{}\\/|,")
        characters += special_chars  # Adds special characters except excluded ones

    # Generate a password by randomly selecting characters based on the length provided
    return "".join(random.choice(characters) for _ in range(length))

# Function to check password strength
def check_password_strength(password):
    length = len(password)
    has_digits = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation and c not in "()[]{}\\/|," for c in password)

    if length >= 10 and has_digits and has_special:
        return f"Strong 💪"
    elif length >= 8 and (has_digits or has_special):
        return "Moderate 😐"
    else:
        return "Weak ❌"  # Password is too short or does not contain both numbers and special characters

# Streamlit UI setup
st.title("Simple Password Generator")  # Display the app title on the web page

# User input: password length (slider to select length between 6 and 32 characters)
length = st.slider("Select password length:", min_value=6, max_value=12, value=12)

# Checkbox options for including numbers and special characters in the password
use_digits = st.checkbox("Include numbers")  # Checkbox for numbers (0-9)
use_special = st.checkbox("Include special characters")  # Checkbox for special characters (!@#$%^&*)

# Button to generate password
if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)  # Generate password
    strength = check_password_strength(password)  # Check password strength
    
    # Display the generated password and its strength
    st.write(f"Generated Password: `{password}`")
    st.write(f"Password Strength: **{strength}**")

    
    
    
    
    
    
    