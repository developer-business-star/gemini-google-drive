# Google Drive to Gemini Connector

A custom application that securely links Google Gemini to specific Google Drive folders or documents, enabling Gemini to access and utilize the full contents of your documents for complex querying, analysis, and generation tasks.

## 🎯 Features

- **Direct Google Drive Integration**: Connect to any Google Drive folder and access all documents within
- **Multi-Format Support**: Supports Google Docs, PDFs, Word documents, text files, and more
- **RAG (Retrieval-Augmented Generation)**: Intelligent document chunking and retrieval for optimal context
- **Flexible Querying**: Ask complex questions, perform analysis, and generate content based on your documents
- **Reusable Template**: Easily duplicate and connect to different Drive folders for multiple knowledge bases
- **Web Interface**: User-friendly web UI for querying your documents
- **REST API**: Programmatic access for integration with other applications

## Prerequisites

1. **Python 3.8+** installed on your system
2. **Google Cloud Project** with APIs enabled:
   - Google Drive API
   - Google Gemini API (via Google AI Studio)
3. **OAuth2 Credentials** from Google Cloud Console
4. **Google Gemini API Key** from [Google AI Studio](https://makersuite.google.com/app/apikey)

## Quick Start Guide

### Step 1: Set Up Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the following APIs:
   - **Google Drive API**: [Enable here](https://console.cloud.google.com/apis/library/drive.googleapis.com)
4. **Configure OAuth Consent Screen** (REQUIRED FIRST):
   - Go to [OAuth Consent Screen](https://console.cloud.google.com/apis/credentials/consent)
   - Select "External" user type
   - Fill in app information
   - Add scope: `https://www.googleapis.com/auth/drive.readonly`
   - Add yourself as a test user
   - ** Detailed instructions: See `OAUTH_SETUP_GUIDE.md`**
5. Create OAuth2 credentials:
   - Go to [Credentials](https://console.cloud.google.com/apis/credentials)
   - Click "Create Credentials" → "OAuth client ID"
   - Choose "Desktop app" as application type
   - Download the JSON file and save it as `credentials.json` in the project root

### Step 2: Get Google Gemini API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the API key (you'll need it in Step 4)

### Step 3: Get Your Google Drive Folder ID

1. Open Google Drive and navigate to the folder you want to connect
2. Click on the folder to open it
3. Look at the URL: `https://drive.google.com/drive/folders/FOLDER_ID_HERE`
4. Copy the `FOLDER_ID_HERE` part

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Configure the Application

Create a `.env` file in the project root:

```env
DRIVE_FOLDER_ID=your_folder_id_here
GEMINI_API_KEY=your_gemini_api_key_here
CREDENTIALS_FILE=credentials.json
```

Or edit `config.py` directly:

```python
DRIVE_FOLDER_ID = 'your_folder_id_here'
GEMINI_API_KEY = 'your_gemini_api_key_here'
```

### Step 6: Run the Application

```bash
python app.py
```

The application will:
1. Authenticate with Google Drive (first time will open browser for OAuth)
2. Load all documents from your specified folder
3. Start a web server at `http://localhost:5000`

### Step 7: Use the Application

1. Open your browser and go to `http://localhost:5000`
2. Enter your question or prompt in the text area
3. Click "Ask Gemini" to get answers based on your documents

## Usage Examples

### Web Interface

Simply visit `http://localhost:5000` and use the web form to query your documents.

### API Usage

#### Query Documents

```bash
curl -X POST http://localhost:5000/api/query \
  -H "Content-Type: application/json" \
  -d '{"query": "What are the main topics discussed in these documents?"}'
```

#### Check Status

```bash
curl http://localhost:5000/api/status
```

#### Reload Documents

```bash
curl -X POST http://localhost:5000/api/reload \
  -H "Content-Type: application/json" \
  -d '{"folder_id": "new_folder_id_here"}'
```

### Python Code Example

```python
from drive_connector import DriveConnector
from gemini_connector import GeminiConnector
from rag_processor import RAGProcessor

# Initialize connectors
drive = DriveConnector('your_folder_id')
documents = drive.get_all_documents()

rag = RAGProcessor()
rag.load_documents(documents)

gemini = GeminiConnector()

# Query with context
query = "Summarize the key points from all documents"
context = rag.retrieve_relevant_chunks(query)
response = gemini.query_with_context(query, context)
print(response)
```

## Creating Multiple Instances (Reusable Template)

To create multiple knowledge bases for different projects:

### Method 1: Multiple Configuration Files

1. Copy the entire project folder
2. Update the `.env` file or `config.py` with a new `DRIVE_FOLDER_ID`
3. Run the application

### Method 2: Environment-Based Configuration

Create separate `.env` files for each project:

```bash
# Project 1
cp .env .env.project1
# Edit .env.project1 with folder ID for project 1

# Project 2
cp .env .env.project2
# Edit .env.project2 with folder ID for project 2
```

Then run with specific environment:
```bash
# Linux/Mac
export $(cat .env.project1 | xargs) && python app.py

# Windows PowerShell
Get-Content .env.project1 | ForEach-Object { $line = $_ -split '='; [Environment]::SetEnvironmentVariable($line[0], $line[1]) }
python app.py
```

### Method 3: Command-Line Folder ID

Modify `app.py` to accept folder ID as command-line argument:

```python
import sys
if len(sys.argv) > 1:
    folder_id = sys.argv[1]
    initialize_connectors(folder_id)
```

Then run:
```bash
python app.py your_folder_id_here
```

## Project Structure

```
.
├── app.py                 # Main Flask application
├── config.py              # Configuration settings
├── drive_connector.py     # Google Drive API integration
├── gemini_connector.py    # Google Gemini API integration
├── rag_processor.py       # RAG document processing
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── credentials.json       # OAuth2 credentials (not in repo)
├── token.json            # OAuth token (auto-generated)
└── .env                  # Environment variables (not in repo)
```

## Configuration Options

Edit `config.py` to customize:

- `CHUNK_SIZE`: Size of document chunks (default: 10000 characters)
- `CHUNK_OVERLAP`: Overlap between chunks (default: 500 characters)
- `MAX_CONTEXT_LENGTH`: Maximum context sent to Gemini (default: 30000 characters)
- `GEMINI_MODEL`: Gemini model to use (default: 'gemini-pro')

## Supported File Types

- Google Docs (`.gdoc`)
- Google Sheets (`.gsheet`)
- Google Slides (`.gslides`)
- PDF files (`.pdf`)
- Microsoft Word (`.docx`, `.doc`)
- Plain text files (`.txt`)
- CSV files (`.csv`)

## Security Notes

1. **Never commit** `credentials.json`, `token.json`, or `.env` to version control
2. Keep your Gemini API key secure
3. The OAuth token grants read-only access to your Drive files
4. Consider using service account credentials for production deployments

## Troubleshooting

### "Credentials file not found"
- Ensure `credentials.json` is in the project root
- Download OAuth2 credentials from Google Cloud Console

### "GEMINI_API_KEY not set"
- Set the API key in `.env` file or `config.py`
- Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

### "DRIVE_FOLDER_ID not set"
- Set the folder ID in `.env` file or `config.py`
- Get folder ID from the Google Drive folder URL

### "Permission denied" errors
- Ensure the OAuth credentials have the correct scopes
- Re-authenticate by deleting `token.json` and running again

### Documents not loading
- Check that the folder ID is correct
- Verify you have read access to the folder
- Check file types are supported

## Advanced Usage

### Custom RAG Retrieval

Modify `rag_processor.py` to use embeddings for better retrieval:

```python
# Example: Use sentence transformers for embeddings
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')
# Generate embeddings for chunks
# Use cosine similarity for retrieval
```

### Integration with Google AI Studio

This application can be integrated with Google AI Studio by:
1. Deploying the Flask app to a cloud service (Google Cloud Run, etc.)
2. Using the API endpoints from Google AI Studio's custom functions
3. Or using the application as a standalone service

## Contributing

This is a template project. Feel free to customize and extend it for your needs.

## License

This project is provided as-is for the client's use case.

## Support

For issues or questions:
1. Check the Troubleshooting section
2. Review Google Drive API and Gemini API documentation
3. Verify all credentials and configurations are correct

---

**Built with for seamless Google Drive to Gemini integration**

