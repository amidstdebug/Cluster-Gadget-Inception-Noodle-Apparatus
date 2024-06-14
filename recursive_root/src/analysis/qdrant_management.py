from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct
from qdrant_client.http.models import Distance, VectorParams

class QdrantManager:
    def __init__(self, collection_name="main_test"):
        self.client = QdrantClient(":memory:")
        self.collection_name = collection_name

        try:
            self.client.delete_collection(self.collection_name)
        except Exception:
            pass

        self.client.create_collection(
            collection_name=self.collection_name,
            vectors_config=VectorParams(size=256, distance=Distance.COSINE),
        )

    def upsert_embeddings(self, embeddings, snippets):
        points = [
            PointStruct(
                id=idx,
                vector=embedding.tolist(),
                payload={"snippet": snippets[idx]}
            )
            for idx, embedding in enumerate(embeddings)
        ]
        self.client.upsert(collection_name=self.collection_name, points=points)

    def search_similar(self, query_embedding, limit=3):
        return self.client.search(
            collection_name=self.collection_name,
            query_vector=query_embedding,
            limit=limit
        )
