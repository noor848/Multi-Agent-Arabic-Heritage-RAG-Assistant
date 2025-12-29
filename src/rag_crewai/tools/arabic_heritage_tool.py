from crewai.tools import BaseTool
from typing import List, Type, Any
from pydantic import BaseModel, Field, ConfigDict
from sentence_transformers import SentenceTransformer
import numpy as np



class TXTSearchInput(BaseModel):
    query: str = Field(..., description="Search query")


class ArabicHeritageTool(BaseTool):
    name: str = "search_arabic_heritage"
    description: str = "Searches the Arabic heritage document for relevant information"
    args_schema: Type[BaseModel] = TXTSearchInput
    model_config = ConfigDict(extra='forbid')  # ← THIS LINE

    # Allow arbitrary types for Pydantic v2
    # model_config = ConfigDict(arbitrary_types_allowed=True)

    # Declare fields properly
    embedding_model: Any = None
    text_chunks: List[str] = []
    chunk_embeddings: Any = None

    def __init__(self):
        super().__init__()

        print("Loading embedding model...")
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

        with open("knowledge/_ALL_ARAB_HERITAGE_EN.txt", 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        self.text_chunks = self._create_chunks(content)
        print(f"Created {len(self.text_chunks)} chunks")

        print("Generating embeddings...")
        self.chunk_embeddings = self.embedding_model.encode(
            self.text_chunks,
            show_progress_bar=True,
            normalize_embeddings=True
        )
        print("✓ Tool ready!")

    def _create_chunks(self, text: str, chunk_size: int = 400) -> List[str]:
        words = text.split()
        chunks = []
        for i in range(0, len(words), chunk_size):
            chunk = ' '.join(words[i:i + chunk_size])
            chunks.append(chunk)
        return chunks

    def _run(self, query: str) -> str:

        query_embedding = self.embedding_model.encode(
            [query],
            normalize_embeddings=True
        )[0]

        similarities = np.dot(self.chunk_embeddings, query_embedding)
        top_indices = np.argsort(similarities)[-3:][::-1]

        results = [self.text_chunks[i] for i in top_indices]
        return "\n\n--- RELEVANT CHUNK ---\n\n".join(results)

print("Initializing Arabic Heritage Search Tool...")
