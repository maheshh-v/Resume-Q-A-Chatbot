import getpass
import os
from dotenv import load_dotenv

from pinecone import Pinecone, ServerlessSpec

load_dotenv()  
if not os.getenv("PINECONE_API_KEY"):
    os.environ["PINECONE_API_KEY"] = getpass.getpass("Enter your Pinecone API key: ")

pinecone_api_key = os.environ.get("PINECONE_API_KEY")

pc = Pinecone(api_key=pinecone_api_key)


# Create a dense index with integrated embedding
# Your existing code for getting the API key and creating `pc`...

INDEX_NAME = "resume-rag-index" # Choose a name for your index
EMBEDDING_DIMENSION = 384 # ⚠️ IMPORTANT: Change this to your model's actual dimension

def get_or_create_index():
    """
    Checks if a Pinecone index exists. If not, it creates one.
    Then, it connects to the index and returns the index object.
    """
    print(f"Checking for index '{INDEX_NAME}'...")
    
    # 1. Check if the index already exists.
    # The pc object has a method to list all index names.

    if not pc.has_index(INDEX_NAME):
        pc.create_index(
            name=INDEX_NAME,
            dimension=EMBEDDING_DIMENSION,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1"),
        )
        
    else:
        print(f"Index '{INDEX_NAME}' already exists. Connecting...")
    
    index = pc.Index(INDEX_NAME)
    return index

# You can test your function like this:
if __name__ == '__main__':
    resume_index = get_or_create_index()
    print("Successfully connected to the index!")
    print(resume_index.describe_index_stats()) # This will show you stats about your index


