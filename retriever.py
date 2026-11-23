import chromadb

from embeddings import create_embedding


client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_collection(
    name="company_documents"
)


def search_question(question, company_id, max_distance=0.6):

    query_embedding = create_embedding(question)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3,
        where={"company_id": company_id},
        include=["documents", "distances"],
    )

    docs = results["documents"][0]
    distances = results["distances"][0]

    relevant = []
    for d, dist in zip(docs, distances):
        if dist <= max_distance:
            relevant.append(d)

    if not relevant:
        return None

    return "\n\n".join(relevant)

#result = search_question("كم سعر شاشة p5", 4)
#print(result)