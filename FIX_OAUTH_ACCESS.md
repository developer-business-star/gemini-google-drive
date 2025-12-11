# Fix OAuth Access Blocked Error

## Problem
You're seeing: "Access blocked: Drive Gemini Connector has not completed the Google verification process"

This happens because your OAuth app is in "Testing" mode and your email isn't added as a test user.

## Solution: Add Yourself as a Test User

### Step 1: Go to OAuth Consent Screen

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Make sure you're in the correct project
3. Navigate to **"APIs & Services"** → **"OAuth consent screen"**
   - Direct link: https://console.cloud.google.com/apis/credentials/consent

### Step 2: Add Test Users

1. Scroll down to the **"Test users"** section
2. Click **"Add Users"** button
3. Enter your email address: `famousdev3@gmail.com`
4. Click **"Add"**
5. Click **"Save"** at the bottom of the page

### Step 3: Try Again

1. Close the browser window with the error
2. Run your application again:
   ```cmd
   py app.py
   ```
3. When the browser opens for authentication, try again
4. You should now be able to authorize the app

## Alternative: Publish the App (Not Recommended for Personal Use)

If you want to avoid adding test users, you can publish the app, but this requires:
- App verification by Google
- Privacy policy URL
- Terms of service URL
- More complex setup

**For personal use, adding test users is the easiest solution.**

## Quick Checklist

- [ ] Go to OAuth Consent Screen in Google Cloud Console
- [ ] Find "Test users" section
- [ ] Click "Add Users"
- [ ] Add `famousdev3@gmail.com`
- [ ] Save changes
- [ ] Try running the app again

## Still Having Issues?

If you still get blocked after adding yourself as a test user:

1. **Wait a few minutes** - Changes can take a moment to propagate
2. **Clear browser cache** - Sometimes cached errors persist
3. **Use incognito/private window** - To avoid cache issues
4. **Check the email** - Make sure you're using the exact email that's added as a test user

---

**After adding yourself as a test user, the authentication should work!**

