import numpy as np

def search_index(index, query_embedding, chunks, top_k=2):

    distances, indices = index.search(
        np.array([query_embedding], dtype="float32"),
        top_k
    )

    results = []

    for idx in indices[0]:
        results.append(chunks[idx])

    return results