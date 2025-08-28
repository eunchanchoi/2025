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
if "stage" not in st.session_state:
    st.session_state.stage = "start"
if "category" not in st.session_state:
    st.session_state.category = None
if "current_round" not in st.session_state:
    st.session_state.current_round = []
if "match_index" not in st.session_state:
    st.session_state.match_index = 0
if "next_round" not in st.session_state:
    st.session_state.next_round = []
if "round_name" not in st.session_state:
    st.session_state.round_name = ""

# 시작 페이지
if st.session_state.stage == "start":
    st.subheader("원하는 음식을 선택하세요!")
    category = st.radio("카테고리 선택", ["아래 중에서 선택하십시오","한식", "양식", "일식"])
    if st.button("시작하기"):
        if category == "아래 중에서 선택하십시오":
            st.warning("⚠️ 음식 종류를 선택해주세요!")
        else:
            st.session_state.category = category
            st.session_state.current_round = random.sample(foods[category], 16)
            st.session_state.round_name = "16강"
            st.session_state.match_index = 0
            st.session_state.next_round = []
            st.session_state.stage = "playing"
            st.experimental_rerun()

# 게임 진행 페이지
elif st.session_state.stage == "playing":
    current_pair = st.session_state.current_round[st.session_state.match_index:st.session_state.match_index+2]
    st.subheader(f"{st.session_state.round_name} - 남은 경기: {len(st.session_state.current_round)//2 - st.session_state.match_index//2}")

    if len(current_pair) == 2:
        col1, col2 = st.columns(2)
        with col1:
            if st.button(current_pair[0]):
                st.session_state.next_round.append(current_pair[0])
                st.session_state.match_index += 2
                st.experimental_rerun()
        with col2:
            if st.button(current_pair[1]):
                st.session_state.next_round.append(current_pair[1])
                st.session_state.match_index += 2
                st.experimental_rerun()
    else:
        # 라운드 종료
        if len(st.session_state.next_round) == 1:
            st.success(f"🎉 최종 선택 음식: {st.session_state.next_round[0]} 🎉")
            st.balloons()  # 풍선 애니메이션
            st.session_state.stage = "finished"
        else:
            # 다음 라운드 준비
            st.session_state.current_round = st.session_state.next_round
            st.session_state.next_round = []
            st.session_state.match_index = 0
            # 라운드 이름 변경
            if len(st.session_state.current_round) == 8:
                st.session_state.round_name = "8강"
            elif len(st.session_state.current_round) == 4:
                st.session_state.round_name = "4강"
            elif len(st.session_state.current_round) == 2:
                st.session_state.round_name = "결승"
            st.experimental_rerun()

# 완료 페이지
elif st.session_state.stage == "finished":
    st.write("게임이 종료되었습니다. 새로고침하면 다시 플레이 가능합니다.")
