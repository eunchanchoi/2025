import streamlit as st

# 페이지 상태 초기화
if "page" not in st.session_state:
    st.session_state.page = 1

# 선택값 초기화
for key in ["head", "body", "arm", "feature", "personality"]:
    if key not in st.session_state:
        st.session_state[key] = None

# ---------------------------
# 페이지 1: 부품 선택
# ---------------------------
if st.session_state.page == 1:
    st.title("🤖 나만의 로봇 만들기 - 부품 선택")
    st.session_state.head = st.selectbox("머리 🧑", ["🤖", "👩", "🐱", "👽", "🎩"])
    st.session_state.body = st.selectbox("몸통 🦾", ["🦾", "👕", "🐻", "🦖", "💎"])
    st.session_state.arm = st.selectbox("팔 💪", ["💪", "🦿", "🪽", "🐙", "⚡"])
    st.session_state.feature = st.selectbox("기능 ⚙️", ["🔊 음악", "🛡️ 방어", "🚀 날기", "🧮 계산", "🌱 치유"])
    st.session_state.personality = st.selectbox("성격 😎", ["😊 친절함", "🤓 똑똑함", "😈 장난꾸러기", "🧐 진지함", "😂 개그"])

    if st.button("➡️ 다음 페이지"):
        st.session_state.page = 2

# ---------------------------
# 페이지 2: 로봇 미리보기
# ---------------------------
elif st.session_state.page == 2:
    st.title("✨ 나만의 로봇 완성 ✨")

    # HTML로 부품 위치 배치
    robot_html = f"""
    <div style='text-align:center; font-size:80px; position: relative;'>
        <div style='position:relative; top:0px;'>{st.session_state.head}</div>
        <div style='position:relative; top:-20px;'>{st.session_state.body}</div>
        <div style='position:relative; top:-40px;'>{st.session_state.arm}</div>
    </div>
    """

    # 풍선 애니메이션
    balloons_html = """
    <style>
    @keyframes floatUp {
        0% { transform: translateY(0px); }
        100% { transform: translateY(-500px); }
    }
    .balloon {
        font-size:40px;
        position: absolute;
        animation: floatUp 5s linear infinite;
    }
    </style>
    <div style='position:relative; height:200px;'>
        <div class='balloon' style='left:10%'>🎈</div>
        <div class='balloon' style='left:30%'>🎈</div>
        <div class='balloon' style='left:50%'>🎈</div>
        <div class='balloon' style='left:70%'>🎈</div>
        <div class='balloon' style='left:90%'>🎈</div>
    </div>
    """

    st.markdown(robot_html, unsafe_allow_html=True)
    st.markdown(balloons_html, unsafe_allow_html=True)

    if st.button("⬅️ 이전 페이지"):
        st.session_state.page = 1
    if st.button("➡️ 다음 페이지"):
        st.session_state.page = 3

# ---------------------------
# 페이지 3: 최종 기능 소개
# ---------------------------
elif st.session_state.page == 3:
    st.title("🚀 최종 로봇 기능 소개")
    st.write(f"당신의 로봇은 {st.session_state.feature} 능력을 가지고 있고,")
    st.write(f"{st.session_state.personality} 성격을 가진 특별한 로봇이에요!")
    st.success("멋진 로봇을 완성했네요! 🎉")

    if st.button("⬅️ 이전 페이지"):
        st.session_state.page = 2
