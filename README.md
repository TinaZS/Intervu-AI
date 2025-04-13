# Intervu-AI

An AI-powered Product Management mock interview assistant

## 🚀 Features

- Asks realistic PM interview questions
- Provides follow-up questions based on your response
- Gives detailed feedback to help you improve

## 🛠️ Setup

1. **Create a virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use: .\venv\Scripts\activate
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` file** in the root directory and add:

   ```env
   AZURE_CHATOPENAI_ENDPOINT=your-endpoint
   AZURE_CHATOPENAI_DEPLOYMENT=your-deployment-name
   CHATOPENAI_API_VERSION=your-api-version
   AZURE_CHATOPENAI_API_KEY=your-api-key
   ```
