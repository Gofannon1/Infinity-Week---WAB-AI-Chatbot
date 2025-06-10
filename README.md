# WAB AI Assistant

A bespoke AI assistant for Western Academy of Beijing that answers questions about the school using curated information.

## Quick Start

1. **Clone/Download the project**
   ```bash
   # If you have the project folder, navigate to it
   cd "ai wab infinity week information"
   ```

2. **Set up your API key**
   ```bash
   cp .env.example .env
   # Edit .env and replace 'your_openai_api_key_here' with your actual OpenAI API key
   ```

3. **Run the application**
   ```bash
   # Option 1: Use the launch script (recommended)
   ./start.sh
   
   # Option 2: Manual setup
   pip install -r requirements.txt
   python app.py
   ```

4. **Access the application**
   Open your browser and go to: http://localhost:5050

## Project Structure

```
├── app.py                 # Flask web application
├── wabai.py              # AI logic and OpenAI integration
├── start.sh              # Launch script for easy startup
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── .env                  # Your environment variables (create from .env.example)
├── .gitignore           # Git ignore rules
├── README.md            # This file
├── config/              # Configuration module
│   ├── __init__.py
│   └── settings.py      # Application settings
├── data/                # Knowledge base files
│   └── Information_Wab.txt
├── templates/           # HTML templates
│   └── index.html       # Main web interface
└── static/             # Static assets
    ├── css/
    │   └── style.css    # Styling
    └── js/
        └── main.js      # JavaScript functionality
```

## Features

- **Focused AI**: Only answers questions about WAB using curated information
- **Web Interface**: Simple and clean web interface
- **Secure**: Uses environment variables for API keys
- **Extensible**: Easy to add new features and improve the knowledge base

## Troubleshooting

### Common Issues

1. **OpenAI Version Error**
   ```bash
   # If you get a TypeError with OpenAI client, update the library:
   pip install --upgrade openai==1.85.0
   ```

2. **API Key Issues**
   ```bash
   # Make sure your .env file has a valid OpenAI API key:
   OPENAI_API_KEY=sk-proj-your-actual-key-here
   ```

3. **Port Already in Use**
   ```bash
   # If port 5050 is busy, stop existing processes:
   pkill -f "python app.py"
   ```

4. **Module Import Errors**
   ```bash
   # Clear Python cache and reinstall:
   rm -rf __pycache__ config/__pycache__
   pip install -r requirements.txt
   ```

## Usage

Simply type your question about Western Academy of Beijing in the web interface and get instant answers based on the comprehensive school information database.
