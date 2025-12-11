# Quick Reference Card

## 🚀 Quick Start (5 Steps)

1. **Get Credentials**
   ```bash
   # Download credentials.json from Google Cloud Console
   # Get API key from https://makersuite.google.com/app/apikey
   ```

2. **Configure**
   ```bash
   # Create .env file:
   DRIVE_FOLDER_ID=your_folder_id
   GEMINI_API_KEY=your_api_key
   ```

3. **Install**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run**
   ```bash
   python app.py
   ```

5. **Use**
   ```
   Open: http://localhost:5000
   ```

## 📋 File Locations

| File | Purpose |
|------|---------|
| `app.py` | Main Flask application |
| `config.py` | Configuration settings |
| `drive_connector.py` | Google Drive API |
| `gemini_connector.py` | Gemini API |
| `rag_processor.py` | Document processing |
| `.env` | Your credentials (create this) |
| `credentials.json` | OAuth credentials (download from Google) |

## 🔑 Required Setup

1. **Google Cloud Console**
   - Enable Google Drive API
   - Create OAuth2 credentials (Desktop app)
   - Download as `credentials.json`

2. **Google AI Studio**
   - Get API key: https://makersuite.google.com/app/apikey

3. **Google Drive**
   - Get folder ID from URL: `drive.google.com/drive/folders/FOLDER_ID`

## 💻 Common Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run application
python app.py

# Run examples
python example_usage.py

# Check status (when running)
curl http://localhost:5000/api/status
```

## 🔄 Create New Instance

```bash
# Copy project
cp -r my_work new_project

# Update .env in new_project
cd new_project
# Edit .env: change DRIVE_FOLDER_ID

# Run
python app.py
```

## 🌐 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Web interface |
| `/api/query` | POST | Query documents |
| `/api/status` | GET | Check status |
| `/api/reload` | POST | Reload documents |

## 📝 API Usage

```bash
# Query
curl -X POST http://localhost:5000/api/query \
  -H "Content-Type: application/json" \
  -d '{"query": "Your question here"}'

# Status
curl http://localhost:5000/api/status
```

## 🐛 Quick Fixes

| Problem | Solution |
|---------|----------|
| "Credentials not found" | Download `credentials.json` from Google Cloud |
| "API key not set" | Set `GEMINI_API_KEY` in `.env` |
| "Folder ID not set" | Set `DRIVE_FOLDER_ID` in `.env` |
| "Permission denied" | Delete `token.json`, re-run to re-authenticate |
| "Module not found" | Run `pip install -r requirements.txt` |

## 📚 Documentation Files

- `README.md` - Full documentation
- `SETUP_GUIDE.md` - Detailed setup instructions
- `TEMPLATE_USAGE.md` - How to create multiple instances
- `QUICK_REFERENCE.md` - This file

## ⚙️ Configuration

Edit `config.py` to change:
- `CHUNK_SIZE` - Document chunk size
- `CHUNK_OVERLAP` - Overlap between chunks
- `MAX_CONTEXT_LENGTH` - Max context for Gemini
- `GEMINI_MODEL` - Gemini model to use

## 🔒 Security

- ❌ Never commit: `.env`, `credentials.json`, `token.json`
- ✅ Keep API keys secret
- ✅ Use read-only Drive access

## 📞 Support Checklist

Before asking for help, check:
- [ ] All dependencies installed
- [ ] `credentials.json` in project root
- [ ] `.env` file created and configured
- [ ] APIs enabled in Google Cloud Console
- [ ] Folder ID is correct
- [ ] Have read access to the folder

---

**Need more help?** See `README.md` or `SETUP_GUIDE.md`

