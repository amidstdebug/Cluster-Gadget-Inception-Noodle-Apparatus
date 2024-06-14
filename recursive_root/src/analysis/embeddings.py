import numpy as np
from openai import OpenAI
from src.config import EMBEDDING_OPENAI_KEY

class EmbeddingAnalysis:
    def __init__(self):
        self.client = OpenAI(api_key=EMBEDDING_OPENAI_KEY)

    def get_embeddings(self, texts, batch_size=100):
        embeddings = []
        for i in range(0, len(texts), batch_size):
            end = min(len(texts), i + batch_size)
            response = self.client.embeddings.create(
                model="text-embedding-3-small",
                input=texts[i:end]
            )
            embeddings.extend(response['data'])
        return np.array([embed['embedding'] for embed in embeddings])

    def remove_near_identical(self, vectors, threshold=0.01):
        to_remove = set()
        for i in range(len(vectors)):
            for j in range(i+1, len(vectors)):
                if j in to_remove:
                    continue
                distance = np.linalg.norm(vectors[i] - vectors[j])
                if distance < threshold:
                    to_remove.add(j)

        full = set(range(len(vectors)))
        remaining = list(full - to_remove)
        filtered_vectors = np.delete(vectors, list(to_remove), axis=0)
        return filtered_vectors, remaining
