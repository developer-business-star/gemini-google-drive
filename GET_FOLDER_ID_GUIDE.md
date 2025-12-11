# How to Get Google Drive Folder ID - Step by Step Guide

This guide will walk you through finding your Google Drive Folder ID in multiple ways.

## Method 1: From Google Drive URL (Easiest)

### Step 1: Open Google Drive
1. Go to [Google Drive](https://drive.google.com)
2. Sign in with your Google account

### Step 2: Navigate to Your Folder
1. Find the folder you want to connect to Gemini
2. **Click once** on the folder to select it (don't double-click to open it yet)

### Step 3: Open the Folder
1. **Double-click** the folder to open it
2. OR right-click the folder and select "Open in new tab"

### Step 4: Look at the Browser URL
1. Look at the address bar in your browser
2. The URL will look like one of these formats:

**Format 1:**
```
https://drive.google.com/drive/folders/1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p
```

**Format 2:**
```
https://drive.google.com/drive/u/0/folders/1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p
```

### Step 5: Copy the Folder ID
1. Find the part that comes **after** `/folders/`
2. The Folder ID is the long string of letters and numbers
3. In the examples above, the Folder ID would be: `1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p`
4. **Copy this entire string** (it's usually 33 characters long)

### Example:
If your URL is:
```
https://drive.google.com/drive/folders/1ABC123def456GHI789jkl012MNO345pqr
```

Then your Folder ID is:
```
1ABC123def456GHI789jkl012MNO345pqr
```

---

## Method 2: From Folder Properties (Alternative)

### Step 1: Right-Click the Folder
1. In Google Drive, find your folder
2. **Right-click** on the folder
3. Select **"Get link"** or **"Share"**

### Step 2: Copy the Link
1. A dialog box will appear with a link
2. The link will look like:
   ```
   https://drive.google.com/drive/folders/1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p?usp=sharing
   ```
3. Copy the entire link

### Step 3: Extract the Folder ID
1. The Folder ID is the part between `/folders/` and `?` (or end of URL)
2. In the example above: `1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p`

---

## Method 3: From Shared Folder Link

If someone shared a folder with you:

1. The shared link will look like:
   ```
   https://drive.google.com/drive/folders/1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p?usp=sharing
   ```
2. The Folder ID is the same - the part after `/folders/` and before `?`

---

## Visual Guide

### What the URL Looks Like:

```
https://drive.google.com/drive/folders/[THIS_IS_YOUR_FOLDER_ID]
                                    ↑
                          Copy everything after /folders/
```

### Folder ID Characteristics:

- ✅ Usually 33 characters long
- ✅ Contains letters (both uppercase and lowercase) and numbers
- ✅ No spaces or special characters (except sometimes hyphens)
- ✅ Example format: `1aB2cD3eF4gH5iJ6kL7mN8oP9qR0sT1uV2wX`

---

## Common Mistakes to Avoid

### ❌ Wrong: Copying the entire URL
```
❌ https://drive.google.com/drive/folders/1a2b3c4d5e6f7g8h9i0j
```

### ✅ Correct: Copying only the Folder ID
```
✅ 1a2b3c4d5e6f7g8h9i0j
```

### ❌ Wrong: Including query parameters
```
❌ 1a2b3c4d5e6f7g8h9i0j?usp=sharing
```

### ✅ Correct: Just the ID
```
✅ 1a2b3c4d5e6f7g8h9i0j
```

---

## How to Verify Your Folder ID is Correct

1. **Format Check:**
   - Should be about 33 characters
   - Contains letters and numbers
   - No spaces

2. **Test in Browser:**
   - Try visiting: `https://drive.google.com/drive/folders/YOUR_FOLDER_ID`
   - If it opens your folder, the ID is correct!

3. **Test in Application:**
   - Add it to your `.env` file
   - Run the application
   - If documents load, the ID is correct!

---

## Step-by-Step Checklist

- [ ] Opened Google Drive in browser
- [ ] Found the folder I want to connect
- [ ] Opened the folder (double-clicked or right-click → open in new tab)
- [ ] Looked at the browser URL bar
- [ ] Found the part after `/folders/`
- [ ] Copied the Folder ID (long string of letters/numbers)
- [ ] Verified it's about 33 characters
- [ ] Tested by visiting the URL with the ID
- [ ] Saved it to `.env` file as `DRIVE_FOLDER_ID=...`

---

## Adding Folder ID to Your Project

Once you have the Folder ID:

### Option 1: Add to `.env` file

Create or edit `.env` file in your project root:

```env
DRIVE_FOLDER_ID=1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p
GEMINI_API_KEY=your_gemini_api_key_here
```

### Option 2: Add to `config.py`

Edit `config.py`:

```python
DRIVE_FOLDER_ID = '1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p'
```

**Replace** `1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p` with your actual Folder ID.

---

## Troubleshooting

### Problem: "I can't see the folder ID in the URL"

**Solutions:**
- Make sure you've **opened** the folder (double-clicked it)
- Try right-clicking the folder → "Open in new tab"
- The URL should contain `/folders/` in it

### Problem: "The URL looks different"

**Different URL formats:**
- `drive.google.com/drive/folders/ID` ✅
- `drive.google.com/drive/u/0/folders/ID` ✅ (same ID, just different format)
- `drive.google.com/file/d/ID` ❌ (This is a file, not a folder)

### Problem: "I see a file ID instead of folder ID"

**Solution:**
- Make sure you're clicking on a **folder** (has a folder icon)
- Files have `/file/d/` in the URL
- Folders have `/folders/` in the URL

### Problem: "The folder is shared with me"

**Solution:**
- Shared folders work the same way
- The Folder ID is still in the URL after `/folders/`
- Make sure you have at least "Viewer" access to the folder

---

## Quick Reference

**What you need:**
- A Google Drive folder
- Access to open that folder
- The URL from your browser

**What you get:**
- A Folder ID (33-character string)
- Use it in `DRIVE_FOLDER_ID` in your `.env` file

**Example:**
```
URL: https://drive.google.com/drive/folders/1ABC123def456GHI789jkl012MNO345pqr
ID:  1ABC123def456GHI789jkl012MNO345pqr
```

---

**Need more help?** Check the main `README.md` or `SETUP_GUIDE.md` for complete setup instructions.

