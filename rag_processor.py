"""
RAG (Retrieval-Augmented Generation) processor for chunking and retrieving documents.
"""
from typing import List, Dict
from config import CHUNK_SIZE, CHUNK_OVERLAP


class RAGProcessor:
    """Processes documents for RAG by chunking and retrieving relevant content."""
    
    def __init__(self):
        """Initialize RAG processor."""
        self.documents = {}
        self.chunks = []
    
    def load_documents(self, documents: Dict[str, str]):
        """
        Load documents and create chunks.
        
        Args:
            documents: Dictionary mapping file names to content
        """
        self.documents = documents
        self.chunks = self._create_chunks(documents)
        print(f"Created {len(self.chunks)} chunks from {len(documents)} documents")
    
    def _create_chunks(self, documents: Dict[str, str]) -> List[Dict]:
        """
        Split documents into chunks for better retrieval.
        
        Args:
            documents: Dictionary mapping file names to content
            
        Returns:
            List of chunk dictionaries with metadata
        """
        chunks = []
        
        for file_name, content in documents.items():
            # Split content into chunks
            start = 0
            while start < len(content):
                end = start + CHUNK_SIZE
                chunk_text = content[start:end]
                
                chunks.append({
                    'file': file_name,
                    'content': chunk_text,
                    'start': start,
                    'end': min(end, len(content))
                })
                
                # Move start position with overlap
                start = end - CHUNK_OVERLAP
        
        return chunks
    
    def retrieve_relevant_chunks(self, query: str, top_k: int = 5) -> str:
        """
        Retrieve most relevant chunks based on query.
        Uses simple keyword matching (can be enhanced with embeddings).
        
        Args:
            query: User query
            top_k: Number of top chunks to retrieve
            
        Returns:
            Combined relevant context
        """
        if not self.chunks:
            return ""
        
        # Simple keyword-based retrieval
        # In production, you'd use embeddings and vector similarity
        query_lower = query.lower()
        query_words = set(query_lower.split())
        
        scored_chunks = []
        for chunk in self.chunks:
            chunk_lower = chunk['content'].lower()
            chunk_words = set(chunk_lower.split())
            
            # Calculate simple relevance score (word overlap)
            common_words = query_words.intersection(chunk_words)
            score = len(common_words) / max(len(query_words), 1)
            
            scored_chunks.append((score, chunk))
        
        # Sort by score and get top_k
        scored_chunks.sort(reverse=True, key=lambda x: x[0])
        top_chunks = scored_chunks[:top_k]
        
        # Combine top chunks
        context_parts = []
        for score, chunk in top_chunks:
            context_parts.append(
                f"--- From file: {chunk['file']} ---\n{chunk['content']}\n"
            )
        
        return "\n".join(context_parts)
    
    def get_all_content(self) -> str:
        """
        Get all document content (for small document sets).
        
        Returns:
            Combined content from all documents
        """
        content_parts = []
        for file_name, content in self.documents.items():
            content_parts.append(f"--- File: {file_name} ---\n{content}\n")
        return "\n".join(content_parts)

