♊ Gemini AI Code AssistantA beginner-friendly web application built with Python and Streamlit that uses Google's Gemini API to instantly generate code snippets from natural language descriptions.✨ FeaturesNatural Language to Code: Generates Python, JavaScript, SQL, C++, and Bash code based on text prompts.Gemini 2.5 Flash: Utilizes the highly efficient gemini-2.5-flash model for fast, high-quality results.Strict Code Output: Configured with specific system instructions to ensure the model outputs only runnable code enclosed in a Markdown block, minimizing conversational text.Responsive UI: Interactive interface built quickly using Streamlit.Secure: Uses a separate .env file to manage the API key securely.⚙️ PrerequisitesBefore running the application, you will need:Python 3.9+ installed on your system.A Gemini API Key obtained from Google AI Studio.🚀 Setup and InstallationFollow these steps to get your project running locally.1. Clone the Repositorygit clone <YOUR_REPO_URL>
cd ai-code-assistant
2. Create and Activate a Virtual EnvironmentIt is highly recommended to use a virtual environment to manage dependencies:# Create the environment
python -m venv venv 

# Activate the environment (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Activate the environment (macOS/Linux)
# source venv/bin/activate
3. Install Required LibrariesThis project uses the google-generativeai SDK, which is currently compatible with the necessary Streamlit components.pip install streamlit python-dotenv google-generativeai
4. Configure Your API KeyCreate a file named .env in the root of your project directory (ai-code-assistant/).Add your Gemini API key to this file:GEMINI_API_KEY="AIzaSyA_Paste_Your_Actual_Gemini_API_Key_Here"
Note: Do not commit your .env file to GitHub!▶️ Running the ApplicationWith your virtual environment active, run the Streamlit app:streamlit run app.py
The application will open automatically in your default web browser (usually http://localhost:8501).🛠️ Troubleshooting: Dependency Conflicts (Protobuf)If you have other complex Python libraries installed in your virtual environment (like TensorFlow or older Streamlit versions), you might encounter a dependency conflict regarding the protobuf package.If you see an error related to protobuf versions when running the app, try force-downgrading protobuf to a stable version that satisfies all library requirements:pip install protobuf==4.25.3 --no-deps --force-reinstall
This command often resolves compatibility issues between Google APIs and older Streamlit/TensorFlow versions.File Structureai-code-assistant/
├── venv/                   # Python Virtual Environment
├── .env                    # API Key (SECURE)
├── app.py                  # Main Streamlit application code
└── README.md               # This file
