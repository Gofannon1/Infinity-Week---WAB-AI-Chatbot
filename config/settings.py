"""
Configuration settings for WAB AI Assistant
"""
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # OpenAI Configuration
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-4o')
    OPENAI_TEMPERATURE = float(os.getenv('OPENAI_TEMPERATURE', '0.3'))
    OPENAI_MAX_TOKENS = int(os.getenv('OPENAI_MAX_TOKENS', '1000'))
    
    # Flask Configuration
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    FLASK_DEBUG = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    FLASK_HOST = os.getenv('FLASK_HOST', '0.0.0.0')
    FLASK_PORT = int(os.getenv('PORT', os.getenv('FLASK_PORT', '5050')))
    
    # Data Configuration
    KNOWLEDGE_BASE_PATH = os.getenv('KNOWLEDGE_BASE_PATH', 'data/Information_Wab.txt')
    
    # Validation
    @classmethod
    def validate(cls):
        if not cls.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY environment variable is required")
        
        if not os.path.exists(cls.KNOWLEDGE_BASE_PATH):
            raise FileNotFoundError(f"Knowledge base file not found: {cls.KNOWLEDGE_BASE_PATH}")
        
        return True
