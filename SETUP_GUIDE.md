# Detailed Setup Guide

This guide will walk you through setting up the Google Drive to Gemini connector step by step.

## Part 1: Google Cloud Setup

### 1.1 Create a Google Cloud Project

1. Go to https://console.cloud.google.com/
2. Click on the project dropdown at the top
3. Click "New Project"
4. Enter a project name (e.g., "Drive-Gemini-Connector")
5. Click "Create"

### 1.2 Enable Google Drive API

1. In your Google Cloud project, go to "APIs & Services" → "Library"
2. Search for "Google Drive API"
3. Click on it and click "Enable"

### 1.3 Configure OAuth Consent Screen (REQUIRED FIRST)

**⚠️ IMPORTANT:** You MUST configure the OAuth consent screen BEFORE creating the OAuth client ID. If you see a warning about configuring the consent screen, follow these steps:

1. Go to "APIs & Services" → "OAuth consent screen"
   - Or directly: https://console.cloud.google.com/apis/credentials/consent
2. Select **User Type**: Choose "External" (unless you have Google Workspace)
3. Click "Create"
4. **Step 1 - App Information:**
   - App name: "Drive Gemini Connector"
   - User support email: Your email
   - Developer contact: Your email
   - Click "Save and Continue"
5. **Step 2 - Scopes:**
   - Click "Add or Remove Scopes"
   - Search for: `drive.readonly`
   - Check: `https://www.googleapis.com/auth/drive.readonly`
   - Click "Update" then "Save and Continue"
6. **Step 3 - Test Users:**
   - Click "Add Users"
   - Add your email address
   - Click "Save and Continue"
7. **Step 4 - Summary:**
   - Review and click "Back to Dashboard"

**📖 For detailed step-by-step instructions, see `OAUTH_SETUP_GUIDE.md`**

### 1.4 Create OAuth2 Credentials

Now you can create the OAuth client ID:

1. Go to "APIs & Services" → "Credentials"
2. Click "Create Credentials" → "OAuth client ID"
3. **Application type**: Select "Desktop app"
4. **Name**: "Drive Connector Desktop" (or any name)
5. Click "Create"
6. Click "Download JSON" in the popup
7. Rename the downloaded file to `credentials.json`
8. Place it in the project root directory (same folder as `app.py`)

## Part 2: Google AI Studio Setup

### 2.1 Get Gemini API Key

1. Go to https://makersuite.google.com/app/apikey
2. Sign in with your Google account
3. Click "Create API Key"
4. Select your Google Cloud project (or create a new one)
5. Copy the API key (you'll need it later)

## Part 3: Get Google Drive Folder ID

### 3.1 Find Your Folder ID

1. Open Google Drive (https://drive.google.com)
2. Navigate to the folder you want to connect
3. Click on the folder to open it
4. Look at the URL in your browser
5. The URL will look like: `https://drive.google.com/drive/folders/1a2b3c4d5e6f7g8h9i0j`
6. Copy the part after `/folders/` (e.g., `1a2b3c4d5e6f7g8h9i0j`)

**Note**: Make sure the folder is shared with the Google account you're using for authentication, or it's in your own Drive.

## Part 4: Install and Configure

### 4.1 Install Python Dependencies

Open terminal/command prompt in the project directory:

```bash
pip install -r requirements.txt
```

If you encounter issues, try:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4.2 Create Environment File

Create a file named `.env` in the project root:

**Windows (PowerShell):**
```powershell
@"
DRIVE_FOLDER_ID=your_folder_id_here
GEMINI_API_KEY=your_gemini_api_key_here
CREDENTIALS_FILE=credentials.json
"@ | Out-File -FilePath .env -Encoding utf8
```

**Linux/Mac:**
```bash
cat > .env << EOF
DRIVE_FOLDER_ID=your_folder_id_here
GEMINI_API_KEY=your_gemini_api_key_here
CREDENTIALS_FILE=credentials.json
EOF
```

Then edit `.env` and replace:
- `your_folder_id_here` with your actual folder ID
- `your_gemini_api_key_here` with your actual Gemini API key

### 4.3 Verify File Structure

Your project should now have:
```
my_work/
├── app.py
├── config.py
├── drive_connector.py
├── gemini_connector.py
├── rag_processor.py
├── requirements.txt
├── README.md
├── credentials.json      ← Your OAuth credentials
└── .env                  ← Your configuration
```

## Part 5: Run the Application

### 5.1 First Run

```bash
python app.py
```

**First time authentication:**
1. A browser window will open automatically
2. Sign in with your Google account
3. Grant permissions to access Google Drive
4. The browser will show "The authentication flow has completed"
5. Close the browser and return to the terminal

The application will then:
- Connect to your Google Drive folder
- Load all documents
- Start the web server

### 5.2 Access the Web Interface

Open your browser and go to: `http://localhost:5000`

You should see:
- The folder ID you're connected to
- Number of documents loaded
- A query form

### 5.3 Test with a Query

Try asking:
- "What documents are in this folder?"
- "Summarize the main topics"
- "What are the key points from all documents?"

## Part 6: Creating Multiple Instances

### Method 1: Copy the Project

1. Copy the entire project folder
2. Rename it (e.g., `my_work_project2`)
3. Update the `.env` file with a new `DRIVE_FOLDER_ID`
4. Run `python app.py` in the new folder

### Method 2: Use Different Ports

You can run multiple instances on different ports by modifying `app.py`:

```python
# At the bottom of app.py, change:
app.run(debug=True, host='0.0.0.0', port=5000)  # Instance 1
app.run(debug=True, host='0.0.0.0', port=5001)  # Instance 2
```

Then access:
- Instance 1: http://localhost:5000
- Instance 2: http://localhost:5001

## Troubleshooting

### Issue: "ModuleNotFoundError"

**Solution:**
```bash
pip install -r requirements.txt
```

### Issue: "Credentials file not found"

**Solution:**
- Ensure `credentials.json` is in the project root
- Check the filename is exactly `credentials.json` (case-sensitive)

### Issue: "GEMINI_API_KEY not set"

**Solution:**
- Check your `.env` file exists
- Verify the API key is correct in `.env`
- Or set it directly in `config.py`

### Issue: "Permission denied" or "Access denied"

**Solution:**
- Delete `token.json` and re-run to re-authenticate
- Ensure you granted all requested permissions
- Check the folder is accessible with your Google account

### Issue: "No documents found"

**Solution:**
- Verify the folder ID is correct
- Check you have read access to the folder
- Ensure the folder contains supported file types

### Issue: Browser doesn't open for authentication

**Solution:**
- Manually go to the URL shown in the terminal
- Or copy the authentication URL from the terminal output

## Next Steps

Once everything is working:

1. **Customize the RAG system**: Modify `rag_processor.py` to improve document retrieval
2. **Add more file types**: Extend `drive_connector.py` to support additional formats
3. **Deploy to cloud**: Consider deploying to Google Cloud Run for always-on access
4. **Enhance the UI**: Customize the web interface in `app.py`

## Support

If you encounter issues:
1. Check all credentials are correct
2. Verify APIs are enabled in Google Cloud Console
3. Check the terminal output for detailed error messages
4. Review the main README.md for additional troubleshooting

