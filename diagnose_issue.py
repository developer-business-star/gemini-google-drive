"""
Diagnostic script to check why connectors aren't initializing.
Run this to see detailed error messages.
"""
from config import DRIVE_FOLDER_ID, GEMINI_API_KEY, CREDENTIALS_FILE
import os

print("=" * 60)
print("Diagnostic Check")
print("=" * 60)

# Check 1: Configuration
print("\n1. Checking Configuration...")
print(f"   DRIVE_FOLDER_ID: {DRIVE_FOLDER_ID}")
print(f"   GEMINI_API_KEY: {'Set' if GEMINI_API_KEY and GEMINI_API_KEY != 'YOUR_GEMINI_API_KEY_HERE' else 'NOT SET'}")
print(f"   CREDENTIALS_FILE: {CREDENTIALS_FILE}")

# Check 2: Files
print("\n2. Checking Files...")
print(f"   credentials.json exists: {os.path.exists(CREDENTIALS_FILE)}")
print(f"   token.json exists: {os.path.exists('token.json')}")

# Check 3: Try Gemini initialization
print("\n3. Testing Gemini Connector...")
try:
    from gemini_connector import GeminiConnector
    gemini = GeminiConnector()
    print("   ✓ Gemini connector initialized successfully")
    print(f"   Model: {gemini.model._model_name if hasattr(gemini.model, '_model_name') else 'Unknown'}")
except Exception as e:
    print(f"   ✗ Gemini connector failed: {str(e)}")
    print(f"   Error type: {type(e).__name__}")

# Check 4: Try Drive connector
print("\n4. Testing Drive Connector...")
try:
    from drive_connector import DriveConnector
    drive = DriveConnector(DRIVE_FOLDER_ID)
    print("   ✓ Drive connector initialized successfully")
    
    # Try to list files
    files = drive.list_files()
    print(f"   Found {len(files)} files in folder")
    if files:
        print("   Files:")
        for f in files[:5]:  # Show first 5
            print(f"     - {f['name']} ({f.get('mimeType', 'unknown')})")
except Exception as e:
    print(f"   ✗ Drive connector failed: {str(e)}")
    print(f"   Error type: {type(e).__name__}")

# Check 5: Try full initialization
print("\n5. Testing Full Initialization...")
try:
    from app import initialize_connectors
    initialize_connectors()
    print("   ✓ Full initialization successful!")
except Exception as e:
    print(f"   ✗ Full initialization failed: {str(e)}")
    print(f"   Error type: {type(e).__name__}")
    import traceback
    print("\n   Full traceback:")
    traceback.print_exc()

print("\n" + "=" * 60)
print("Diagnostic complete!")
print("=" * 60)

