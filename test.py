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

(2)
        with col1:
            if st.button(food1, use_container# --- 초기 세팅 ---
if "page" not in st.session_state:
    st.session_state.page = "home"
if "category" not in st.session_state:
    st.session_state.category = None
if "candidates" not in st.session_state:
    st.session_state.candidates = []
if "round" not in st.session_state:
    st.session_state.round = 1

# -------------------------------
# 홈 화면
# -------------------------------
if st.session_state.page == "home":
    st.title("🍴 음식 이상형 월드컵")


# -------------------------------
# 월드컵 화면
# -------------------------------
elif st.session_state.page == "worldcup":
    st.title(f"🍜 {st.session_state.category} 월드컵")
    candidates = st.session_state.candidates

    if len(candidates) > 1:
        food1, food2 = candidates[0], candidates[1]
        st.subheader(f"Round {st.session_state.round}")

        col1, col2 = st.columns_width=True):
                st.session_state.candidates = candidates[1:]  # food1 선택
                st.session_state.round += 1
                st.experimental_rerun()
        with col2:
            if st.button(food2, use_container_width=True):
                st.session_state.candidates = [food1] + candidates[2:]  # food2 선택
                st.session_state.round += 1
                st.experimental_rerun()

    else:
        st.success(f"🎉 최종 우승 음식은 {candidates[0]} 입니다!")
        if st.button("다시하기"):
            st.session_state.page = "home"
            st.session_state.round = 1
            st.experimental_rerun()

