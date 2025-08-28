import streamlit as st
import random

st.set_page_config(page_title="음식 이상형 월드컵", page_icon="🍲", layout="wide")

# --- 음식 데이터 ---
food_data = {
    "한식": [
        {"name":"비빔밥", "img": "bibimbap.jpeg"},
        {"name":"불고기", "img": "bulgogi.jpeg"},
        {"name":"김치찌개", "img": "kimchi.jpeg"},
        {"name":"삼겹살", "img": "samgyeopsal.jpeg"},
        {"name":"떡볶이", "img": "tteokbokki.jpeg"},
        {"name":"삼계탕", "img": "samgyetang.jpeg"},
        {"name":"잡채", "img": "japchae.jpeg"},
        {"name":"갈비찜", "img": "galbijjim.jpeg"},
        {"name":"김밥", "img": "gimbap.jpeg"},
        {"name":"파전", "img": "pajeon.jpeg"},
        {"name":"냉면", "img": "naengmyeon.jpeg"},
        {"name":"순두부찌개", "img": "soondubu.jpeg"},
        {"name":"라면", "img": "ramyeon.jpeg"},
        {"name":"칼국수", "img": "kalguksu.jpeg"},
        {"name":"제육볶음", "img": "jeyuk.jpeg"},
        {"name":"콩나물국밥", "img": "gokbap.jpeg"},
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
        st.experimental_rerun()

# 토너먼트 화면
elif st.session_state.stage == "tournament":
    idx = st.session_state.round_index
    food_pair = st.session_state.food_list[idx:idx+2]

    # 남은 음식이 1개뿐이면 자동으로 다음 라운드로
    if len(food_pair) == 1:
        st.session_state.next_round.append(food_pair[0])
        st.session_state.round_index += 1
        st.experimental_rerun()

    col1, col2 = st.columns(2)

    with col1:
    st.image(food_pair[0]["img"], use_column_width=True)
    if st.button(food_pair[0]["name"], key=f"{idx}_0"):
        st.session_state.next_round.append(food_pair[0])
        st.session_state.round_index += 2
        st.experimental_rerun()  # 여기서만 호출

with col2:
    st.image(food_pair[1]["img"], use_column_width=True)
    if st.button(food_pair[1]["name"], key=f"{idx}_1"):
        st.session_state.next_round.append(food_pair[1])
        st.session_state.round_index += 2
        st.experimental_rerun()  # 여기서만 호출

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
