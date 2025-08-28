import streamlit as st
import random

st.set_page_config(page_title="음식 이상형 월드컵", page_icon="🍲", layout="wide")

# --- 음식 데이터 ---
food_data = {
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
if "stage" not in st.session_state:
    st.session_state.stage = "select_type"
if "food_list" not in st.session_state:
    st.session_state.food_list = []
if "next_round" not in st.session_state:
    st.session_state.next_round = []
if "round_index" not in st.session_state:
    st.session_state.round_index = 0

# 처음 화면: 음식 종류 선택
if st.session_state.stage == "select_type":
    st.title("🍴 음식 이상형 월드컵")
    choice = st.radio("음식 종류를 선택하세요", ("한식", "양식", "일식"))
    if st.button("시작"):
        st.session_state.food_list = random.sample(food_data[choice], 16)
        st.session_state.stage = "tournament"

# 토너먼트 화면
elif st.session_state.stage == "tournament":
    idx = st.session_state.round_index
    food_pair = st.session_state.food_list[idx:idx+2]

    col1, col2 = st.columns(2)

    with col1:
        if st.button(food_pair[0]["name"]):
            st.session_state.next_round.append(food_pair[0])
            st.session_state.round_index += 2
            st.experimental_rerun()
        st.image(food_pair[0]["img"], use_column_width=True)

    with col2:
        if st.button(food_pair[1]["name"]):
            st.session_state.next_round.append(food_pair[1])
            st.session_state.round_index += 2
            st.experimental_rerun()
        st.image(food_pair[1]["img"], use_column_width=True)

    # 라운드 끝 처리
    if st.session_state.round_index >= len(st.session_state.food_list):
        if len(st.session_state.next_round) == 1:
            st.session_state.stage = "winner"
        else:
            st.session_state.food_list = st.session_state.next_round
            st.session_state.next_round = []
            st.session_state.round_index = 0
            st.experimental_rerun()

# 우승자 화면
elif st.session_state.stage == "winner":
    st.title("🏆 최종 우승!")
    st.image(st.session_state.food_list[0]["img"], use_column_width=True)
    st.subheader(st.session_state.food_list[0]["name"])
