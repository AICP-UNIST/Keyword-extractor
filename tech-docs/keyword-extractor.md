# Keyword-extractor

## Tech List

### 빈도 분석 (Frequency Analysis)

장점: 구현이 간단하고, 계산이 빠릅니다.

단점: 문맥이나 중요도를 고려하지 않으며, 불용어(stopwords) 처리가 필요합니다.

### TF-IDF (Term Frequency-Inverse Document Frequency)

장점: 단어의 중요도를 고려하여 키워드를 추출합니다. 문서의 개수가 많을수록 결과가 더 정확해집니다.

단점: 문장의 개수가 적은 경우에는 성능이 떨어질 수 있으며, 불용어 처리가 필요합니다.

### TextRank

장점: 문장의 문맥과 중요도를 고려하여 키워드를 추출하며, 불용어 처리가 덜 필요합니다.

단점: 계산 시간이 오래 걸릴 수 있으며, 하이퍼파라미터 조정이 필요할 수 있습니다.

### RAKE (Rapid Automatic Keyword Extraction)

장점: 구현이 간단하고 빠르며, 불용어 처리가 내장되어 있습니다.

단점: 문맥과 중요도를 고려하지 않아 다른 방법에 비해 성능이 떨어질 수 있습니다.

### BERT와 같은 신경망 기반 기술

장점: 문맥을 잘 파악하고, 키워드 추출 성능이 높습니다.

단점: 큰 모델이기 때문에 실행 시간과 메모리 소모가 크며, 사전 훈련된 모델이 필요합니다.