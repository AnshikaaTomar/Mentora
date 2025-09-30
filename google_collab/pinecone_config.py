import os
from pinecone import Pinecone

PINECONE_API_KEY = os.environ['PINECONE_API_KEY']
INDEX_NAME = "gbu-facts"

pc = Pinecone(api_key=PINECONE_API_KEY)

index = pc.Index(INDEX_NAME)
