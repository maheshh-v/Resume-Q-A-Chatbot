from sentence_transformers import SentenceTransformer
from .pinecone_Vector_DB import get_or_create_index
import time

embedding_model = SentenceTransformer('all-MiniLM-L6-v2') 

def embed_and_upsert_chunks(chunks: list, filename: str, namespace: str):
    pinecone_index = get_or_create_index()
    timestamp = int(time.time())
    print(f"Processing {filename}...")

    batch_size = 32
    for i in range(0, len(chunks), batch_size):
        i_end = min(i + batch_size, len(chunks))
        batch = chunks[i:i_end]
        
        ids = [f"{filename}_{timestamp}_{i+j}" for j in range(len(batch))]
        embeddings = embedding_model.encode(batch).tolist()
        
        metadata = [{
            'text': text_chunk, 
            'source': filename,
            'char_count': len(text_chunk)
        } for text_chunk in batch]

        vectors_to_upsert = list(zip(ids, embeddings, metadata))
        pinecone_index.upsert(vectors=vectors_to_upsert, namespace=namespace)
        print(f"Batch {i // batch_size + 1} done")
    
    print(f"Finished {filename}")