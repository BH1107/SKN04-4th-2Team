from dotenv import load_dotenv
import os
import openai

from rag.prompt import prompting
from rag.retrieval import retrieve_and_answer

# 환경변수 불러오기
load_dotenv()

# 환경변수 세팅
openai.api_key = os.getenv("OPENAI_API_KEY")
csv_path = os.getenv("csv_path")
faiss_path = os.getenv("faiss_path")

# Chat 기능
def chat(question:str):
    # rag데이터베이스의 내용을 가져와 검색을 세팅하여 답변호출
    retriever = retrieve_and_answer(faiss_path=faiss_path)
    response = prompting(retriever, question=question)

    print(f'Answer : \n{response}')
    return response

chat("Asus에서 괜찮은 노트북 3개를 추천해줘")