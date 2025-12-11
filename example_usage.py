"""
Example usage of the Google Drive to Gemini connector.
This demonstrates how to use the connector programmatically.
"""
from drive_connector import DriveConnector
from gemini_connector import GeminiConnector
from rag_processor import RAGProcessor
from config import DRIVE_FOLDER_ID


def example_basic_usage():
    """Basic example: Load documents and query."""
    print("=" * 60)
    print("Example 1: Basic Usage")
    print("=" * 60)
    
    # Initialize connectors
    print("\n1. Connecting to Google Drive...")
    drive = DriveConnector(DRIVE_FOLDER_ID)
    
    print("2. Loading documents...")
    documents = drive.get_all_documents()
    print(f"   Loaded {len(documents)} documents")
    
    print("3. Processing documents for RAG...")
    rag = RAGProcessor()
    rag.load_documents(documents)
    
    print("4. Initializing Gemini...")
    gemini = GeminiConnector()
    
    # Query
    print("\n5. Querying Gemini...")
    query = "What are the main topics in these documents?"
    context = rag.retrieve_relevant_chunks(query, top_k=3)
    response = gemini.query_with_context(query, context)
    
    print(f"\nQuery: {query}")
    print(f"\nResponse:\n{response}\n")


def example_multiple_queries():
    """Example: Multiple queries on the same documents."""
    print("=" * 60)
    print("Example 2: Multiple Queries")
    print("=" * 60)
    
    # Initialize once
    drive = DriveConnector(DRIVE_FOLDER_ID)
    documents = drive.get_all_documents()
    rag = RAGProcessor()
    rag.load_documents(documents)
    gemini = GeminiConnector()
    
    # Multiple queries
    queries = [
        "Summarize the key points",
        "What are the main themes?",
        "List any action items mentioned"
    ]
    
    for i, query in enumerate(queries, 1):
        print(f"\n--- Query {i} ---")
        print(f"Q: {query}")
        context = rag.retrieve_relevant_chunks(query)
        response = gemini.query_with_context(query, context)
        print(f"A: {response[:200]}...")  # First 200 chars


def example_specific_file():
    """Example: Query specific file content."""
    print("=" * 60)
    print("Example 3: Query Specific File")
    print("=" * 60)
    
    drive = DriveConnector(DRIVE_FOLDER_ID)
    documents = drive.get_all_documents()
    
    # Get specific file
    file_name = list(documents.keys())[0] if documents else None
    if file_name:
        print(f"\nQuerying file: {file_name}")
        file_content = documents[file_name]
        
        gemini = GeminiConnector()
        query = "What is this document about?"
        response = gemini.query_with_context(query, file_content[:30000])
        
        print(f"\nResponse:\n{response}\n")


def example_list_files():
    """Example: List all files in folder."""
    print("=" * 60)
    print("Example 4: List Files")
    print("=" * 60)
    
    drive = DriveConnector(DRIVE_FOLDER_ID)
    files = drive.list_files()
    
    print(f"\nFound {len(files)} files in folder:\n")
    for file in files:
        print(f"  - {file['name']} ({file.get('mimeType', 'unknown type')})")


if __name__ == '__main__':
    print("\n" + "=" * 60)
    print("Google Drive to Gemini Connector - Examples")
    print("=" * 60 + "\n")
    
    try:
        # Run examples
        example_list_files()
        print("\n")
        example_basic_usage()
        # Uncomment to run other examples:
        # example_multiple_queries()
        # example_specific_file()
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        print("\nMake sure you have:")
        print("  1. Set DRIVE_FOLDER_ID in config.py or .env")
        print("  2. Set GEMINI_API_KEY in config.py or .env")
        print("  3. Placed credentials.json in the project root")
        print("  4. Installed all dependencies: pip install -r requirements.txt")

