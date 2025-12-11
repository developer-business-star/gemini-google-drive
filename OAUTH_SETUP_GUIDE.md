# OAuth Client ID Setup Guide

This guide will walk you through configuring the OAuth consent screen and creating the OAuth client ID step by step.

## Step 1: Configure OAuth Consent Screen (REQUIRED FIRST STEP)

**Important:** You MUST configure the OAuth consent screen BEFORE creating the OAuth client ID.

### 1.1 Navigate to OAuth Consent Screen

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Make sure you have the correct project selected (top dropdown)
3. Go to **"APIs & Services"** → **"OAuth consent screen"**
   - Or directly: https://console.cloud.google.com/apis/credentials/consent

### 1.2 Configure User Type

1. You'll see a screen asking "What user type do you want to support?"
2. Choose **"External"** (unless you have a Google Workspace account)
3. Click **"Create"**

### 1.3 Fill App Information (Step 1 of 4)

Fill in the required fields:

- **App name**: `Drive Gemini Connector` (or any name you prefer)
- **User support email**: Select your email from dropdown
- **App logo**: (Optional) You can skip this
- **App domain**: (Optional) Leave blank for personal use
- **Application home page**: (Optional) Leave blank
- **Application privacy policy link**: (Optional) Leave blank
- **Application terms of service link**: (Optional) Leave blank
- **Authorized domains**: (Optional) Leave blank
- **Developer contact information**: Enter your email address

Click **"Save and Continue"**

### 1.4 Configure Scopes (Step 2 of 4)

This is where you specify what permissions your app needs:

1. Click **"Add or Remove Scopes"**
2. In the filter box, search for: `drive.readonly`
3. Check the box for: **`https://www.googleapis.com/auth/drive.readonly`**
   - This gives read-only access to Google Drive files
4. Click **"Update"**
5. Click **"Save and Continue"**

### 1.5 Add Test Users (Step 3 of 4)

Since this is for personal use, you need to add yourself as a test user:

1. Click **"Add Users"**
2. Enter your Google account email address
3. Click **"Add"**
4. Click **"Save and Continue"**

### 1.6 Review and Summary (Step 4 of 4)

1. Review all the information you entered
2. Click **"Back to Dashboard"**

**✅ OAuth Consent Screen is now configured!**

## Step 2: Create OAuth Client ID

Now you can create the OAuth client ID:

### 2.1 Navigate to Credentials

1. Go to **"APIs & Services"** → **"Credentials"**
   - Or directly: https://console.cloud.google.com/apis/credentials

### 2.2 Create OAuth Client ID

1. Click **"Create Credentials"** button (top of the page)
2. Select **"OAuth client ID"** from the dropdown

### 2.3 Configure OAuth Client

1. **Application type**: Select **"Desktop app"**
2. **Name**: Enter a name like `Drive Connector Desktop` or `Drive Gemini Connector`
3. Click **"Create"**

### 2.4 Download Credentials

1. A popup will appear showing your **Client ID** and **Client Secret**
2. Click **"Download JSON"** button
3. Save the file as `credentials.json`
4. Move this file to your project root directory (where `app.py` is located)

**✅ OAuth Client ID created and downloaded!**

## Step 3: Verify Setup

Your `credentials.json` file should look something like this:

```json
{
  "installed": {
    "client_id": "your-client-id.apps.googleusercontent.com",
    "project_id": "your-project-id",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_secret": "your-client-secret",
    "redirect_uris": ["http://localhost"]
  }
}
```

## Troubleshooting

### Issue: "To create an OAuth client ID, you must first configure your consent screen"

**Solution:** You're seeing this because you skipped Step 1. Go back and complete the OAuth consent screen configuration first (see Step 1 above).

### Issue: Can't find "OAuth consent screen" option

**Solution:** 
- Make sure you're in the correct Google Cloud project
- Go directly to: https://console.cloud.google.com/apis/credentials/consent
- Make sure you have the necessary permissions in the project

### Issue: "App verification required" warning

**Solution:** 
- For personal use, you can ignore this
- The app will work in "Testing" mode
- Only add yourself as a test user (Step 1.5)

### Issue: Can't add scopes

**Solution:**
- Make sure you're searching for the exact scope: `drive.readonly`
- The full scope URL is: `https://www.googleapis.com/auth/drive.readonly`
- Make sure Google Drive API is enabled in your project

### Issue: Downloaded file has different name

**Solution:**
- Rename it to exactly `credentials.json` (case-sensitive)
- Make sure it's in the same folder as `app.py`

## Quick Checklist

- [ ] OAuth consent screen configured (User Type selected)
- [ ] App information filled in
- [ ] `drive.readonly` scope added
- [ ] Test user (yourself) added
- [ ] OAuth client ID created (Desktop app type)
- [ ] `credentials.json` downloaded and renamed
- [ ] `credentials.json` placed in project root

## Next Steps

After completing OAuth setup:

1. Continue with **Part 2** of `SETUP_GUIDE.md` (Get Gemini API Key)
2. Continue with **Part 3** of `SETUP_GUIDE.md` (Get Google Drive Folder ID)
3. Continue with **Part 4** of `SETUP_GUIDE.md` (Install and Configure)
4. Run the application: `python app.py`

---

**Need help?** Refer to the main `SETUP_GUIDE.md` or `README.md` for complete instructions.

