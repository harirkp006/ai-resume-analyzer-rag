from src.ingestion.loader import load_pdf
from src.ingestion.chunk import chunk_text
from src.embedding.embed import create_embeddings
from src.retrieval.vector_store import create_faiss_index
from src.retrieval.retrieve import search_index
from src.llm.generate import generate_answer

pdf_path = "data/resumes/h-1.pdf"

print("Loading Resume...")

text = load_pdf(pdf_path)

chunks = chunk_text(text)

embeddings = create_embeddings(chunks)

index = create_faiss_index(embeddings)

print("Resume Loaded Successfully!")
print(f"Total Chunks: {len(chunks)}")

while True:

    query = input("\nAsk a Question (type 'exit' to quit): ")

    if query.lower() == "exit":
        break

    query_embedding = create_embeddings([query])[0]

    results = search_index(
        index,
        query_embedding,
        chunks,
        top_k=2
    )

    context = "\n".join(results)

    answer = generate_answer(
        query=query,
        context=context
    )

    print("\nAnswer:\n")
    print(answer)