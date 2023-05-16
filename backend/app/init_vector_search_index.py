import json
import os
import numpy as np

from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance

BATCH_SIZE = 256


if __name__ == '__main__':
    qdrant_client = QdrantClient(
        url="https://b976d30b-c420-490a-af80-dde93b7c9434.us-east-1-0.aws.cloud.qdrant.io:6333", 
        api_key="DAXQsPthbMoA5R9kOfnloZ2BEIBeJeFIWdCchUTO2Bjrxtm8yepQ5A"
    )
    # qdrant_client = QdrantClient(host='localhost', port=6333)

    vectors_path = './lyrics_vectors.npy'
    vectors = np.load(vectors_path)
    vector_size = vectors.shape[1]

    payload_path = './lyrics_payloads.json'
    with open(payload_path) as fd:
        payload = map(json.loads, fd)

        qdrant_client.recreate_collection(
            collection_name='lyrics',
            vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE)
        )

        qdrant_client.upload_collection(
            collection_name='lyrics',
            vectors=vectors,
            payload=payload,
            ids=None,
            # batch_size=BATCH_SIZE,
            # parallel=2
        )