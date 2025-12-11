# Template Usage Guide

This document explains how to use this project as a reusable template for multiple Google Drive folders.

## Understanding the Template Structure

This project is designed to be easily duplicated and reconfigured for different Google Drive folders. Each copy becomes an independent knowledge base connector.

## Quick Template Duplication

### Step 1: Copy the Project

```bash
# Copy the entire project folder
cp -r my_work my_work_project2
# Or on Windows:
xcopy my_work my_work_project2 /E /I
```

### Step 2: Update Configuration

Edit the new project's `.env` file:

```env
DRIVE_FOLDER_ID=new_folder_id_here
GEMINI_API_KEY=your_gemini_api_key_here  # Can be the same key
CREDENTIALS_FILE=credentials.json         # Can use same credentials
```

### Step 3: Run the New Instance

```bash
cd my_work_project2
python app.py
```

**That's it!** You now have a separate connector for a different folder.

## Template Customization Options

### Option 1: Environment Variables (Recommended)

Keep one codebase, use different `.env` files:

```bash
# Project 1
.env.project1:
DRIVE_FOLDER_ID=folder_id_1

# Project 2
.env.project2:
DRIVE_FOLDER_ID=folder_id_2
```

Load specific environment:
```bash
# Linux/Mac
export $(cat .env.project1 | xargs) && python app.py

# Windows PowerShell
$env:DRIVE_FOLDER_ID="folder_id_1"
python app.py
```

### Option 2: Command-Line Arguments

Modify `app.py` to accept folder ID:

```python
import sys

if __name__ == '__main__':
    folder_id = sys.argv[1] if len(sys.argv) > 1 else DRIVE_FOLDER_ID
    initialize_connectors(folder_id)
    app.run(debug=True, host='0.0.0.0', port=5000)
```

Usage:
```bash
python app.py folder_id_1
python app.py folder_id_2  # Different folder
```

### Option 3: Configuration File Per Project

Create `config_project1.py`, `config_project2.py`:

```python
# config_project1.py
DRIVE_FOLDER_ID = 'folder_id_1'
# ... other settings

# config_project2.py
DRIVE_FOLDER_ID = 'folder_id_2'
# ... other settings
```

Then import the specific config:
```python
# In app.py, change:
from config_project1 import *  # or config_project2
```

## Multi-Instance Deployment

### Running Multiple Instances Simultaneously

1. **Different Ports**: Modify port in each instance
2. **Different Folders**: Each instance connects to a different folder
3. **Same Credentials**: Can reuse `credentials.json` and API key

Example setup:

```
Instance 1 (Port 5000):
- Folder: Marketing Documents
- URL: http://localhost:5000

Instance 2 (Port 5001):
- Folder: Technical Documentation
- URL: http://localhost:5001

Instance 3 (Port 5002):
- Folder: Client Notes
- URL: http://localhost:5002
```

### Production Deployment

For production, deploy each instance separately:

1. **Google Cloud Run**: Deploy each as separate service
2. **Docker**: Create separate containers
3. **Virtual Machines**: Run on different VMs or ports

## Template Best Practices

### 1. Naming Convention

Name your project copies clearly:
```
drive-gemini-marketing/
drive-gemini-technical/
drive-gemini-clients/
```

### 2. Shared Resources

You can share:
- ✅ `credentials.json` (same Google account)
- ✅ `GEMINI_API_KEY` (same API key)
- ❌ `DRIVE_FOLDER_ID` (must be different)
- ❌ `token.json` (auto-generated, can be shared)

### 3. Version Control

If using Git:
- Keep one main template repository
- Create separate branches or repos for each project
- Or use one repo with multiple config files

### 4. Documentation

For each instance, document:
- Which folder it connects to
- What documents are included
- Any custom configurations

## Example: Creating 3 Knowledge Bases

### Knowledge Base 1: Marketing Materials

```bash
# 1. Copy template
cp -r my_work marketing_kb

# 2. Configure
cd marketing_kb
echo "DRIVE_FOLDER_ID=marketing_folder_id" > .env
echo "GEMINI_API_KEY=your_key" >> .env

# 3. Run
python app.py
# Access at http://localhost:5000
```

### Knowledge Base 2: Technical Docs

```bash
# 1. Copy template
cp -r my_work technical_kb

# 2. Configure
cd technical_kb
echo "DRIVE_FOLDER_ID=technical_folder_id" > .env
echo "GEMINI_API_KEY=your_key" >> .env

# 3. Modify port in app.py (change port=5000 to port=5001)
# 4. Run
python app.py
# Access at http://localhost:5001
```

### Knowledge Base 3: Client Notes

```bash
# 1. Copy template
cp -r my_work clients_kb

# 2. Configure
cd clients_kb
echo "DRIVE_FOLDER_ID=clients_folder_id" > .env
echo "GEMINI_API_KEY=your_key" >> .env

# 3. Modify port in app.py (change port=5000 to port=5002)
# 4. Run
python app.py
# Access at http://localhost:5002
```

## Advanced: Dynamic Folder Selection

Create a web interface to select folders:

```python
# Add to app.py
@app.route('/select-folder', methods=['GET', 'POST'])
def select_folder():
    if request.method == 'POST':
        folder_id = request.form.get('folder_id')
        initialize_connectors(folder_id)
        return redirect('/')
    return render_template_string('''
        <form method="post">
            <input name="folder_id" placeholder="Folder ID">
            <button>Connect</button>
        </form>
    ''')
```

## Template Checklist

When creating a new instance:

- [ ] Copy project folder
- [ ] Update `.env` with new `DRIVE_FOLDER_ID`
- [ ] Verify `GEMINI_API_KEY` is set
- [ ] Ensure `credentials.json` is present
- [ ] Test authentication (first run)
- [ ] Verify documents load correctly
- [ ] Test a sample query
- [ ] Document which folder this instance connects to
- [ ] (Optional) Change port if running multiple instances

## Troubleshooting Template Issues

### Issue: "Folder ID not found"

- Verify the folder ID is correct
- Check the folder is accessible with your Google account
- Ensure the folder exists and is not deleted

### Issue: "Same folder in multiple instances"

- Each instance should have a unique `DRIVE_FOLDER_ID`
- Check your `.env` files are different

### Issue: "Port already in use"

- Change the port in `app.py` for the new instance
- Or stop the other instance first

---

**Remember**: Each template copy is independent. You can have as many instances as you need, each connecting to different Google Drive folders!

