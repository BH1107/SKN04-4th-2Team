from operator import itemgetter
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


def prompting(retriever, question=''):
    template = ''' 
    너는 노트북를 추천해주는 봇이야.
    사용자의 질문에 따라서 여러가지의 노트북의 사양을 비교해서 정리해주거나
    특정 모델명의 노트북의 사양을 정확하게 알려줘 노트북 모델을 추천 할 때는 정확한 모델명을 알려줘
    만약 사용자가 정확한 노트북의 정보를 입력하지 않아서 특정 노트북 모델을 찾을 수 없다면 
    사용자에게 더 세밀한 질문을 원한다고 말해 대답은 한글로 명확하고 자세히 알려줘.
    노트북과 관련된 내용이 아니라면 관련된 내용을 찾을 수 없다고 알려줘.
    노트북을 추천해달라는 문의가 들어오면 가격이 싸고 가벼운 것을 기준으로 알려줘
    가격이 비슷하다면 성능이 조금 더 좋은 것으로 알려줘.

    질문: {question}

    내용: {reference}

    언어: {language}
    '''

    prompt = PromptTemplate(
        template=template,
        input_variables=['question', 'reference', 'language'],
    )
    model = ChatOpenAI(model='gpt-4o-mini')
    parser = StrOutputParser()
    chain = (
        {
            'reference': itemgetter('question') | retriever,
            'question': itemgetter('question'),
            'language': itemgetter('language'),
        }
        | prompt
        | model
        | parser
    )

    # chain을 통해 question
    reference = chain.invoke(
        {
            'question': f'{question}',
            'language': '한국어',
        }
    )
    
    return reference