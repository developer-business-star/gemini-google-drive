"""
Google Drive API connector to read documents from a specified folder.
Supports Google Docs, PDFs, Word documents, and text files.
"""
import io
import os
from typing import List, Dict
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import PyPDF2
from config import SCOPES, CREDENTIALS_FILE


class DriveConnector:
    """Handles connection to Google Drive and document retrieval."""
    
    def __init__(self, folder_id: str):
        """
        Initialize Drive connector.
        
        Args:
            folder_id: Google Drive folder ID to connect to
        """
        self.folder_id = folder_id
        self.service = self._authenticate()
    
    def _authenticate(self):
        """Authenticate and return Google Drive service."""
        creds = None
        token_file = 'token.json'
        
        # Load existing token
        if os.path.exists(token_file):
            creds = Credentials.from_authorized_user_file(token_file, SCOPES)
        
        # If no valid credentials, get new ones
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                if not os.path.exists(CREDENTIALS_FILE):
                    raise FileNotFoundError(
                        f"Credentials file '{CREDENTIALS_FILE}' not found. "
                        "Please download OAuth2 credentials from Google Cloud Console."
                    )
                flow = InstalledAppFlow.from_client_secrets_file(
                    CREDENTIALS_FILE, SCOPES)
                creds = flow.run_local_server(port=0)
            
            # Save credentials for next run
            with open(token_file, 'w') as token:
                token.write(creds.to_json())
        
        return build('drive', 'v3', credentials=creds)
    
    def list_files(self) -> List[Dict]:
        """
        List all files in the connected folder.
        
        Returns:
            List of file metadata dictionaries
        """
        query = f"'{self.folder_id}' in parents and trashed=false"
        results = self.service.files().list(
            q=query,
            fields="files(id, name, mimeType, size)",
            pageSize=100
        ).execute()
        
        return results.get('files', [])
    
    def get_file_content(self, file_id: str, mime_type: str) -> str:
        """
        Extract text content from a Google Drive file.
        
        Args:
            file_id: Google Drive file ID
            mime_type: MIME type of the file
            
        Returns:
            Extracted text content
        """
        content = ""
        
        try:
            # Google Docs, Sheets, Slides
            if mime_type in [
                'application/vnd.google-apps.document',
                'application/vnd.google-apps.spreadsheet',
                'application/vnd.google-apps.presentation'
            ]:
                content = self._get_google_workspace_content(file_id, mime_type)
            
            # PDF files
            elif mime_type == 'application/pdf':
                content = self._get_pdf_content(file_id)
            
            # Plain text files
            elif mime_type in ['text/plain', 'text/csv']:
                content = self._get_text_content(file_id)
            
            # Microsoft Office files (export as text)
            elif mime_type in [
                'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                'application/msword'
            ]:
                content = self._get_office_content(file_id, mime_type)
            
            else:
                print(f"Unsupported file type: {mime_type}")
        
        except Exception as e:
            print(f"Error reading file {file_id}: {str(e)}")
        
        return content
    
    def _get_google_workspace_content(self, file_id: str, mime_type: str) -> str:
        """Extract content from Google Workspace files."""
        if mime_type == 'application/vnd.google-apps.document':
            # Export as plain text
            request = self.service.files().export_media(
                fileId=file_id,
                mimeType='text/plain'
            )
        elif mime_type == 'application/vnd.google-apps.spreadsheet':
            # Export as CSV
            request = self.service.files().export_media(
                fileId=file_id,
                mimeType='text/csv'
            )
        elif mime_type == 'application/vnd.google-apps.presentation':
            # Export as plain text
            request = self.service.files().export_media(
                fileId=file_id,
                mimeType='text/plain'
            )
        else:
            return ""
        
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
        
        return fh.getvalue().decode('utf-8', errors='ignore')
    
    def _get_pdf_content(self, file_id: str) -> str:
        """Extract text from PDF files."""
        request = self.service.files().get_media(fileId=file_id)
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
        
        fh.seek(0)
        pdf_reader = PyPDF2.PdfReader(fh)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
        
        return text
    
    def _get_text_content(self, file_id: str) -> str:
        """Extract content from plain text files."""
        request = self.service.files().get_media(fileId=file_id)
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
        
        return fh.getvalue().decode('utf-8', errors='ignore')
    
    def _get_office_content(self, file_id: str, mime_type: str) -> str:
        """Extract content from Microsoft Office files by exporting as text."""
        # Export Word docs as plain text
        export_mime = 'text/plain'
        request = self.service.files().export_media(
            fileId=file_id,
            mimeType=export_mime
        )
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
        
        return fh.getvalue().decode('utf-8', errors='ignore')
    
    def get_all_documents(self) -> Dict[str, str]:
        """
        Retrieve all documents from the folder and extract their content.
        
        Returns:
            Dictionary mapping file names to their content
        """
        files = self.list_files()
        documents = {}
        
        print(f"Found {len(files)} files in folder. Processing...")
        
        for file in files:
            file_name = file['name']
            file_id = file['id']
            mime_type = file.get('mimeType', '')
            
            print(f"Processing: {file_name}")
            content = self.get_file_content(file_id, mime_type)
            
            if content:
                documents[file_name] = content
                print(f"  ✓ Extracted {len(content)} characters from {file_name}")
            else:
                print(f"  ✗ Could not extract content from {file_name}")
        
        return documents

