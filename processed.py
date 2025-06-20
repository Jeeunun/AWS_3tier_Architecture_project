import re

def clean_article(text):
    # Windows 줄바꿈 CRLF를 LF로 통일
    text = text.replace('\r\n', '\n')

    # 1. /사진=이 포함된 문장 전체 삭제
    text = re.sub(r'.*?/사진=.*(?:\n|$)', '', text)
     # 사진 관련 문장 삭제
    text = re.sub(r'.*?\(사진\).*(?:\n|$)', '', text)  # (사진)이 포함된 문장 삭제
    text = re.sub(r'.*?사진=.*(?:\n|$)', '', text)     # 사진=이 포함된 문장 삭제
    text = re.sub(r'.*?게티이미지뱅크.*(?:\n|$)', '', text)  # 게티이미지뱅크가 포함된 문장 삭제
    text = re.sub(r'.*?출처=.*(?:\n|$)', '', text)     # 출처=이 포함된 문장 삭제

    # 2. '이미지 크게보기', 'ADVERTISEMENT' 제거
    text = re.sub(r'이미지 크게보기', '', text)
    text = re.sub(r'ADVERTISEMENT', '', text)

    # 3. 기자 이름과 이메일 포함 문장 삭제
    text = re.sub(r'.*기자.*?[\w\.-]+@[\w\.-]+', '', text)

    # 4. 특수기호(예: ◇, ※, ▶ 등) 삭제s
    # text = re.sub(r'.[◇※▶●◆■▣★☆♦▶▷❖✔✦✧]', '', text)
    text = re.sub(r'[^a-zA-Z0-9\s가-힣]', '', text)
    
    # 5. 공백 정리
    text = re.sub(r'\n{2,}', '\n', text)  # 여러 줄바꿈 → 1개 줄바꿈
    text = re.sub(r'[ \t]{2,}', ' ', text)  # 여러 공백/탭 → 1칸

    # 6. 앵커, 기자 삭제
    # if text=='[앵커]' or text=='[ 앵커 ]' or text=='[기자]' or text=='[ 기자 ]':
    #     text = text.replace(text, '')

    return text.strip()
