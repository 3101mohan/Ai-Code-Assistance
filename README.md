# ♊ Gemini AI Code Assistant

A beginner-friendly web application built with **Python** and **Streamlit** that uses **Google's Gemini API** to instantly generate code snippets from natural language descriptions.

---

## ✨ Features

* **Natural Language to Code**: Generate Python, JavaScript, SQL, C++, and Bash code based on text prompts.
* **Gemini 2.5 Flash**: Utilizes the highly efficient `gemini-2.5-flash` model for fast, high-quality results.
* **Strict Code Output**: Configured to ensure the model outputs only runnable code enclosed in Markdown blocks, minimizing conversational text.
* **Responsive UI**: Interactive interface built quickly using Streamlit.
* **Secure**: Uses a separate `.env` file to manage the API key securely.

---

## ⚙️ Prerequisites

Before running the application, you will need:

* **Python 3.9+** installed on your system.
* A **Gemini API Key** obtained from [Google AI Studio](https://studio.google.com/).

---

## 🚀 Setup and Installation

### 1. Clone the Repository

```bash
git clone <YOUR_REPO_URL>
cd ai-code-assistant
```

### 2. Create and Activate a Virtual Environment

> Recommended to isolate project dependencies.

```bash
# Create the environment
python -m venv venv

# Activate (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Activate (macOS/Linux)
# source venv/bin/activate
```

### 3. Install Required Libraries

```bash
pip install streamlit python-dotenv google-generativeai
```

### 4. Configure Your API Key

Create a file named `.env` in the root of your project directory (`ai-code-assistant/`) and add:

```bash
GEMINI_API_KEY="AIzaSyA_Paste_Your_Actual_Gemini_API_Key_Here"
```

> **Warning:** Do not commit your `.env` file to GitHub!

---

## ▶️ Running the Application

With the virtual environment active, run:

```bash
streamlit run app.py
```

The application will open in your default browser (usually [http://localhost:8501](http://localhost:8501)).

---

## 🛠️ Troubleshooting: Dependency Conflicts (Protobuf)

If you encounter an error related to **protobuf versions**, try:

```bash
pip install protobuf==4.25.3 --no-deps --force-reinstall
```

This resolves compatibility issues between Google APIs and older Streamlit/TensorFlow versions.

---

## 📂 File Structure

```
ai-code-assistant/
├── venv/                   # Python Virtual Environment
├── .env                    # API Key (SECURE)
├── app.py                  # Main Streamlit application code
└── README.md               # Project documentation

Do you want me to do that?
