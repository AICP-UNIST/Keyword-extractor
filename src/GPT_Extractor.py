import openai
from dotenv import load_dotenv
import os
load_dotenv()

def summarize(openai: any, answer: str) -> str:
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{
            'role': 'user',
            'content': f'이 내용 한국어로 세문장으로 요약해줘 ###\n{answer}\n###'
        }],
    )
    return completion.choices[0].message.content

def extract_keyword(openai: any, answer: str) -> str:
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{
            'role': 'user',
            'content': f'이 내용의 키워드 세 개를 추출해줘 ###\n{answer}\n###'
        }],
    )
    return completion.choices[0].message.content

if __name__ == '__main__':
    openai.api_key = os.environ.get("API_KEY")
    messages = []

    question = input()
    
    summarized = summarize(openai, question)
    print('------------SUMMARIZED-----------')
    print(summarized)
    print('---------------------------------')

    keyword = extract_keyword(openai, question)
    print('--------------KEYWORD------------')
    print(keyword)
    print('---------------------------------')

    messages.append({
        'role': 'assistant',
        'content': summarized
    })

    messages.append({
        'role': 'assistant',
        'content': keyword
    })