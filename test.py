import streamlit as st
import random

st.set_page_config(page_title="음식 이상형 월드컵", page_icon="🍲", layout="wide")

# --- 음식 데이터 ---
foods = {
    "한식": [
        ("비빔밥", "bibimbap.jpeg"),
        ("불고기", "bulgogi.jpeg"),
        ("김치찌개", "kimchi.jpeg"),
        ("삼겹살", "samgyeopsal.jpeg"),
        ("떡볶이", "tteokbokki.jpeg"),
        ("삼계탕", "samgyetang.jpeg"),
        ("잡채", "japchae.jpeg"),
        ("갈비찜", "galbijjim.jpeg"),
        ("김밥", "gimbap.jpeg"),
        ("파전", "pajeon.jpeg"),
        ("냉면", "naengmyeon.jpeg"),
        ("순두부찌개", "soondubu.jpeg"),
        ("라면", "ramyeon.jpeg"),
        ("칼국수", "kalguksu.jpeg"),
        ("제육볶음", "jeyuk.jpeg"),
        ("콩나물국밥", "gokbap.jpeg"),
    ],
}

# -------------------------------
# 페이지 상태 관리
# -------------------------------
if "page" not in st.session_state:
    st.session_state.page = "home"
if "category" not in st.session_state:
    st.session_state.category = None
if "candidates" not in st.session_state:
    st.session_state.candidates = []
if "round" not in st.session_state:
    st.session_state.round = 1
if "rerun_needed" not in st.session_state:
    st.session_state.rerun_needed = False

# -------------------------------
# 홈 화면
# -------------------------------
if st.session_state.page == "home":
    st.title("🍴 음식 이상형 월드컵")
    st.subheader("원하는 카테고리를 선택하세요!")

    # 버튼을 세로로 배치
    for cat in ["한식", "양식", "일식"]:
        if st.button(cat):
            st.session_state.category = cat
            st.session_state.candidates = foods[cat].copy()
            random.shuffle(st.session_state.candidates)
            st.session_state.page = "worldcup"
            st.session_state.round = 1
            st.session_state.rerun_needed = True

# -------------------------------
# 월드컵 화면
# -------------------------------
elif st.session_state.page == "worldcup":
    st.title(f"🍜 {st.session_state.category} 월드컵")
    candidates = st.session_state.candidates

    if len(candidates) > 1:
        food1, food2 = candidates[0], candidates[1]
        st.subheader(f"Round {st.session_state.round}")

        col1, col2 = st.columns(2)
        with col1:
            if st.button(food1[0], key=f"{food1[0]}_{st.session_state.round}_1"):
                # food1 선택
                st.session_state.candidates = [food1] + candidates[2:]
                st.session_state.round += 1
                st.session_state.rerun_needed = True
        with col2:
            if st.button(food2[0], key=f"{food2[0]}_{st.session_state.round}_2"):
                # food2 선택
                st.session_state.candidates = [food2] + candidates[2:]
                st.session_state.round += 1
                st.session_state.rerun_needed = True

    else:
        st.success(f"🎉 최종 우승 음식은 {candidates[0][0]} 입니다! 🎉")
        st.balloons()  # 풍선 애니메이션

        if st.button("다시하기"):
            st.session_state.page = "home"
            st.session_state.round = 1
            st.session_state.rerun_needed = True

# -------------------------------
# 페이지 재실행
# -------------------------------
if st.session_state.rerun_needed:
    st.session_state.rerun_needed = False
    st.experimental_rerun()
