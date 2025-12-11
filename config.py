"""
Configuration file for Google Drive to Gemini connector.
Modify the DRIVE_FOLDER_ID to point to your Google Drive folder.
"""
import os
from dotenv import load_dotenv

load_dotenv()

# Google Drive Configuration
# Get this from the Google Drive folder URL: 
# https://drive.google.com/drive/folders/FOLDER_ID_HERE
DRIVE_FOLDER_ID = os.getenv('DRIVE_FOLDER_ID', '')

# Google Gemini Configuration
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', '')
GEMINI_MODEL = os.getenv('GEMINI_MODEL', 'gemini-flash-latest')  # Options: 'gemini-flash-latest' (fast), 'gemini-pro-latest' (more capable)

# Google Drive API Credentials
# Path to your OAuth2 credentials JSON file
# Download from: https://console.cloud.google.com/apis/credentials
CREDENTIALS_FILE = os.getenv('CREDENTIALS_FILE', 'credentials.json')
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

# Application Configuration
CHUNK_SIZE = 10000  # Characters per chunk for document processing
CHUNK_OVERLAP = 500  # Overlap between chunks
MAX_CONTEXT_LENGTH = 30000  # Maximum context to send to Gemini per query

