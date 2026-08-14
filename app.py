import streamlit as st

from src.utils.save_file import save_uploaded_file
from src.ingestion.loader import load_pdf
from src.ingestion.chunk import chunk_text

from src.embedding.embed import create_embeddings

from src.retrieval.vector_store import create_faiss_index
from src.retrieval.search import retrieve_chunks

from src.llm.generate import generate_answer


st.set_page_config(
    page_title="Resume RAG Assistant",
    page_icon="🤖"
)

st.title("🤖 Resume RAG Assistant")

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

if uploaded_file:

    file_path = save_uploaded_file(uploaded_file)

    st.success("Resume Uploaded Successfully!")

    if st.button("Process Resume"):

        with st.spinner("Processing Resume..."):

            text = load_pdf(file_path)

            chunks = chunk_text(text)

            embeddings = create_embeddings(chunks)

            index = create_faiss_index(embeddings)

            st.session_state["chunks"] = chunks
            st.session_state["index"] = index

        st.success("Resume Processed Successfully!")

        st.write(f"Chunks Created: {len(chunks)}")


if "index" in st.session_state:

    st.divider()

    question = st.text_input(
        "Ask a question about the resume"
    )

    if st.button("Get Answer"):

        retrieved_chunks = retrieve_chunks(
            question,
            st.session_state["index"],
            st.session_state["chunks"]
        )

        context = "\n\n".join(retrieved_chunks)

        answer = generate_answer(
            question,
            context
        )

        st.subheader("Answer")

        st.write(answer)