# Troubleshooting: No Documents Found

## Issue: "Found 0 files in folder"

If you see "Found 0 files in folder" when running the app, here's how to fix it:

## Possible Causes

### 1. Folder is Empty
- The Google Drive folder you're connecting to has no files
- **Solution**: Add some files to the folder

### 2. Wrong Folder ID
- The folder ID in your `.env` or `config.py` is incorrect
- **Solution**: Verify the folder ID from Google Drive URL

### 3. Permission Issues
- The OAuth token doesn't have access to the folder
- **Solution**: Re-authenticate or check folder permissions

### 4. Folder Not Accessible
- The folder might be in a different Google account
- **Solution**: Make sure you're authenticated with the account that owns the folder

## How to Fix

### Step 1: Verify Folder ID

1. Open Google Drive
2. Navigate to your folder
3. Open the folder (double-click)
4. Check the URL: `https://drive.google.com/drive/folders/FOLDER_ID`
5. Compare with your `config.py` or `.env` file

### Step 2: Check Folder Contents

1. Make sure the folder has files in it
2. Supported file types:
   - Google Docs (.gdoc)
   - PDFs (.pdf)
   - Word documents (.docx, .doc)
   - Text files (.txt)
   - CSV files (.csv)

### Step 3: Re-authenticate

1. Delete `token.json` file:
   ```cmd
   del token.json
   ```

2. Run the app again:
   ```cmd
   py app.py
   ```

3. When browser opens, make sure you're signed in with the account that owns the folder

### Step 4: Check Folder Permissions

1. In Google Drive, right-click the folder
2. Click "Share"
3. Make sure your account has at least "Viewer" access
4. If it's your own folder, you should have full access

## Test with a Sample Folder

1. Create a new folder in Google Drive
2. Upload a test file (PDF, Word doc, or text file)
3. Get the folder ID
4. Update your `.env` file:
   ```env
   DRIVE_FOLDER_ID=your_new_folder_id_here
   ```
5. Run the app again

## Verify Folder ID in Code

Check your `config.py`:
```python
DRIVE_FOLDER_ID = '18KkoJlKWFgMAafsJRTBvh34YQzEGEvuw'
```

Make sure this matches your actual folder ID.

## Debug: Check What Files Are Found

The app should print:
```
Found X files in folder. Processing...
```

If it says "Found 0 files", the folder is either:
- Empty
- Wrong ID
- Not accessible

## Quick Checklist

- [ ] Folder ID is correct in config
- [ ] Folder has files in it
- [ ] Signed in with correct Google account
- [ ] Folder is accessible (not deleted or moved)
- [ ] Files are supported formats (Docs, PDF, Word, Text, CSV)

---

**After fixing, the app should find and load your documents!**

