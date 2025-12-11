# How to Install Python on Windows

## Quick Installation Guide

### Method 1: Install from Python.org (Recommended)

1. **Download Python:**
   - Go to https://www.python.org/downloads/
   - Click the big yellow "Download Python" button (latest version)
   - Or go directly to: https://www.python.org/downloads/windows/

2. **Run the Installer:**
   - Double-click the downloaded `.exe` file
   - **IMPORTANT:** Check the box "Add Python to PATH" at the bottom of the installer
   - Click "Install Now"
   - Wait for installation to complete

3. **Verify Installation:**
   - Close and reopen your terminal/PowerShell
   - Run: `python --version`
   - You should see something like: `Python 3.11.x`

4. **Install Dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

### Method 2: Install from Microsoft Store

1. **Open Microsoft Store:**
   - Press `Windows Key`
   - Type "Microsoft Store" and open it

2. **Search for Python:**
   - Search for "Python 3.11" or "Python 3.12"
   - Click "Install"

3. **Verify Installation:**
   - Close and reopen PowerShell
   - Run: `python --version`

4. **Install Dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

## After Installing Python

### Step 1: Close and Reopen PowerShell
- Close your current PowerShell window
- Open a new PowerShell window
- Navigate back to your project:
  ```powershell
  cd D:\task\2025_12_10__Google_Gemini\my_work
  ```

### Step 2: Verify Python is Working
```powershell
python --version
```

### Step 3: Install Project Dependencies
```powershell
pip install -r requirements.txt
```

If `pip` still doesn't work, try:
```powershell
python -m pip install -r requirements.txt
```

## Troubleshooting

### Issue: "python is not recognized" after installation

**Solution 1: Restart PowerShell**
- Close PowerShell completely
- Open a new PowerShell window
- Try again

**Solution 2: Check PATH**
- During installation, make sure you checked "Add Python to PATH"
- If you didn't, reinstall Python and check this box

**Solution 3: Use Full Path**
- Find where Python is installed (usually `C:\Users\YourName\AppData\Local\Programs\Python\`)
- Use the full path to pip:
  ```powershell
  C:\Users\YourName\AppData\Local\Programs\Python\Python311\Scripts\pip.exe install -r requirements.txt
  ```

### Issue: "pip is not recognized"

**Solution:**
```powershell
python -m pip install -r requirements.txt
```

### Issue: Permission Denied

**Solution:**
Run PowerShell as Administrator:
1. Right-click PowerShell
2. Select "Run as Administrator"
3. Navigate to your project folder
4. Run the install command

## Quick Checklist

- [ ] Python downloaded from python.org
- [ ] "Add Python to PATH" checked during installation
- [ ] Installation completed
- [ ] PowerShell closed and reopened
- [ ] `python --version` works
- [ ] `pip install -r requirements.txt` works

## What Version to Install?

- **Python 3.8 or higher** is required
- **Python 3.11 or 3.12** is recommended (latest stable)
- Make sure to get the 64-bit version for Windows

---

**After Python is installed, continue with Step 4 of the setup guide!**

