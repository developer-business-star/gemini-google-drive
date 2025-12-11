# Troubleshooting OAuth Access Blocked Error

## Issue: Still Getting "Access Blocked" After Adding Test User

If you've added yourself as a test user but still see the error, try these solutions:

## Solution 1: Delete Token and Re-authenticate

The old authentication token might be cached. Delete it and re-authenticate:

1. **Delete the token file:**
   - In your project folder, delete `token.json` if it exists
   - This forces a fresh authentication

2. **Run the app again:**
   ```cmd
   py app.py
   ```

3. **When browser opens:**
   - Make sure you're signed in with `famousdev3@gmail.com`
   - Grant permissions
   - Complete the authentication

## Solution 2: Verify Test User Was Saved

1. Go to OAuth Consent Screen: https://console.cloud.google.com/apis/credentials/consent
2. Scroll to "Test users" section
3. Verify `famousdev3@gmail.com` is in the list
4. If not, add it again and **click "Save"** at the bottom
5. Wait 2-3 minutes for changes to propagate

## Solution 3: Use Incognito/Private Browser

Sometimes browser cache causes issues:

1. Close all browser windows
2. Open an **Incognito/Private window** (Ctrl+Shift+N in Chrome)
3. Run your app: `py app.py`
4. When browser opens, try authentication again

## Solution 4: Check You're Using the Correct Email

Make sure you're signing in with the exact email that's in the test users list:
- Test user email: `famousdev3@gmail.com`
- Sign in with: `famousdev3@gmail.com` (exact match, no typos)

## Solution 5: Wait and Retry

Google's changes can take a few minutes to propagate:
1. Wait 3-5 minutes after adding test user
2. Try again

## Solution 6: Check OAuth Consent Screen Status

1. Go to OAuth Consent Screen
2. Check the publishing status
3. Make sure it says "Testing" (not "In production")
4. For personal use, "Testing" mode is fine

## Solution 7: Complete All OAuth Consent Screen Steps

Make sure you've completed all required steps:
1. ✅ User Type selected (External)
2. ✅ App Information filled
3. ✅ Scopes added (`drive.readonly`)
4. ✅ Test users added (`famousdev3@gmail.com`)
5. ✅ All steps saved

## Solution 8: Check Browser Console for Errors

1. When the error page appears, press F12
2. Check the Console tab for any errors
3. Look for specific error messages

## Most Common Fix: Delete token.json

**This is usually the solution:**

1. Stop your app (Ctrl+C)
2. Delete `token.json` file in your project folder
3. Run app again: `py app.py`
4. Authenticate fresh

---

## Step-by-Step Fix (Recommended)

1. **Stop the app** (if running): Press Ctrl+C

2. **Delete token.json:**
   ```cmd
   del token.json
   ```
   Or manually delete the file in your project folder

3. **Verify test user is added:**
   - Go to: https://console.cloud.google.com/apis/credentials/consent
   - Check "Test users" section
   - Make sure `famousdev3@gmail.com` is there
   - If not, add it and click "Save"

4. **Wait 2 minutes** for changes to apply

5. **Run app in fresh browser:**
   - Close all browser windows
   - Open incognito/private window
   - Run: `py app.py`

6. **Sign in with correct email:**
   - Use: `famousdev3@gmail.com`
   - Grant all permissions

---

## Still Not Working?

If none of these work, check:
- Are you in the correct Google Cloud project?
- Is the OAuth client ID correct in `credentials.json`?
- Are you using the same Google account everywhere?

