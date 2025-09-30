import streamlit as st
import os
from dotenv import load_dotenv

# --- IMPORTANT: Using the older 'google-generativeai' SDK that was successfully installed.
import google.generativeai as genai 
# Note: We are removing 'from google.generativeai import types' because it causes the error.
# ------------------------------------------------------------------------------------

# --- 1. CONFIGURATION AND INITIALIZATION ---

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("Error: GEMINI_API_KEY not found. Please ensure it is set in your .env file.")
    st.stop()
    
# Initialize the Gemini Client using the correct pattern for the installed library
try:
    # 1. Configure the API key
    genai.configure(api_key=api_key)
    
    # 2. Initialize the GenerativeModel client
    MODEL_NAME = "gemini-2.5-flash" 
    client = genai.GenerativeModel(model_name=MODEL_NAME)
    
except Exception as e:
    st.error(f"Failed to initialize Gemini Client. Please verify your internet connection and API key validity. Error details: {e}")
    st.stop()


# --- 2. CORE LOGIC: GEMINI API CALL (Using simple dictionary for config) ---

def generate_code(prompt: str, language: str) -> str:
    """
    Calls the Gemini API to generate a code snippet, constrained by a system instruction.
    """
    
    # System Instruction is crucial: It forces the model to act as a strict code generator.
    # This system instruction is bundled into the prompt for stability with the older SDK.
    system_instruction = (
        f"You are an expert AI {language} code assistant. Your task is to generate a complete, working {language} code snippet based on the user's request. "
        "Your response MUST contain ONLY the runnable code, enclosed in a single markdown code block. "
        "DO NOT include any extra explanations, comments, introductory phrases (like 'Here is the code'), or closing remarks."
        f"Ensure the generated code adheres to standard {language} practices and includes all necessary import statements."
    )
    
    try:
        # Combining the system instruction directly into the prompt for stability.
        full_prompt = (
            f"SYSTEM INSTRUCTION: {system_instruction}\n\n"
            f"USER REQUEST: {prompt}"
        )
        
        # --- CRITICAL FIX: Using a simple dictionary for generation_config ---
        # This is the stable way to pass parameters like temperature in older SDKs.
        generation_config = {
            "temperature": 0.1 
        }

        response = client.generate_content(
            contents=[full_prompt],
            generation_config=generation_config
        )
        
        # The model is instructed to return only the markdown code block
        return response.text
        
    except Exception as e:
        # Display API errors gracefully in the app
        return f"An error occurred during API call: {e}"

# --- 3. STREAMLIT USER INTERFACE (UI) ---

def main():
    st.set_page_config(page_title="Gemini AI Code Assistant", layout="wide", initial_sidebar_state="expanded")
    st.title("♊ Gemini AI Code Assistant")
    st.markdown("Instantly generate clean, ready-to-use code snippets from your natural language requests.")
    
    # --- Sidebar for Settings ---
    with st.sidebar:
        st.header("App Settings")
        
        selected_language = st.selectbox(
            "Select Programming Language:",
            ["Python", "JavaScript", "SQL", "C++", "R", "Bash"]
        )
        
        st.markdown("---")
        st.markdown("#### Instructions")
        st.info(
            "1. Describe the code precisely.\n"
            "2. Select the target language.\n"
            "3. Click 'Generate Code' and review the result!"
        )

    # --- Main Input Area ---
    user_prompt = st.text_area(
        f"Describe the {selected_language} code you need:", 
        height=180,
        placeholder=f"e.g., Write a {selected_language} function to connect to a local database and insert a new user record. Ensure error handling is included."
    )
    
    # Button to trigger the generation
    if st.button(f"Generate {selected_language} Code", type="primary"):
        if user_prompt:
            # Use a spinner while waiting for the API response
            with st.spinner(f"Generating optimized {selected_language} code with Gemini..."):
                # Call the core generation function
                code_snippet = generate_code(user_prompt, selected_language)
            
            st.subheader(f"✅ Generated {selected_language} Code")
            # st.code displays the result with syntax highlighting
            st.code(code_snippet, language=selected_language.lower(), line_numbers=True)
            
        else:
            st.error("Please enter a description to generate code.")

# Run the main application
if __name__ == "__main__":
    main()
