import chromadb

from embeddings import create_embedding


client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_collection(
    name="company_documents"
)


def search_question(question, company_id):

    query_embedding = create_embedding(question)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3,
        where={
            "company_id": company_id
        }
    )
    return results

#result = search_question("كم سعر شاشة p5", 4)
#print(result)