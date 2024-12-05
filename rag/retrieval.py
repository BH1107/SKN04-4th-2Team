from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS


# retriever 검색세팅
def retrieve_and_answer(faiss_path, fetch_k=20, k=1, lambda_mult=0.3):
    db = FAISS.load_local(
        folder_path=faiss_path,
        index_name='faiss_index',
        embeddings=OpenAIEmbeddings(model='text-embedding-3-small'),
        allow_dangerous_deserialization=True
    )

    retriever = db.as_retriever(
        search_type = 'mmr',
        search_kwargs={
            'fetch_k':fetch_k,
            'k': k,
            'lambda_mult': lambda_mult,
        }
    )

    return retriever