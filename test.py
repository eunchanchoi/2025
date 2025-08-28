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
    "양식": [
        ("피자", "images/pizza.jpg"),
        ("스파게티", "images/spaghetti.jpg"),
        ("스테이크", "images/steak.jpg"),
        ("햄버거", "images/burger.jpg"),
        ("리조또", "images/risotto.jpg"),
        ("샐러드", "images/salad.jpg"),
        ("치킨", "images/fried_chicken.jpg"),
        ("라자냐", "images/lasagna.jpg"),
        ("핫도그", "images/hotdog.jpg"),
        ("타코", "images/taco.jpg"),
        ("샌드위치", "images/sandwich.jpg"),
        ("감바스", "images/gambas.jpg"),
        ("치즈볼", "images/cheeseball.jpg"),
        ("브라우니", "images/brownie.jpg"),
        ("파스타", "images/pasta.jpg"),
        ("그라탕", "images/gratin.jpg"),
    ],
    "일식": [
        ("초밥", "images/sushi.jpg"),
        ("라멘", "images/ramen.jpg"),
        ("돈까스", "images/tonkatsu.jpg"),
        ("우동", "images/udon.jpg"),
        ("규동", "images/gyudon.jpg"),
        ("오코노미야끼", "images/okonomiyaki.jpg"),
        ("타코야끼", "images/takoyaki.jpg"),
        ("가라아게", "images/karaage.jpg"),
        ("사시미", "images/sashimi.jpg"),
        ("텐동", "images/tendon.jpg"),
        ("규카츠", "images/gyukatsu.jpg"),
        ("오니기리", "images/onigiri.jpg"),
        ("카레라이스", "images/curry_rice.jpg"),
        ("쇼유라멘", "images/shoyu_ramen.jpg"),
        ("미소시루", "images/miso_soup.jpg"),
        ("야키소바", "images/yakisoba.jpg"),
    ]
}

# --- 초기 세팅 ---
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

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("양식"):
            st.session_state.category = "양식"
            st.session_state.candidates = foods["양식"].copy()
            random.shuffle(st.session_state.candidates)
            st.session_state.page = "worldcup"
            st.experimental_rerun()
    with col2:
        if st.button("일식"):
            st.session_state.category = "일식"
            st.session_state.candidates = foods["일식"].copy()
            random.shuffle(st.session_state.candidates)
            st.session_state.page = "worldcup"
            st.experimental_rerun()
    with col3:
        if st.button("한식"):
            st.session_state.category = "한식"
            st.session_state.candidates = foods["한식"].copy()
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
            if st.button(food1, use_container_width=True):
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
