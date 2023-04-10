from rake_nltk import Rake

# 뉴스 기사 문자열을 입력하세요.
news_article = '''
여기에 뉴스 기사 내용을 넣으세요.
'''

# RAKE 객체 생성 및 불용어 설정
r = Rake()

# 키워드 추출
r.extract_keywords_from_text(news_article)

# 상위 3개 키워드 추출
top_keywords = r.get_ranked_phrases()[:3]

print("Top 3 Keywords:")
for keyword in top_keywords:
    print(keyword)
