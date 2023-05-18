from typing import List

from qdrant_client import QdrantClient
from qdrant_client.http.models.models import Filter, FieldCondition, MatchValue
from sentence_transformers import SentenceTransformer


class LyricsSearcher:

    def __init__(self, collection_name):
        self.collection_name = collection_name
        self.model = SentenceTransformer('all-MiniLM-L12-v2', device='cpu')
        self.qdrant_client = QdrantClient(
        url="https://b976d30b-c420-490a-af80-dde93b7c9434.us-east-1-0.aws.cloud.qdrant.io:6333", 
        api_key="DAXQsPthbMoA5R9kOfnloZ2BEIBeJeFIWdCchUTO2Bjrxtm8yepQ5A"
        )
        # self.qdrant_client = QdrantClient(host='localhost', port=6333)


    def search(self, text: str, filter_value: str = None) -> List[dict]:
        vector = self.model.encode(text).tolist()
        hits = self.qdrant_client.search(
            collection_name=self.collection_name,
            query_vector=vector,
            # query_filter=Filter(**filter_) if filter_ else None,
            query_filter=Filter(
                must=[
                    FieldCondition(
                        key="Artist",
                        match=MatchValue(value=filter_value)
                    )]
                ) if filter_value else None,
            limit=3
        )
        # return filter_value
        return [hit.payload for hit in hits]