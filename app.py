import streamlit as st

# 발명품 추천 점수표
inventions = {
    '스마트 안마 침대': 0,
    'AI 숙제 로봇': 0,
    '멀티 가전 로봇': 0,
    '스마트 쿠커': 0,
    '스마트 신발': 0,
    '스마트 옷': 0,
    '휴대용 에너지 부스터': 0,
    '수면 모니터링 베개': 0,
    '집중력 강화 헤드밴드': 0,
    '스트레스 해소 팔찌': 0,
    '자기계발 AI 코치': 0,
    '편리한 생활 보조 장치': 0,
    '스마트 책상': 0,
    'AI 패션 스타일러': 0,
    '모바일 헬스 코치': 0,
    '자동 정리 로봇': 0,
    '스마트 조명 시스템': 0,
    '휴대용 미니 공기청정기': 0,
    '다기능 키친 로봇': 0,
    '자율 주행 카트': 0,
    'AI 여행 플래너': 0,
    '언어 학습 로봇': 0,
    '가상 현실 운동 기기': 0,
    '스마트 거울': 0,
    '맞춤형 음악 생성기': 0,
    '스마트 텐트': 0,
    '휴대용 태양광 충전기': 0,
    'AI 감정 분석기': 0,
    '맞춤형 스킨케어 기기': 0,
    '스마트 원예 로봇': 0
}

# 질문 및 세분화 옵션
questions = {
    'Q1. 요즘 가장 필요한 건 무엇인가요?': [
        '에너지 보충 (커피, 음료 등)',
        '깊은 숙면과 회복',
        '집중력 향상',
        '스트레스 해소',
        '자기계발/동기부여',
        '편리한 생활 보조'
    ],
    'Q2. 요즘 가장 귀찮은 일은 무엇인가요?': [
        '집안일 (청소, 빨래)',
        '요리',
        '공부/업무',
        '외출 준비',
        '정리정돈',
        '관리해야 하는 것'
    ],
    'Q3. 원하는 편의성은 무엇인가요?': [
        '자동화된 생활',
        '즉각적인 피드백',
        '원격 제어',
        '맞춤형 추천',
        '휴대 가능',
        '다기능'
  
    'Q4. 공부/업무 효율을 높이는 방법?': [
        '집중력 향상 기기',
        'AI 보조',
        '자동 정리 도구',
        '시간 관리',
        '학습 분석',
        '동기 부여'
  
    'Q5. 패션/라이프스타일에서 원하는 변화?': [
        '옷 스타일 변화',
        '액세서리 스마트화',
        '홈 데코 자동화',
        '편리한 여행',
        '맞춤형 기기',
        '다기능 사용'
    ]
}

st.set_page_config(page_title='💡기발한 발명품 추천기💡', page_icon='🚀', layout='centered')
st.title('🌟 나만의 발명품 찾기 퀴즈 🌟')
st.write('아래 10개의 질문에 답하면 당신에게 딱 맞는 발명품을 추천합니다!')

# 사용자 선택 저장
user_answers = {}

for q, opts in questions.items():
    st.markdown(f"<h3 style='font-size:20px'>{q}</h3>", unsafe_allow_html=True)
    user_answers[q] = st.selectbox('선택하세요:', opts, key=q)

# 점수 계산 (간단히 선택 순서로 점수 부여)
for i, (q, opts) in enumerate(questions.items()):
    answer = user_answers[q]
    index = opts.index(answer)
    # 각 질문마다 인덱스가 낮을수록 앞쪽 발명품에 점수
    for j, inv in enumerate(inventions.keys()):
        inventions[inv] += max(0, len(opts) - abs(j - index))

# 추천 발명품 출력
if st.button('추천 받기 🚀'):
    recommended = max(inventions, key=inventions.get)
    st.success(f'✨ 당신을 위한 발명품: {recommended}')
