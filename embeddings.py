import os
from dotenv import load_dotenv
from google import genai
from crudfiles import get_company_content
from chunker import text_splitter
from vector_db import collection

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)


def create_embedding(text):

    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text
    )

    return response.embeddings[0].values


def build_embeddings(company_id):

    text = get_company_content(company_id)

    chunks = text_splitter.split_text(text)

    for i, chunk in enumerate(chunks):
        embedding = create_embedding(chunk)
        collection.add(
            ids=[f"company_{company_id}_chunk{i}"],
            documents=[chunk],
            embeddings=[embedding],
            metadatas=[
                {
                    "company_id": company_id,
                    "chunk_index": i
                }
            ]
        )
        

        #print(
            #f"Stored chunk {i} "
            #f"| embedding size: {len(embedding)}"
        #)


#build_embeddings(4)





