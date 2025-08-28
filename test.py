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

# -------------------------------
# 홈 화면
# -------------------------------
if st.session_state.page == "home":
    st.title("🍴 음식 이상형 월드컵")
    st.subheader("원하는 카테고리를 선택하세요!")

    if st.button("양식"):
        st.session_state.category = "양식"
        st.session_state.candidates = foods.get("양식", []).copy()
        random.shuffle(st.session_state.candidates)
        st.session_state.page = "worldcup"
        st.experimental_rerun()

    if st.button("일식"):
        st.session_state.category = "일식"
        st.session_state.candidates = foods.get("일식", []).copy()
        random.shuffle(st.session_state.candidates)
        st.session_state.page = "worldcup"
        st.experimental_rerun()

    if st.button("한식"):
        st.session_state.category = "한식"
        st.session_state.candidates = foods.get("한식", []).copy()
        random.shuffle(st.session_state.candidates)
        st.session_state.page = "worldcup"
        st.experimental_rerun()

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
            st.image(f"images/{food1[1]}", use_column_width=True)
            if st.button(food1[0], key=f"{food1[0]}"):
                st.session_state.candidates = [food1] + candidates[2:]
                st.session_state.round += 1
                st.experimental_rerun()
        with col2:
            st.image(f"images/{food2[1]}", use_column_width=True)
            if st.button(food2[0], key=f"{food2[0]}"):
                st.session_state.candidates = [food2] + candidates[2:]
                st.session_state.round += 1
                st.experimental_rerun()

    else:
        st.balloons()  # 풍선 애니메이션
        st.success(f"🎉 최종 우승 음식은 {candidates[0][0]} 입니다!")
        if st.button("다시하기"):
            st.session_state.page = "home"
            st.session_state.round = 1
            st.session_state.candidates = []
            st.experimental_rerun()
