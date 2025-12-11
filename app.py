"""
Main Flask application for Google Drive to Gemini connector.
Provides a web interface and API for querying documents via Gemini.
"""
from flask import Flask, request, jsonify, render_template_string
from drive_connector import DriveConnector
from gemini_connector import GeminiConnector
from rag_processor import RAGProcessor
from config import DRIVE_FOLDER_ID
import os

app = Flask(__name__)

# Global instances
drive_connector = None
gemini_connector = None
rag_processor = None


def initialize_connectors(folder_id: str = None):
    """Initialize all connectors with the specified folder ID."""
    global drive_connector, gemini_connector, rag_processor
    
    folder_id = folder_id or DRIVE_FOLDER_ID
    
    if folder_id == 'YOUR_FOLDER_ID_HERE':
        raise ValueError(
            "DRIVE_FOLDER_ID not set. Please set it in .env file or config.py"
        )
    
    print("Initializing Google Drive connector...")
    drive_connector = DriveConnector(folder_id)
    
    print("Initializing Google Gemini connector...")
    gemini_connector = GeminiConnector()
    
    print("Loading documents from Google Drive...")
    documents = drive_connector.get_all_documents()
    
    print("Processing documents for RAG...")
    rag_processor = RAGProcessor()
    rag_processor.load_documents(documents)
    
    print("✓ All connectors initialized successfully!")
    return True


# HTML template for the web interface
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Google Drive to Gemini Connector</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background: #f5f5f5;
        }
        .container {
            background: white;
            border-radius: 8px;
            padding: 30px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #1a73e8;
            margin-bottom: 10px;
        }
        .subtitle {
            color: #666;
            margin-bottom: 30px;
        }
        .query-form {
            margin-bottom: 30px;
        }
        textarea {
            width: 100%;
            min-height: 100px;
            padding: 12px;
            border: 2px solid #ddd;
            border-radius: 4px;
            font-size: 14px;
            font-family: inherit;
            resize: vertical;
        }
        textarea:focus {
            outline: none;
            border-color: #1a73e8;
        }
        button {
            background: #1a73e8;
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 4px;
            font-size: 16px;
            cursor: pointer;
            margin-top: 10px;
        }
        button:hover {
            background: #1557b0;
        }
        button:disabled {
            background: #ccc;
            cursor: not-allowed;
        }
        .response {
            margin-top: 20px;
            padding: 20px;
            background: #f9f9f9;
            border-radius: 4px;
            border-left: 4px solid #1a73e8;
            white-space: pre-wrap;
            line-height: 1.6;
        }
        .loading {
            color: #666;
            font-style: italic;
        }
        .error {
            color: #d32f2f;
            background: #ffebee;
            border-left-color: #d32f2f;
        }
        .info {
            background: #e3f2fd;
            padding: 15px;
            border-radius: 4px;
            margin-bottom: 20px;
            border-left: 4px solid #1a73e8;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 Google Drive to Gemini Connector</h1>
        <p class="subtitle">Query your Google Drive documents using Google Gemini AI</p>
        
        <div class="info">
            <strong>Connected Folder ID:</strong> {{ folder_id }}<br>
            <strong>Documents Loaded:</strong> {{ doc_count }} files<br>
            <strong>Model:</strong> gemini-flash-latest (Free Tier) ✅
        </div>
        
        <div class="info" style="background: #fff3cd; border-left-color: #ffc107;">
            <strong>💡 Pricing Information:</strong><br>
            This application uses <strong>free tier models</strong> (no cost). For premium models like gemini-2.5-pro, 
            a paid Google Cloud billing account is required. See <code>CLIENT_PRICING_MESSAGE.md</code> for details.
        </div>
        
        <div class="query-form">
            <form id="queryForm">
                <label for="query"><strong>Enter your question or prompt:</strong></label>
                <textarea id="query" name="query" placeholder="Ask anything about your documents..."></textarea>
                <button type="submit">Ask Gemini</button>
            </form>
        </div>
        
        <div id="response" class="response" style="display: none;"></div>
    </div>
    
    <script>
        document.getElementById('queryForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            const query = document.getElementById('query').value;
            const responseDiv = document.getElementById('response');
            const button = document.querySelector('button');
            
            if (!query.trim()) {
                alert('Please enter a question');
                return;
            }
            
            responseDiv.style.display = 'block';
            responseDiv.className = 'response loading';
            responseDiv.textContent = 'Processing your query...';
            button.disabled = true;
            
            try {
                const response = await fetch('/api/query', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ query: query })
                });
                
                const data = await response.json();
                
                if (data.error) {
                    responseDiv.className = 'response error';
                    responseDiv.textContent = 'Error: ' + data.error;
                } else {
                    responseDiv.className = 'response';
                    responseDiv.textContent = data.response;
                }
            } catch (error) {
                responseDiv.className = 'response error';
                responseDiv.textContent = 'Error: ' + error.message;
            } finally {
                button.disabled = false;
            }
        });
    </script>
</body>
</html>
"""


@app.route('/')
def index():
    """Render the main web interface."""
    doc_count = len(rag_processor.documents) if rag_processor else 0
    return render_template_string(
        HTML_TEMPLATE,
        folder_id=DRIVE_FOLDER_ID,
        doc_count=doc_count
    )


@app.route('/api/query', methods=['POST'])
def query():
    """API endpoint for querying documents via Gemini."""
    if not gemini_connector or not rag_processor:
        return jsonify({'error': 'Connectors not initialized'}), 500
    
    data = request.get_json()
    user_query = data.get('query', '')
    
    if not user_query:
        return jsonify({'error': 'Query is required'}), 400
    
    try:
        # Retrieve relevant context from documents
        context = rag_processor.retrieve_relevant_chunks(user_query, top_k=5)
        
        # If no context found, use all content (for small document sets)
        if not context.strip():
            context = rag_processor.get_all_content()
            # Still truncate if too long
            if len(context) > 30000:
                context = context[:30000] + "... [truncated]"
        
        # Query Gemini with context
        response = gemini_connector.query_with_context(user_query, context)
        
        return jsonify({'response': response})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/reload', methods=['POST'])
def reload():
    """Reload documents from Google Drive."""
    try:
        folder_id = request.json.get('folder_id') if request.json else None
        initialize_connectors(folder_id)
        return jsonify({
            'success': True,
            'message': f'Reloaded {len(rag_processor.documents)} documents'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/status', methods=['GET'])
def status():
    """Get status of the connector."""
    return jsonify({
        'initialized': rag_processor is not None,
        'document_count': len(rag_processor.documents) if rag_processor else 0,
        'folder_id': DRIVE_FOLDER_ID
    })


if __name__ == '__main__':
    # Initialize connectors on startup
    try:
        initialize_connectors()
        print("\n" + "="*50)
        print("✓ Application started successfully!")
        print("="*50)
        print(f"📁 Connected to folder: {DRIVE_FOLDER_ID}")
        print(f"📄 Loaded {len(rag_processor.documents)} documents")
        print(f"🌐 Web interface: http://localhost:5000")
        print(f"🔌 API endpoint: http://localhost:5000/api/query")
        print("="*50 + "\n")
    except Exception as e:
        print(f"\n❌ Error initializing: {str(e)}\n")
        print("Please check your configuration and try again.\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000, use_reloader=False)

