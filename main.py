import streamlit as st

# ===== MBTI별 파스텔톤 배경색 데이터 =====
mbti_colors = {
    "INTJ": "#C3B1E1",  # 연보라
    "INTP": "#B5EAD7",  # 민트
    "ENTJ": "#FFDAC1",  # 살구
    "ENTP": "#FFB7B2",  # 코랄핑크
    "INFJ": "#E2F0CB",  # 연두
    "INFP": "#FBC4AB",  # 피치
    "ENFJ": "#FFECB3",  # 크림옐로우
    "ENFP": "#FFD6E0",  # 연핑크
    "ISTJ": "#D0E6A5",  # 파스텔 라임
    "ISFJ": "#AED9E0",  # 하늘민트
    "ESTJ": "#F7D9C4",  # 연살구
    "ESFJ": "#FFF5BA",  # 파스텔 옐로우
    "ISTP": "#B5EAEA",  # 파스텔 블루
    "ISFP": "#FFB5E8",  # 연분홍
    "ESTP": "#B8F2E6",  # 연청록
    "ESFP": "#F2B5D4",  # 핑크퍼플
}

# ===== MBTI별 직업 데이터 =====
mbti_jobs = {
    "INTJ": ["🧠 데이터 과학자", "📊 전략 컨설턴트", "🔬 연구원"],
    "INTP": ["💻 소프트웨어 개발자", "🧪 이공계 연구원", "💡 발명가"],
    "ENTJ": ["🏢 기업가", "📈 경영 컨설턴트", "📋 프로젝트 매니저"],
    "ENTP": ["🎯 마케팅 디렉터", "🚀 벤처 창업가", "📝 기획자"],
    "INFJ": ["💬 심리상담가", "✍️ 작가", "🎓 교수"],
    "INFP": ["🎨 예술가", "🎼 작곡가", "🤝 사회복지사"],
    "ENFJ": ["👩‍🏫 교사", "🧑‍💼 인사 전문가", "📢 홍보 전문가"],
    "ENFP": ["📺 광고 기획자", "🎉 이벤트 플래너", "📚 작가"],
    "ISTJ": ["📑 회계사", "🏛 행정 공무원", "⚖ 변호사"],
    "ISFJ": ["💉 간호사", "📖 교사", "📚 사서"],
    "ESTJ": ["🎖 군 장교", "💼 경영자", "📊 세무사"],
    "ESFJ": ["👩‍🏫 초등교사", "🧑‍💼 인사담당자", "🤝 사회복지사"],
    "ISTP": ["🔧 기계공", "✈️ 파일럿", "🚑 응급 구조사"],
    "ISFP": ["🎨 디자이너", "📸 사진작가", "👐 물리치료사"],
    "ESTP": ["💼 영업 전문가", "🎯 이벤트 코디네이터", "🏋️ 스포츠 코치"],
    "ESFP": ["🎭 배우", "🎤 가수", "🧳 여행 가이드"]
}

# ===== 앱 제목 =====
st.set_page_config(page_title="MBTI 직업 추천", page_icon="💼", layout="centered")
st.title("💼 MBTI 기반 직업 추천 앱 💼")
st.write("**당신의 MBTI에 맞는 직업 추천을 받아보세요! 🔮**")

# ===== MBTI 선택 =====
mbti = st.selectbox(
    "👇 당신의 MBTI 유형을 선택하세요:",
    list(mbti_jobs.keys())
)

# ===== 배경색 적용 (선택한 MBTI 색상) =====
bg_color = mbti_colors.get(mbti, "#FFFFFF")
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {bg_color};
        color: #333333;
        font-family: 'Arial';
    }}
    div.stButton > button:first-child {{
        background-color: white;
        color: #333333;
        border-radius: 10px;
        height: 3em;
        font-size: 1.1em;
        font-weight: bold;
        border: 2px solid #ccc;
        transition: 0.3s;
    }}
    div.stButton > button:first-child:hover {{
        background-color: #f0f0f0;
        transform: scale(1.05);
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ===== 버튼 클릭 시 결과 출력 =====
if st.button("🌸 직업 추천 받기 🌸"):
    jobs = mbti_jobs.get(mbti, [])
    if jobs:
        st.success(f"🎯 **{mbti} 유형 추천 직업**")
        for job in jobs:
            st.write(f"- {job}")
    else:
        st.error("⚠ 해당 MBTI 유형에 대한 데이터가 없습니다.")

# ===== 추가 정보 =====
st.write("---")
st.info("💡 MBTI는 참고용 도구일 뿐이며, 진로 선택은 다양한 경험과 자기 이해를 기반으로 해야 합니다.")
