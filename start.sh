#!/bin/bash

# WAB AI Assistant Launch Script

echo "🐅 Starting WAB AI Assistant..."
echo "================================="

# Stop any existing instances
echo "Checking for existing instances..."
pkill -f "python app.py" 2>/dev/null || true

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "⚠️  Warning: .env file not found!"
    echo "Please copy .env.example to .env and add your OpenAI API key"
    echo "cp .env.example .env"
    exit 1
fi

# Check if API key is set
if ! grep -q "OPENAI_API_KEY=sk-" .env; then
    echo "⚠️  Warning: OpenAI API key not configured!"
    echo "Please edit .env file and add your OpenAI API key"
    exit 1
fi

# Start the application
echo "🚀 Launching WAB AI Assistant..."
echo "Access the application at: http://localhost:5050"
echo "Press Ctrl+C to stop the server"
echo "================================="

python app.py
