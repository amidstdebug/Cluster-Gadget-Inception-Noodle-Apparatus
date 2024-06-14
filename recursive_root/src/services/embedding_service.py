from openai import OpenAI
from src.config import EMBEDDING_OPENAI_KEY

class EmbeddingService:
    def __init__(self):
        self.client = OpenAI(api_key=EMBEDDING_OPENAI_KEY)

    def get_embedding(self, text):
        response = self.client.embeddings.create(
            model="text-embedding-3-small",
            input=[text]
        )
        return response['data'][0]['embedding']
